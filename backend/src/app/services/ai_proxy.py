"""
AI代理服务
用于调用AI模型生成文章目录等功能
"""
import asyncio
import json
import re
from typing import Optional, List, Dict
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

# 文章内容最小长度阈值（字符）
MIN_CONTENT_LENGTH_FOR_CATALOG = 500

# 目录生成提示词模板
CATALOG_PROMPT_TEMPLATE = """
请帮我为以下文章内容生成一个结构化的章节目录。

文章内容：
{content}

要求：
1. 只提取文章中的主要标题和子标题
2. 使用中文输出
3. 目录级别不超过3级
4. 如果文章内容太少或没有明确的章节结构，请返回空列表
5. 返回格式为JSON数组，包含level（层级）和title（标题）字段

示例输出：
[
  {"level": 1, "title": "引言"},
  {"level": 2, "title": "背景介绍"},
  {"level": 1, "title": "核心概念"},
  {"level": 2, "title": "定义与特点"},
  {"level": 2, "title": "应用场景"},
  {"level": 1, "title": "总结"}
]
"""

class AIProxyService:
    def __init__(self):
        self.default_model = None
    
    async def generate_catalog(self, content: str, model_config=None) -> List[Dict[str, str]]:
        """
        生成文章目录
        
        Args:
            content: 文章内容
            model_config: AI模型配置
        
        Returns:
            章节目录列表
        """
        # 如果内容太短，返回空目录
        if len(content.strip()) < MIN_CONTENT_LENGTH_FOR_CATALOG:
            logger.info(f"文章内容过短（{len(content)}字符），跳过目录生成")
            return []
        
        try:
            # 优先使用提供的模型配置
            config = model_config or self.default_model
            
            if not config:
                logger.warning("未配置AI模型，使用本地目录提取")
                return self.extract_catalog_from_html(content)
            
            # 调用AI模型生成目录
            return await self.call_ai_model(content, config)
        
        except Exception as e:
            logger.error(f"AI生成目录失败: {str(e)}")
            # 降级处理：使用本地目录提取
            logger.info("降级到本地目录提取")
            return self.extract_catalog_from_html(content)
    
    async def call_ai_model(self, content: str, config) -> List[Dict[str, str]]:
        """
        调用AI模型
        
        Args:
            content: 文章内容
            config: AI模型配置
        
        Returns:
            AI返回的目录列表
        """
        import httpx
        
        prompt = CATALOG_PROMPT_TEMPLATE.format(content=content[:3000])  # 限制内容长度
        
        headers = {
            "Content-Type": "application/json"
        }
        
        if config.api_key:
            headers["Authorization"] = f"Bearer {config.api_key}"
        
        payload = {
            "model": config.model_type,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": config.max_tokens,
            "temperature": config.temperature,
            "timeout": config.timeout
        }
        
        try:
            async with httpx.AsyncClient(timeout=config.timeout) as client:
                response = await client.post(
                    config.api_url,
                    headers=headers,
                    json=payload
                )
                
                response.raise_for_status()
                result = response.json()
                
                # 解析AI返回结果
                return self.parse_ai_response(result)
                
        except httpx.TimeoutException:
            raise Exception(f"请求超时（{config.timeout}秒）")
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP错误: {e.response.status_code}")
        except Exception as e:
            raise Exception(f"调用失败: {str(e)}")
    
    def parse_ai_response(self, response: dict) -> List[Dict[str, str]]:
        """
        解析AI模型返回的结果
        
        Args:
            response: AI模型返回的响应
        
        Returns:
            解析后的目录列表
        """
        try:
            # 不同模型返回格式可能不同
            if "choices" in response:
                content = response["choices"][0]["message"]["content"]
            elif "result" in response:
                content = response["result"]
            elif "content" in response:
                content = response["content"]
            else:
                content = str(response)
            
            # 提取JSON部分
            match = re.search(r'\[.*\]', content, re.DOTALL)
            if match:
                json_str = match.group()
                catalog = json.loads(json_str)
                
                # 验证格式
                if isinstance(catalog, list):
                    return catalog
            
            # 如果不是JSON格式，尝试解析为列表
            return self.extract_catalog_from_text(content)
            
        except Exception as e:
            logger.error(f"解析AI响应失败: {str(e)}")
            return []
    
    def extract_catalog_from_html(self, content: str) -> List[Dict[str, str]]:
        """
        从HTML内容中提取目录
        
        Args:
            content: HTML内容
        
        Returns:
            目录列表
        """
        catalog = []
        # 匹配h1-h6标签
        headings = re.findall(r'<h([1-6])[^>]*>(.*?)</h\1>', content, re.DOTALL)
        
        for level, text in headings:
            # 移除标签内的HTML标签
            text = re.sub(r'<[^>]+>', '', text).strip()
            
            if text and len(text) <= 100:  # 过滤过长的标题
                catalog.append({
                    'level': int(level),
                    'title': text
                })
        
        return catalog
    
    def extract_catalog_from_text(self, text: str) -> List[Dict[str, str]]:
        """
        从纯文本中提取目录
        
        Args:
            text: 纯文本内容
        
        Returns:
            目录列表
        """
        catalog = []
        
        # 尝试匹配常见的目录格式
        lines = text.strip().split('\n')
        level_pattern = re.compile(r'^(\s*[\d\-\*]+)\s+(.+)')
        
        for line in lines:
            match = level_pattern.match(line)
            if match:
                prefix = match.group(1)
                title = match.group(2).strip()
                
                # 根据前缀判断层级
                if '1.' in prefix or '一、' in prefix or '第[一二三四五]章' in prefix:
                    level = 1
                elif '1.1' in prefix or '1)' in prefix:
                    level = 2
                else:
                    level = 3
                
                if title and len(title) <= 100:
                    catalog.append({
                        'level': level,
                        'title': title
                    })
        
        return catalog
    
    def set_default_model(self, model_config):
        """设置默认模型配置"""
        self.default_model = model_config

# 全局AI代理服务实例
ai_proxy_service = AIProxyService()

# 同步包装函数
def generate_catalog_sync(content: str, model_config=None) -> List[Dict[str, str]]:
    """同步生成文章目录"""
    return asyncio.run(ai_proxy_service.generate_catalog(content, model_config))

# 测试示例
if __name__ == "__main__":
    test_content = """
    <h1>深入理解人工智能</h1>
    <p>人工智能是计算机科学的一个重要分支...</p>
    
    <h2>1. 人工智能的定义</h2>
    <p>人工智能（Artificial Intelligence，简称AI）...</p>
    
    <h2>2. 发展历程</h2>
    <h3>2.1 早期发展</h3>
    <p>人工智能的概念最早可以追溯到...</p>
    
    <h3>2.2 现代AI</h3>
    <p>近年来，随着大数据和计算能力的提升...</p>
    
    <h2>3. 应用领域</h2>
    <p>人工智能在各个领域都有广泛应用...</p>
    """
    
    # 测试本地目录提取
    catalog = ai_proxy_service.extract_catalog_from_html(test_content)
    print("本地提取目录:")
    for item in catalog:
        print(f"  {'  ' * (item['level'] - 1)}{item['title']}")
