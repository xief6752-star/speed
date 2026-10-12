#!/usr/bin/env python3
"""
IndexNow 自动提交脚本
在内容更新后自动通知搜索引擎
支持 Bing、Yandex 等搜索引擎的快速收录
"""
import json
import requests
from datetime import datetime
import glob

def get_indexnow_key():
    """读取 IndexNow 验证密钥"""
    try:
        with open('314aad3b40e9457c88d8eec5994eef2e.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("❌ 未找到 IndexNow 密钥文件")
        return None

def submit_to_indexnow(urls, key):
    """提交 URL 列表到 IndexNow API"""

    payload = {
        "host": "jichangspeed.com",
        "key": key,
        "keyLocation": "https://jichangspeed.com/314aad3b40e9457c88d8eec5994eef2e.txt",
        "urlList": urls
    }

    # IndexNow API 端点
    api_url = "https://api.indexnow.org/indexnow"

    try:
        response = requests.post(
            api_url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        if response.status_code == 200:
            print(f"✅ 成功提交 {len(urls)} 个 URL 到 IndexNow")
            return True
        elif response.status_code == 202:
            print(f"✅ URL 已接受处理: {len(urls)} 个")
            return True
        else:
            print(f"⚠️  提交返回状态码: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"❌ 提交失败: {e}")
        return False

def load_recent_updates():
    """从 indexnow-payload.json 加载最近更新的页面"""
    try:
        with open('indexnow-payload.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('urlList', [])
    except FileNotFoundError:
        print("⚠️  未找到 indexnow-payload.json，将提交所有主要页面")
        return []

def get_all_important_pages():
    """获取所有重要页面的 URL"""
    base_url = "https://jichangspeed.com/"

    # 主要页面
    important_pages = [
        "",  # 主页
        "compare.html",
        "faq.html",
        "status.html",
        "toolbox.html",
        "coupon.html",
        "rank-stable.html",
        "rank-value.html",
    ]

    # 机场评测页面
    review_files = glob.glob('*-jichang-pingce.html')

    # 教程页面
    tutorial_files = glob.glob('tutorial-*.html')

    # 博客页面
    blog_files = glob.glob('blog-*.html')

    # 合并所有页面
    all_files = important_pages + review_files + tutorial_files + blog_files

    # 转换为完整 URL
    urls = [base_url + (f if f else "") for f in all_files]

    return urls

def main():
    print("🚀 IndexNow 自动提交工具\n")

    # 获取密钥
    key = get_indexnow_key()
    if not key:
        return

    print(f"🔑 密钥: {key}\n")

    # 尝试加载最近更新的页面
    recent_urls = load_recent_updates()

    if recent_urls:
        print(f"📄 从 indexnow-payload.json 加载了 {len(recent_urls)} 个 URL")
        urls_to_submit = recent_urls
    else:
        # 如果没有最近更新记录，提交所有重要页面
        print("📄 准备提交所有重要页面")
        urls_to_submit = get_all_important_pages()

    # IndexNow 建议每次提交不超过 10000 个 URL
    # 分批提交（每批 100 个）
    batch_size = 100
    total_submitted = 0

    for i in range(0, len(urls_to_submit), batch_size):
        batch = urls_to_submit[i:i + batch_size]
        print(f"\n📤 提交批次 {i//batch_size + 1} ({len(batch)} 个 URL)...")

        if submit_to_indexnow(batch, key):
            total_submitted += len(batch)

    print(f"\n🎉 提交完成!")
    print(f"📊 总计: {total_submitted}/{len(urls_to_submit)} 个 URL")
    print(f"📅 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 保存提交记录
    with open('indexnow-last-submit.json', 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'count': total_submitted,
            'urls': urls_to_submit[:10]  # 只保存前 10 个作为示例
        }, f, ensure_ascii=False, indent=2)

    print("✅ 提交记录已保存到 indexnow-last-submit.json")

if __name__ == '__main__':
    main()
