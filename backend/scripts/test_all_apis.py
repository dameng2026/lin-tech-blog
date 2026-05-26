"""
综合测试脚本 - 测试所有修复的 API
"""
import requests
import json

BASE_URL = "http://localhost:8000/api/v1"

def test_api(name, url, expected_fields=None):
    """测试单个 API"""
    try:
        response = requests.get(url)
        print(f"\n{'='*60}")
        print(f"测试: {name}")
        print(f"URL: {url}")
        print(f"状态码: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print(f"✓ 响应成功")
            print(f"  code: {data.get('code')}")
            print(f"  msg: {data.get('msg')}")

            if expected_fields and 'data' in data:
                if isinstance(data['data'], list):
                    print(f"  数据列表长度: {len(data['data'])}")
                    if len(data['data']) > 0:
                        print(f"  第一条数据: {json.dumps(data['data'][0], ensure_ascii=False, indent=2)}")
                elif isinstance(data['data'], dict):
                    print(f"  数据字段: {list(data['data'].keys())}")
            return True
        else:
            print(f"✗ 请求失败: {response.status_code}")
            print(f"  响应: {response.text[:200]}")
            return False
    except Exception as e:
        print(f"✗ 测试异常: {str(e)}")
        return False

def main():
    print("\n" + "="*60)
    print("开始测试所有 API")
    print("="*60)

    results = []

    # 测试分类 API
    results.append(("获取分类列表", test_api("获取分类列表", f"{BASE_URL}/taxonomy/categories")))

    # 测试标签 API
    results.append(("获取标签列表", test_api("获取标签列表", f"{BASE_URL}/taxonomy/tags")))

    # 测试文章 API
    results.append(("获取文章列表", test_api("获取文章列表", f"{BASE_URL}/articles/")))

    # 测试 Dashboard API
    results.append(("获取仪表盘摘要", test_api("获取仪表盘摘要", f"{BASE_URL}/dashboard/summary")))

    # 统计结果
    print("\n" + "="*60)
    print("测试结果汇总")
    print("="*60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✓ 通过" if result else "✗ 失败"
        print(f"{status} - {name}")

    print(f"\n总计: {passed}/{total} 测试通过")

    if passed == total:
        print("\n🎉 所有测试通过！")
    else:
        print(f"\n⚠️  有 {total - passed} 个测试失败")

if __name__ == "__main__":
    main()
