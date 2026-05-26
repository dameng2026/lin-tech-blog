"""
阅读时长计算工具
用于根据文章内容自动计算阅读时长
"""
import re
from typing import Optional

# 默认阅读速度（中文字符/分钟）
DEFAULT_READING_SPEED = 400  # 中等阅读速度

# 不同类型内容的阅读速度系数
READING_SPEED_FACTORS = {
    'normal': 1.0,      # 普通文本
    'code': 0.3,        # 代码块（阅读较慢）
    'list': 1.2,        # 列表（阅读较快）
    'quote': 0.9,       # 引用（阅读较慢）
}

def calculate_read_time(content: str, reading_speed: int = DEFAULT_READING_SPEED) -> int:
    """
    计算文章阅读时长（分钟）
    
    Args:
        content: 文章内容（HTML格式或纯文本）
        reading_speed: 阅读速度（字符/分钟），默认为400
    
    Returns:
        阅读时长（分钟），向上取整
    """
    if not content:
        return 0
    
    # 移除HTML标签，提取纯文本
    text = remove_html_tags(content)
    
    # 统计中文字符数
    chinese_chars = count_chinese_characters(text)
    
    # 统计英文字符数（单词数 * 平均单词长度）
    english_chars = count_english_characters(text)
    
    # 总字符数（中文 + 英文）
    total_chars = chinese_chars + english_chars
    
    if total_chars == 0:
        return 0
    
    # 计算阅读时长（分钟），向上取整
    read_time_minutes = (total_chars + reading_speed - 1) // reading_speed
    
    # 至少返回1分钟
    return max(1, read_time_minutes)

def remove_html_tags(content: str) -> str:
    """
    移除HTML标签，保留纯文本
    
    Args:
        content: HTML内容
    
    Returns:
        纯文本内容
    """
    # 移除HTML标签
    text = re.sub(r'<[^>]+>', ' ', content)
    
    # 移除多余的空白字符
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def count_chinese_characters(text: str) -> int:
    """
    统计中文字符数量
    
    Args:
        text: 纯文本内容
    
    Returns:
        中文字符数量
    """
    count = 0
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            count += 1
    return count

def count_english_characters(text: str) -> int:
    """
    统计英文内容的字符数（单词数 * 平均单词长度5）
    
    Args:
        text: 纯文本内容
    
    Returns:
        英文等效字符数
    """
    # 匹配英文单词
    words = re.findall(r'[a-zA-Z]+', text)
    
    # 平均每个英文单词按5个字符计算
    return len(words) * 5

def extract_content_features(content: str) -> dict:
    """
    提取文章内容特征用于更精确的阅读时间计算
    
    Args:
        content: 文章内容（HTML格式）
    
    Returns:
        内容特征字典
    """
    features = {
        'total_length': len(content),
        'html_tags': len(re.findall(r'<[^>]+>', content)),
        'code_blocks': len(re.findall(r'<code[^>]*>.*?</code>', content, re.DOTALL)),
        'lists': len(re.findall(r'<(ul|ol)[^>]*>', content)),
        'quotes': len(re.findall(r'<blockquote[^>]*>', content)),
        'images': len(re.findall(r'<img[^>]+>', content)),
    }
    
    return features

def calculate_read_time_with_features(content: str, reading_speed: int = DEFAULT_READING_SPEED) -> dict:
    """
    计算阅读时长并返回详细信息
    
    Args:
        content: 文章内容（HTML格式）
        reading_speed: 阅读速度（字符/分钟）
    
    Returns:
        包含阅读时长和内容特征的字典
    """
    features = extract_content_features(content)
    
    # 基础阅读时间
    base_time = calculate_read_time(content, reading_speed)
    
    # 根据内容特征调整阅读时间
    # 代码块增加阅读时间
    code_penalty = features['code_blocks'] * 2
    
    # 图片增加浏览时间（每张图片约10秒）
    image_penalty = (features['images'] * 10) // 60
    
    # 总阅读时间
    total_time = base_time + code_penalty + image_penalty
    
    return {
        'read_time_minutes': max(1, total_time),
        'base_time_minutes': base_time,
        'code_blocks': features['code_blocks'],
        'images': features['images'],
        'total_length': features['total_length'],
        'reading_speed': reading_speed,
    }

def format_read_time(minutes: int) -> str:
    """
    格式化阅读时长显示
    
    Args:
        minutes: 分钟数
    
    Returns:
        格式化的时间字符串
    """
    if minutes < 1:
        return '小于1分钟'
    elif minutes == 1:
        return '1分钟'
    elif minutes < 60:
        return f'{minutes}分钟'
    else:
        hours = minutes // 60
        remaining_minutes = minutes % 60
        if remaining_minutes == 0:
            return f'{hours}小时'
        else:
            return f'{hours}小时{remaining_minutes}分钟'

# 测试示例
if __name__ == '__main__':
    # 测试内容
    test_content = """
    <h1>深入理解人工智能</h1>
    <p>人工智能（Artificial Intelligence，简称AI）是计算机科学的一个分支，旨在研究、开发用于模拟、延伸和扩展人的智能的理论、方法、技术及应用系统。</p>
    <p>人工智能领域的研究包括机器人、语言识别、图像识别、自然语言处理和专家系统等。</p>
    <pre><code>def hello():
        print("Hello, AI!")</code></pre>
    <p>随着大数据和计算能力的提升，人工智能技术得到了飞速发展。</p>
    <img src="ai.jpg" />
    """
    
    # 计算阅读时间
    result = calculate_read_time_with_features(test_content)
    print(f"基础阅读时间: {result['base_time_minutes']}分钟")
    print(f"代码块数量: {result['code_blocks']}")
    print(f"图片数量: {result['images']}")
    print(f"总阅读时间: {result['read_time_minutes']}分钟")
    print(f"格式化显示: {format_read_time(result['read_time_minutes'])}")
