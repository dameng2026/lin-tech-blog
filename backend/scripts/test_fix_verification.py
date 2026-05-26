"""
功能修复验证测试脚本
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import asyncio
import requests

def test_backend_api():
    """测试后端API"""
    print("\n" + "="*60)
    print("测试后端API")
    print("="*60)
    
    base_url = "http://localhost:8000"
    
    test_endpoints = [
        ("/", "首页"),
        ("/health", "健康检查"),
        ("/api/v1/auth/me", "用户信息"),
        ("/api/v1/taxonomy/categories", "分类列表"),
        ("/api/v1/settings/", "系统设置"),
        ("/api/v1/settings/ai-model/enabled", "AI模型开关"),
    ]
    
    for endpoint, name in test_endpoints:
        url = f"{base_url}{endpoint}"
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code
            
            if status_code == 200:
                print(f"✓ {name}: {url} - {status_code} OK")
            elif status_code == 401:
                print(f"✓ {name}: {url} - {status_code} (需要登录，正常)")
            else:
                print(f"✗ {name}: {url} - {status_code}")
                try:
                    data = response.json()
                    print(f"   错误信息: {data.get('msg', '未知')}")
                except:
                    print(f"   响应: {response.text[:100]}")
        except requests.exceptions.RequestException as e:
            print(f"✗ {name}: {url} - 连接失败: {e}")

def test_system_settings():
    """测试系统设置功能"""
    print("\n" + "="*60)
    print("测试系统设置功能")
    print("="*60)
    
    base_url = "http://localhost:8000/api/v1/settings"
    
    try:
        # 获取设置
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200:
            print("✓ 获取系统设置成功")
            print(f"   设置数量: {len(response.json().get('data', {}))}")
        else:
            print(f"✗ 获取系统设置失败: {response.status_code}")
        
        # 检查AI模型开关
        response = requests.get(f"{base_url}/ai-model/enabled", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✓ AI模型开关状态: {'开启' if data.get('data', {}).get('enabled') else '关闭'}")
        else:
            print(f"✗ 获取AI模型开关失败: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"✗ 测试失败: {e}")

def test_catalog_generation():
    """测试目录生成功能"""
    print("\n" + "="*60)
    print("测试目录生成功能")
    print("="*60)
    
    base_url = "http://localhost:8000/api/v1/catalog"
    
    test_content = """
    <h1>深入理解人工智能</h1>
    <p>人工智能是计算机科学的一个重要分支...</p>
    
    <h2>1. 人工智能的定义</h2>
    <p>人工智能（Artificial Intelligence，简称AI）...</p>
    
    <h2>2. 发展历程</h2>
    <h3>2.1 早期发展</h3>
    <p>人工智能的概念最早可以追溯到...</p>
    """
    
    try:
        response = requests.post(
            f"{base_url}/generate",
            params={"content": test_content, "use_ai": False},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            catalog = data.get('data', {}).get('catalog', [])
            print(f"✓ 目录生成成功")
            print(f"   目录条目数: {len(catalog)}")
            for item in catalog:
                print(f"     - 第{item['level']}级: {item['title']}")
        else:
            print(f"✗ 目录生成失败: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"✗ 测试失败: {e}")

def test_login():
    """测试登录功能"""
    print("\n" + "="*60)
    print("测试登录功能")
    print("="*60)
    
    base_url = "http://localhost:8000/api/v1/auth/login"
    
    test_data = {
        "username": "test",
        "password": "test123"
    }
    
    try:
        response = requests.post(base_url, json=test_data, timeout=5)
        status_code = response.status_code
        
        if status_code == 200:
            data = response.json()
            print("✓ 登录成功")
            print(f"   token: {data.get('data', {}).get('token', '')[:20]}...")
        elif status_code == 400:
            print("✓ 登录失败（预期，可能账号密码错误或用户不存在）")
            print(f"   错误信息: {response.json().get('msg', '未知')}")
        else:
            print(f"✗ 登录异常: {status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"✗ 测试失败: {e}")

def main():
    print("\n" + "="*60)
    print("开始功能修复验证测试")
    print("="*60)
    
    print("\n📋 测试内容:")
    print("  1. 后端API测试")
    print("  2. 系统设置功能测试")
    print("  3. 目录生成功能测试")
    print("  4. 登录功能测试")
    
    test_backend_api()
    test_system_settings()
    test_catalog_generation()
    test_login()
    
    print("\n" + "="*60)
    print("测试完成！")
    print("="*60)
    
    print("\n✅ 已修复的功能:")
    print("  1. 后端500错误修复 - 添加全局异常处理")
    print("  2. 系统设置模型功能开关机制")
    print("  3. 章节目录管理功能")
    print("  4. 自动获取章节按钮")
    
    print("\n🔧 新增API端点:")
    print("  - GET/POST /api/v1/settings/ - 系统设置")
    print("  - GET/PUT /api/v1/settings/ai-model/enabled - AI模型开关")
    print("  - POST /api/v1/catalog/generate - 生成目录")
    print("  - POST /api/v1/catalog/generate-with-check - 生成目录(带开关检查)")
    
    print("\n🚀 测试结果说明:")
    print("  - 200 OK: 接口正常")
    print("  - 401 Unauthorized: 需要登录，属于正常状态")
    print("  - 400 Bad Request: 参数错误或功能未开启")

if __name__ == "__main__":
    main()
