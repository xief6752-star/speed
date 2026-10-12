#!/usr/bin/env python3
"""
为所有 HTML 页面批量添加性能优化标记
包括: DNS 预解析、预连接、移动端优化等
"""
import os
import glob
import re

def add_performance_tags(filepath):
    """在 <head> 中添加性能优化标记"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查是否已经有性能优化标记
    if 'dns-prefetch' in content or 'mobile-web-app-capable' in content:
        print(f"⏭️  跳过 {os.path.basename(filepath)} (已有性能标记)")
        return False

    # 性能优化标记
    performance_tags = '''  <!-- 性能优化 -->
  <link rel="dns-prefetch" href="//jichangspeed.com">
  <link rel="preconnect" href="https://jichangspeed.com">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

  <!-- 移动端优化 -->
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="SpeedRank">
  <meta name="theme-color" content="#0f172a">
'''

    # 在 canonical 或 viewport 标记后插入
    if '<link rel="canonical"' in content:
        content = re.sub(
            r'(<link rel="canonical"[^>]*>)',
            r'\1\n' + performance_tags,
            content,
            count=1
        )
    elif '<meta name="viewport"' in content:
        content = re.sub(
            r'(<meta name="viewport"[^>]*>)',
            r'\1\n' + performance_tags,
            content,
            count=1
        )
    else:
        # 在 </head> 前插入
        content = content.replace('</head>', f'{performance_tags}\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ 已添加性能标记: {os.path.basename(filepath)}")
    return True

def main():
    html_files = glob.glob('*.html')
    print(f"📊 找到 {len(html_files)} 个 HTML 文件\n")

    updated_count = 0
    for filepath in sorted(html_files):
        if add_performance_tags(filepath):
            updated_count += 1

    print(f"\n🎉 完成! 更新了 {updated_count}/{len(html_files)} 个文件")

if __name__ == '__main__':
    main()
