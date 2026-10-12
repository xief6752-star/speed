#!/usr/bin/env python3
"""
为所有 HTML 页面批量添加 GEO 地理位置标记
优化搜索引擎对中文用户的定位
"""
import os
import glob
import re

def add_geo_tags(filepath):
    """在 <head> 中添加 GEO 标记"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查是否已经有 geo.region 标记
    if 'geo.region' in content:
        print(f"⏭️  跳过 {os.path.basename(filepath)} (已有 GEO 标记)")
        return False

    # GEO 标记内容
    geo_tags = '''  <!-- 地理位置优化 -->
  <meta name="geo.region" content="CN" />
  <meta name="geo.placename" content="China" />
  <meta name="language" content="zh-CN" />
  <link rel="alternate" hreflang="zh-CN" href="https://jichangspeed.com/" />
  <link rel="alternate" hreflang="zh-Hans" href="https://jichangspeed.com/" />
'''

    # 在 robots 标记后插入
    if '<meta name="robots"' in content:
        content = re.sub(
            r'(<meta name="robots"[^>]*>)',
            r'\1\n' + geo_tags,
            content,
            count=1
        )
    # 或在 viewport 标记后插入
    elif '<meta name="viewport"' in content:
        content = re.sub(
            r'(<meta name="viewport"[^>]*>)',
            r'\1\n' + geo_tags,
            content,
            count=1
        )
    # 或在 </head> 前插入
    else:
        content = content.replace('</head>', f'{geo_tags}\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ 已添加 GEO 标记: {os.path.basename(filepath)}")
    return True

def main():
    html_files = glob.glob('*.html')
    print(f"📊 找到 {len(html_files)} 个 HTML 文件\n")

    updated_count = 0
    for filepath in sorted(html_files):
        if add_geo_tags(filepath):
            updated_count += 1

    print(f"\n🎉 完成! 更新了 {updated_count}/{len(html_files)} 个文件")

if __name__ == '__main__':
    main()
