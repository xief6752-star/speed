#!/usr/bin/env python3
"""
技术 SEO 检查工具
检查死链、重复内容、缺失标签等问题
"""
import os
import glob
import re
from typing import List, Dict, Set
from collections import defaultdict

class SEOChecker:
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.stats = defaultdict(int)
        self.all_urls = set()

    def check_file(self, filepath: str) -> Dict:
        """检查单个文件的 SEO 问题"""
        filename = os.path.basename(filepath)

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        file_issues = []

        # 1. 检查必要的 meta 标签
        if '<title>' not in content:
            file_issues.append("❌ 缺少 <title> 标签")

        if 'name="description"' not in content:
            file_issues.append("❌ 缺少 meta description")

        if 'name="keywords"' not in content:
            file_issues.append("⚠️  缺少 meta keywords")

        # 2. 检查 canonical 标签
        if 'rel="canonical"' not in content:
            file_issues.append("⚠️  缺少 canonical 标签")

        # 3. 检查标题长度
        title_match = re.search(r'<title>([^<]+)</title>', content)
        if title_match:
            title = title_match.group(1)
            if len(title) > 60:
                file_issues.append(f"⚠️  标题过长 ({len(title)} 字符,建议 < 60)")
            elif len(title) < 30:
                file_issues.append(f"⚠️  标题过短 ({len(title)} 字符,建议 30-60)")

        # 4. 检查 description 长度
        desc_match = re.search(r'name="description" content="([^"]*)"', content)
        if desc_match:
            description = desc_match.group(1)
            if len(description) > 160:
                file_issues.append(f"⚠️  描述过长 ({len(description)} 字符,建议 < 160)")
            elif len(description) < 50:
                file_issues.append(f"⚠️  描述过短 ({len(description)} 字符,建议 50-160)")

        # 5. 检查图片 alt 属性
        img_tags = re.findall(r'<img[^>]*>', content)
        imgs_without_alt = [img for img in img_tags if 'alt=' not in img]
        if imgs_without_alt:
            file_issues.append(f"⚠️  {len(imgs_without_alt)} 个图片缺少 alt 属性")

        # 6. 检查内部链接
        links = re.findall(r'href="([^"]*\.html)"', content)
        for link in links:
            # 移除锚点
            link_clean = link.split('#')[0]
            if link_clean and not link_clean.startswith('http'):
                self.all_urls.add(link_clean)

        # 7. 检查 h1 标签
        h1_count = len(re.findall(r'<h1[^>]*>.*?</h1>', content, re.DOTALL))
        if h1_count == 0:
            file_issues.append("⚠️  缺少 h1 标签")
        elif h1_count > 1:
            file_issues.append(f"⚠️  有 {h1_count} 个 h1 标签 (建议只有 1 个)")

        # 8. 检查 Open Graph 标签
        if 'property="og:title"' not in content:
            file_issues.append("⚠️  缺少 Open Graph 标签")

        return {
            'filename': filename,
            'issues': file_issues,
            'title_length': len(title) if title_match else 0,
            'desc_length': len(description) if desc_match else 0,
            'h1_count': h1_count,
            'img_count': len(img_tags),
            'imgs_without_alt': len(imgs_without_alt),
        }

    def check_dead_links(self):
        """检查死链"""
        print("\n🔍 检查死链...")

        html_files = set(os.path.basename(f) for f in glob.glob('*.html'))
        dead_links = self.all_urls - html_files

        if dead_links:
            print(f"\n❌ 发现 {len(dead_links)} 个死链:")
            for link in sorted(dead_links):
                print(f"   • {link}")
        else:
            print("✅ 未发现死链")

    def check_duplicate_titles(self, results: List[Dict]):
        """检查重复标题"""
        print("\n🔍 检查重复标题...")

        titles = defaultdict(list)
        for result in results:
            with open(result['filename'], 'r', encoding='utf-8') as f:
                content = f.read()
                title_match = re.search(r'<title>([^<]+)</title>', content)
                if title_match:
                    titles[title_match.group(1)].append(result['filename'])

        duplicates = {title: files for title, files in titles.items() if len(files) > 1}

        if duplicates:
            print(f"\n⚠️  发现 {len(duplicates)} 组重复标题:")
            for title, files in list(duplicates.items())[:3]:
                print(f"   • \"{title[:50]}...\"")
                for f in files[:3]:
                    print(f"     - {f}")
        else:
            print("✅ 未发现重复标题")

    def generate_report(self, results: List[Dict]):
        """生成报告"""
        print("\n" + "="*60)
        print("📊 技术 SEO 检查报告")
        print("="*60)

        # 统计
        total_files = len(results)
        files_with_issues = sum(1 for r in results if r['issues'])
        total_issues = sum(len(r['issues']) for r in results)

        print(f"\n检查文件数: {total_files}")
        print(f"有问题的文件: {files_with_issues}")
        print(f"总问题数: {total_issues}")

        # 分类统计
        issue_types = defaultdict(int)
        for result in results:
            for issue in result['issues']:
                if '缺少' in issue:
                    issue_types['缺少必要标签'] += 1
                elif '过长' in issue or '过短' in issue:
                    issue_types['标题/描述长度'] += 1
                elif 'alt' in issue:
                    issue_types['图片 alt 属性'] += 1
                elif 'h1' in issue:
                    issue_types['h1 标签问题'] += 1

        if issue_types:
            print("\n问题分类:")
            for issue_type, count in sorted(issue_types.items(), key=lambda x: -x[1]):
                print(f"   • {issue_type}: {count} 处")

        # 显示最严重的问题文件
        serious_files = [r for r in results if len(r['issues']) >= 3]
        if serious_files:
            print(f"\n🔴 需要优先处理的文件 ({len(serious_files)} 个):")
            for result in sorted(serious_files, key=lambda x: -len(x['issues']))[:10]:
                print(f"\n   {result['filename']} ({len(result['issues'])} 个问题)")
                for issue in result['issues'][:3]:
                    print(f"      {issue}")

        # 检查死链
        self.check_dead_links()

        # 检查重复标题
        self.check_duplicate_titles(results)

        print("\n" + "="*60)
        print("✅ 检查完成!")
        print("="*60)

def main():
    print("🚀 技术 SEO 检查工具\n")

    checker = SEOChecker()

    # 获取所有 HTML 文件
    html_files = glob.glob('*.html')
    print(f"📊 检查 {len(html_files)} 个 HTML 文件...\n")

    results = []
    for filepath in sorted(html_files):
        result = checker.check_file(filepath)
        results.append(result)

        # 只显示有问题的文件
        if result['issues']:
            print(f"⚠️  {result['filename']}")
            for issue in result['issues']:
                print(f"   {issue}")

    # 生成完整报告
    checker.generate_report(results)

    print("\n💡 建议:")
    print("   1. 优先修复缺少必要标签的页面")
    print("   2. 调整标题和描述长度到推荐范围")
    print("   3. 为所有图片添加 alt 属性")
    print("   4. 修复死链")
    print("   5. 确保每个页面有且只有一个 h1 标签")

if __name__ == '__main__':
    main()
