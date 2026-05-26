"""
分类管理功能测试脚本
"""
import requests
import json

BASE_URL = "http://localhost:8000/api/v1"

def test_api(name, method, url, data=None, expected_status=200):
    """测试单个 API"""
    try:
        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url, json=data)
        elif method == 'PUT':
            response = requests.put(url, json=data)
        elif method == 'PATCH':
            response = requests.patch(url)
        elif method == 'DELETE':
            response = requests.delete(url)

        print(f"\n{'='*60}")
        print(f"测试: {name}")
        print(f"方法: {method}")
        print(f"URL: {url}")
        print(f"状态码: {response.status_code}")

        if response.status_code == expected_status:
            print(f"✓ 响应成功")
            data = response.json()
            print(f"  code: {data.get('code')}")
            print(f"  msg: {data.get('msg')}")
            if 'data' in data and data['data']:
                print(f"  data: {json.dumps(data['data'], ensure_ascii=False, indent=2)}")
            return True, data
        else:
            print(f"✗ 请求失败: {response.status_code}")
            print(f"  响应: {response.text[:200]}")
            return False, None
    except Exception as e:
        print(f"✗ 测试异常: {str(e)}")
        return False, None

def main():
    print("\n" + "="*60)
    print("开始测试分类管理功能")
    print("="*60)

    results = []

    # 测试1: 获取所有分类（包括已暂停）
    success, data = test_api(
        "获取所有分类（包括已暂停）",
        'GET',
        f"{BASE_URL}/taxonomy/categories?include_inactive=true"
    )
    results.append(("获取所有分类", success))
    all_categories = data.get('data', []) if success else []
    print(f"\n当前共有 {len(all_categories)} 个分类")

    # 测试2: 获取激活的分类
    success, data = test_api(
        "获取激活的分类（默认）",
        'GET',
        f"{BASE_URL}/taxonomy/categories"
    )
    results.append(("获取激活分类", success))
    active_categories = data.get('data', []) if success else []

    # 测试3: 创建新分类
    test_category = {
        "name": f"测试分类{len(all_categories) + 1}",
        "description": "这是一个测试分类，用于功能验证"
    }
    success, created = test_api(
        "创建新分类",
        'POST',
        f"{BASE_URL}/taxonomy/categories",
        test_category
    )
    results.append(("创建分类", success))

    new_category_id = created.get('data', {}).get('id') if success else None

    # 测试4: 更新分类
    if new_category_id:
        update_data = {
            "name": f"测试分类{len(all_categories) + 1}（已修改）",
            "description": "分类介绍已修改，这是一个多行文本字段，支持最多500个字符的详细描述"
        }
        success, _ = test_api(
            "更新分类",
            'PUT',
            f"{BASE_URL}/taxonomy/categories/{new_category_id}",
            update_data
        )
        results.append(("更新分类", success))

        # 测试5: 暂停分类
        success, _ = test_api(
            "暂停分类",
            'PATCH',
            f"{BASE_URL}/taxonomy/categories/{new_category_id}/toggle-status"
        )
        results.append(("暂停分类", success))

        # 测试6: 验证分类已暂停（不包含在激活列表中）
        success, data = test_api(
            "验证分类已暂停",
            'GET',
            f"{BASE_URL}/taxonomy/categories"
        )
        results.append(("验证暂停", success))
        active_after_pause = data.get('data', []) if success else []
        paused_in_active = any(c.get('id') == new_category_id for c in active_after_pause)
        if not paused_in_active:
            print("  ✓ 暂停的分类未出现在激活列表中")

        # 测试7: 恢复分类
        success, _ = test_api(
            "恢复分类",
            'PATCH',
            f"{BASE_URL}/taxonomy/categories/{new_category_id}/toggle-status"
        )
        results.append(("恢复分类", success))

        # 测试8: 删除分类
        success, _ = test_api(
            "删除分类",
            'DELETE',
            f"{BASE_URL}/taxonomy/categories/{new_category_id}"
        )
        results.append(("删除分类", success))

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
