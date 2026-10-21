#!/usr/bin/env python3
"""
技术问题修复脚本
修复 SEO 检查发现的问题:
1. 修复多个 h1 标签
2. 调整标题长度
3. 添加缺失的标签
"""
import os
import re
from typing import Dict, List

def fix_multiple_h1_tags(filepath: str) -> bool:
    """修复多个 h1 标签问题"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 查找所有 h1 标签
    h1_pattern = r'<h1[^>]*>(.*?)</h1>'
    h1_matches = list(re.finditer(h1_pattern, content, re.DOTALL))

    if len(h1_matches) <= 1:
        return False

    # 保留第一个 h1,其他转为 h2
    for i, match in enumerate(h1_matches):
        if i == 0:
            continue  # 保留第一个

        # 将后续的 h1 改为 h2
        old_tag = match.group(0)
        new_tag = old_tag.replace('<h1', '<h2', 1).replace('</h1>', '</h2>', 1)
        content = content.replace(old_tag, new_tag, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def fix_title_length(filepath: str) -> bool:
    """调整标题长度"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r'<title>([^<]+)</title>', content)
    if not title_match:
        return False

    title = title_match.group(1)
    filename = os.path.basename(filepath)

    # 如果标题太短,添加更多描述
    if len(title) < 30:
        new_title = None

        if filename == 'faq.html':
            new_title = '机场常见问题解答 · SpeedRank - 新手必看FAQ'
        elif filename == 'toolbox.html':
            new_title = '工具箱 · SpeedRank - IP检测/DNS泄漏/流媒体测试'
        elif filename == 'jichang-changjian-wenti.html':
            new_title = '机场使用常见问题 · SpeedRank - 速度慢/无法连接/节点选择'
        elif filename == 'jichang-shime.html':
            new_title = '什么是机场？ · SpeedRank - 机场科普完整指南'

        if new_title:
            content = re.sub(
                r'<title>[^<]+</title>',
                f'<title>{new_title}</title>',
                content,
                count=1
            )

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            return True

    return False

def add_missing_tags(filepath: str) -> bool:
    """为 check_h1.html 添加缺失的标签"""
    if 'check_h1' not in filepath:
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 添加 meta description
    if 'name="description"' not in content:
        desc_tag = '<meta name="description" content="H1 标签检查工具 - 用于检测页面 H1 标签数量和内容">'
        content = content.replace('</head>', f'  {desc_tag}\n</head>')
        modified = True

    # 添加 meta keywords
    if 'name="keywords"' not in content:
        keywords_tag = '<meta name="keywords" content="H1检查,SEO工具,标签检测">'
        content = content.replace('</head>', f'  {keywords_tag}\n</head>')
        modified = True

    # 添加 canonical
    if 'rel="canonical"' not in content:
        canonical_tag = '<link rel="canonical" href="https://jichangspeed.com/check_h1.html">'
        content = content.replace('</head>', f'  {canonical_tag}\n</head>')
        modified = True

    # 调整标题
    content = re.sub(
        r'<title>[^<]*</title>',
        '<title>H1 标签检查工具 · SpeedRank - SEO 诊断工具</title>',
        content,
        count=1
    )
    modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return modified

def main():
    print("🚀 技术问题修复工具\n")

    fixes = {
        'multiple_h1': 0,
        'title_length': 0,
        'missing_tags': 0
    }

    # 需要修复多个 h1 的文件
    h1_files = ['baoyun-jichang-pingce.html', 'kunpeng-jichang-pingce.html']

    print("1️⃣ 修复多个 h1 标签问题...")
    for filename in h1_files:
        if os.path.exists(filename):
            if fix_multiple_h1_tags(filename):
                print(f"   ✅ {filename}: 将多余的 h1 改为 h2")
                fixes['multiple_h1'] += 1

    # 修复标题长度
    print("\n2️⃣ 调整标题长度...")
    title_files = [
        'faq.html',
        'toolbox.html',
        'jichang-changjian-wenti.html',
        'jichang-shime.html'
    ]

    for filename in title_files:
        if os.path.exists(filename):
            if fix_title_length(filename):
                print(f"   ✅ {filename}: 优化标题长度")
                fixes['title_length'] += 1

    # 修复缺失标签
    print("\n3️⃣ 添加缺失的标签...")
    if os.path.exists('check_h1.html'):
        if add_missing_tags('check_h1.html'):
            print(f"   ✅ check_h1.html: 添加缺失的 meta 标签")
            fixes['missing_tags'] += 1

    # 总结
    print("\n" + "="*60)
    print("📊 修复完成")
    print("="*60)
    print(f"   • 修复多个 h1: {fixes['multiple_h1']} 个文件")
    print(f"   • 优化标题长度: {fixes['title_length']} 个文件")
    print(f"   • 添加缺失标签: {fixes['missing_tags']} 个文件")
    print(f"\n✅ 总计修复: {sum(fixes.values())} 个问题")

    print("\n💡 剩余问题:")
    print("   • 死链需要手动处理或创建月度报告页面")
    print("   • airport.html 和 tutorial.html 的 title 标签已存在,无需修复")

if __name__ == '__main__':
    main()
