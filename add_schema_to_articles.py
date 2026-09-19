#!/usr/bin/env python3
"""
为比较和博客页面批量添加 Article Schema.org 结构化数据
"""

import re
from datetime import datetime

articles_data = {
    'compare.html': {
        'headline': '2026机场测速对比：60+机场实测排名',
        'description': '基于真实测速数据的机场对比排名，覆盖速度、延迟、稳定性、节点数量等核心指标，帮助你选择最适合的机场服务。',
        'datePublished': '2026-09-01',
        'dateModified': datetime.now().strftime('%Y-%m-%d')
    },
    'faq.html': {
        'headline': '机场常见问题解答：选购指南与使用技巧',
        'description': '涵盖机场选择、订阅购买、客户端配置、节点切换、速度优化等常见问题的详细解答，新手必读。',
        'datePublished': '2026-08-15',
        'dateModified': datetime.now().strftime('%Y-%m-%d')
    },
    'status.html': {
        'headline': '机场实时状态监控：稳定性与可用性追踪',
        'description': '实时监控60+机场的服务状态、节点可用性、速度波动，及时发现和报告机场故障与维护信息。',
        'datePublished': '2026-08-20',
        'dateModified': datetime.now().strftime('%Y-%m-%d')
    },
    'tutorial.html': {
        'headline': '机场配置教程大全：iOS/Android/Windows/macOS完整指南',
        'description': '全平台机场客户端配置教程，包括Clash、Shadowrocket、v2rayN等主流客户端的下载、安装、订阅导入与使用技巧。',
        'datePublished': '2026-08-10',
        'dateModified': datetime.now().strftime('%Y-%m-%d')
    }
}

def generate_article_schema(data):
    """生成 Article Schema.org JSON-LD"""
    schema = f'''
  <!-- Schema.org 结构化数据 -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{data['headline']}",
    "description": "{data['description']}",
    "datePublished": "{data['datePublished']}",
    "dateModified": "{data['dateModified']}",
    "author": {{
      "@type": "Organization",
      "name": "SpeedRank"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "SpeedRank",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://jichangspeed.com/img_network.jpg"
      }}
    }}
  }}
  </script>
'''
    return schema

def add_article_schema(filename):
    """为文章页面添加 Article Schema"""
    if filename not in articles_data:
        print(f"⊙ {filename}: 无数据配置，跳过")
        return False

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否已经有 Article Schema（但允许有其他类型的 schema）
        if '"@type": "Article"' in content:
            print(f"✓ {filename}: 已包含 Article Schema，跳过")
            return False

        data = articles_data[filename]
        schema = generate_article_schema(data)

        # 在 canonical 标签后插入
        pattern = re.compile(r'(<link rel="canonical"[^>]*>)\n')
        new_content = pattern.sub(r'\1\n' + schema + '\n', content)

        if new_content == content:
            print(f"✗ {filename}: 未找到插入位置")
            return False

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✓ {filename}: 成功添加 Article Schema")
        return True

    except Exception as e:
        print(f"✗ {filename}: 处理失败 - {e}")
        return False

def main():
    print("=== 批量添加 Article Schema.org 结构化数据 ===\n")

    success_count = 0
    for filename in articles_data.keys():
        if add_article_schema(filename):
            success_count += 1

    print(f"\n总结：成功添加 {success_count}/{len(articles_data)} 个页面的结构化数据")

if __name__ == '__main__':
    main()
