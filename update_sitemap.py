#!/usr/bin/env python3
"""
自动更新 sitemap.xml 中的 lastmod 时间戳
基于文件的实际修改时间
"""
import os
from datetime import datetime
import xml.etree.ElementTree as ET

def get_file_mtime(filepath):
    """获取文件修改时间"""
    return datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d')

def update_sitemap():
    """更新 sitemap.xml 中的所有 lastmod 时间"""
    sitemap_path = 'sitemap.xml'

    # 解析 sitemap.xml
    tree = ET.parse(sitemap_path)
    root = tree.getroot()

    # 命名空间
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    updated_count = 0

    # 遍历所有 URL 条目
    for url in root.findall('ns:url', ns):
        loc = url.find('ns:loc', ns)
        lastmod = url.find('ns:lastmod', ns)

        if loc is not None and lastmod is not None:
            url_path = loc.text.strip()

            # 提取文件名
            if url_path.endswith('.html'):
                filename = url_path.split('/')[-1]

                # 检查文件是否存在
                if os.path.exists(filename):
                    # 获取文件修改时间
                    mtime = get_file_mtime(filename)

                    # 更新 lastmod
                    if lastmod.text != mtime:
                        old_time = lastmod.text
                        lastmod.text = mtime
                        updated_count += 1
                        print(f"✅ {filename}: {old_time} → {mtime}")
                else:
                    print(f"⚠️  文件不存在: {filename}")

            # 处理主页
            elif url_path.endswith('jichangspeed.com/'):
                if os.path.exists('index.html'):
                    mtime = get_file_mtime('index.html')
                    if lastmod.text != mtime:
                        old_time = lastmod.text
                        lastmod.text = mtime
                        updated_count += 1
                        print(f"✅ index.html (主页): {old_time} → {mtime}")

    # 格式化输出 XML (带缩进)
    ET.indent(tree, space="  ")
    tree.write(sitemap_path, encoding='UTF-8', xml_declaration=True)

    print(f"\n🎉 Sitemap 更新完成!")
    print(f"📊 共更新 {updated_count} 个条目的时间戳")
    print(f"📅 当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == '__main__':
    print("🚀 开始更新 sitemap.xml...\n")
    update_sitemap()
