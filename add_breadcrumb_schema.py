#!/usr/bin/env python3
"""
结构化数据增强脚本 - 添加 BreadcrumbList 面包屑导航
提升搜索结果展示,增加富文本片段
"""
import os
import glob
import re
import json

def generate_breadcrumb_schema(page_type: str, page_title: str, page_url: str) -> str:
    """生成面包屑导航 Schema"""

    # 基础面包屑
    breadcrumb_items = [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "首页",
            "item": "https://jichangspeed.com/"
        }
    ]

    # 根据页面类型添加层级
    if 'pingce' in page_type or 'airport' in page_type:
        breadcrumb_items.append({
            "@type": "ListItem",
            "position": 2,
            "name": "机场评测",
            "item": "https://jichangspeed.com/#reviews"
        })
        breadcrumb_items.append({
            "@type": "ListItem",
            "position": 3,
            "name": page_title,
            "item": f"https://jichangspeed.com/{page_url}"
        })
    elif 'tutorial' in page_type:
        breadcrumb_items.append({
            "@type": "ListItem",
            "position": 2,
            "name": "使用教程",
            "item": "https://jichangspeed.com/tutorial.html"
        })
        breadcrumb_items.append({
            "@type": "ListItem",
            "position": 3,
            "name": page_title,
            "item": f"https://jichangspeed.com/{page_url}"
        })
    elif 'blog' in page_type or 'jichang-' in page_type:
        breadcrumb_items.append({
            "@type": "ListItem",
            "position": 2,
            "name": "机场科普",
            "item": "https://jichangspeed.com/#articles"
        })
        breadcrumb_items.append({
            "@type": "ListItem",
            "position": 3,
            "name": page_title,
            "item": f"https://jichangspeed.com/{page_url}"
        })
    elif 'tool' in page_type:
        breadcrumb_items.append({
            "@type": "ListItem",
            "position": 2,
            "name": "工具箱",
            "item": "https://jichangspeed.com/toolbox.html"
        })
        breadcrumb_items.append({
            "@type": "ListItem",
            "position": 3,
            "name": page_title,
            "item": f"https://jichangspeed.com/{page_url}"
        })

    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": breadcrumb_items
    }

    return json.dumps(schema, ensure_ascii=False, indent=2)

def extract_title(content: str) -> str:
    """从 HTML 中提取标题"""
    title_match = re.search(r'<title>([^<]+)</title>', content)
    if title_match:
        title = title_match.group(1)
        # 移除 "· SpeedRank" 等后缀
        title = re.sub(r'\s*[·•]\s*SpeedRank.*$', '', title)
        return title.strip()
    return "SpeedRank"

def add_breadcrumb_to_file(filepath: str) -> bool:
    """为单个文件添加面包屑 Schema"""
    filename = os.path.basename(filepath)

    # 跳过不需要面包屑的页面
    if filename in ['index.html', 'compare.html', 'faq.html', 'status.html']:
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查是否已有面包屑
    if '"@type": "BreadcrumbList"' in content or '"@type":"BreadcrumbList"' in content:
        print(f"⏭️  跳过 {filename} (已有面包屑)")
        return False

    # 提取标题
    page_title = extract_title(content)

    # 判断页面类型
    page_type = filename

    # 生成面包屑 Schema
    breadcrumb_schema = generate_breadcrumb_schema(page_type, page_title, filename)

    # 构建完整的 script 标签
    breadcrumb_script = f'''  <script type="application/ld+json">
  {breadcrumb_schema}
  </script>
'''

    # 在最后一个 </script> 后插入
    last_script_pos = content.rfind('</script>')
    if last_script_pos != -1:
        # 找到该 </script> 之后的位置
        insert_pos = last_script_pos + len('</script>')
        content = content[:insert_pos] + '\n' + breadcrumb_script + content[insert_pos:]
    else:
        # 如果没有 script 标签,在 </head> 前插入
        content = content.replace('</head>', breadcrumb_script + '\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ {filename}: 添加面包屑导航")
    return True

def main():
    print("🚀 结构化数据增强 - 添加面包屑导航\n")

    # 获取所有 HTML 文件(排除 index 等特殊页面)
    html_files = [f for f in glob.glob('*.html')
                  if f not in ['index.html', 'compare.html', 'faq.html', 'status.html', 'check_h1.html']]

    print(f"📊 找到 {len(html_files)} 个页面\n")

    updated_count = 0
    for filepath in sorted(html_files):
        if add_breadcrumb_to_file(filepath):
            updated_count += 1

    print(f"\n🎉 完成! 为 {updated_count} 个页面添加了面包屑导航")
    print(f"\n📈 SEO 优化效果:")
    print(f"   • 搜索结果显示完整导航路径")
    print(f"   • 提升页面层级结构理解")
    print(f"   • 增加点击率 (CTR)")
    print(f"   • 改善用户体验")

if __name__ == '__main__':
    main()
