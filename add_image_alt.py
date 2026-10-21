#!/usr/bin/env python3
"""
图片 alt 属性优化脚本
为所有缺失 alt 属性的图片添加描述性文本
提升 SEO 和无障碍访问
"""
import os
import glob
import re
from typing import List, Tuple

def generate_alt_text(img_tag: str, context: str, filename: str) -> str:
    """根据上下文生成 alt 文本"""

    # 从 src 中提取图片信息
    src_match = re.search(r'src="([^"]*)"', img_tag)
    src = src_match.group(1) if src_match else ''

    # 根据图片文件名生成描述
    if 'logo' in src.lower() or 'logo' in img_tag.lower():
        return 'SpeedRank 机场测速排名 Logo'
    elif 'icon' in src.lower():
        return '图标'
    elif 'network' in src.lower() or 'img_network' in src:
        return '机场网络架构示意图'
    elif 'app' in src.lower() or 'img_app' in src:
        return '代理客户端应用截图'
    elif 'guide' in src.lower() or 'img_guide' in src:
        return '机场使用教程配置指南'
    elif 'steps' in src.lower() or 'img_steps' in src:
        return '机场配置步骤图解'
    elif 'screenshot' in src.lower():
        return '软件配置截图'
    elif 'qr' in src.lower() or 'qrcode' in src.lower():
        return '机场注册二维码'

    # 根据页面类型生成默认描述
    if 'tutorial' in filename:
        return '客户端配置教程截图'
    elif 'pingce' in filename or 'airport' in filename:
        return '机场测速数据图表'
    elif 'blog' in filename:
        return '文章配图'
    elif 'tool' in filename:
        return '工具使用示例'

    return '相关图片'

def add_alt_to_images(filepath: str) -> Tuple[int, int]:
    """为文件中的图片添加 alt 属性"""
    filename = os.path.basename(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 查找所有 img 标签
    img_pattern = r'<img[^>]*>'
    img_tags = re.findall(img_pattern, content)

    if not img_tags:
        return 0, 0

    total_imgs = len(img_tags)
    fixed_count = 0

    # 为每个缺少 alt 的图片添加
    for img_tag in img_tags:
        if 'alt=' in img_tag:
            continue

        # 生成 alt 文本
        alt_text = generate_alt_text(img_tag, content, filename)

        # 在 > 前插入 alt 属性
        new_img_tag = img_tag.replace('>', f' alt="{alt_text}">', 1)
        content = content.replace(img_tag, new_img_tag, 1)
        fixed_count += 1

    if fixed_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return total_imgs, fixed_count

def main():
    print("🚀 图片 alt 属性优化\n")

    # 获取所有 HTML 文件
    html_files = glob.glob('*.html')
    print(f"📊 检查 {len(html_files)} 个 HTML 文件...\n")

    total_images = 0
    total_fixed = 0
    files_with_fixes = 0

    for filepath in sorted(html_files):
        imgs, fixed = add_alt_to_images(filepath)
        total_images += imgs

        if fixed > 0:
            total_fixed += fixed
            files_with_fixes += 1
            print(f"✅ {os.path.basename(filepath)}: 为 {fixed}/{imgs} 张图片添加 alt")

    print("\n" + "="*60)
    print("📊 优化完成")
    print("="*60)
    print(f"   • 检查文件: {len(html_files)} 个")
    print(f"   • 图片总数: {total_images} 张")
    print(f"   • 添加 alt: {total_fixed} 张")
    print(f"   • 涉及文件: {files_with_fixes} 个")

    print("\n📈 SEO 优化效果:")
    print("   • 提升图片搜索排名")
    print("   • 改善无障碍访问")
    print("   • 增强页面 SEO 得分")
    print("   • 图片加载失败时显示描述")

if __name__ == '__main__':
    main()
