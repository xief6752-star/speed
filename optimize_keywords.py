#!/usr/bin/env python3
"""
机场推荐关键词 SEO 优化脚本
为不同类型的页面添加精准的关键词优化
"""
import os
import glob
import re

# 核心关键词库
KEYWORDS = {
    # 主页关键词
    'index': [
        '机场推荐2026', '机场排名', '机场测速', '最好用的机场',
        '高速机场推荐', '专线机场', '性价比机场', 'IEPL机场',
        '机场推荐知乎', '机场节点', '科学上网', '翻墙工具'
    ],

    # 机场评测页关键词
    'pingce': [
        '{name}机场', '{name}怎么样', '{name}评测', '{name}测速',
        '机场推荐', '机场评测', '专线机场', 'IEPL机场',
        '高速机场', '稳定机场', '机场节点', '机场优惠码'
    ],

    # 教程页关键词
    'tutorial': [
        'Clash教程', 'V2Ray教程', 'Shadowrocket教程',
        '机场使用教程', '科学上网教程', '翻墙软件',
        '机场订阅', '节点配置', '代理设置'
    ],

    # 博客科普页关键词
    'blog': [
        '机场科普', '机场知识', 'IEPL vs IPLC', '机场选择',
        '机场跑路', '机场防坑', '机场推荐', '科学上网'
    ],

    # 工具页关键词
    'tool': [
        'IP检测', 'DNS泄漏', '流媒体解锁', '机场测速',
        '节点测试', '代理检测', '科学上网工具'
    ]
}

def get_page_type(filename):
    """判断页面类型"""
    if filename == 'index.html':
        return 'index'
    elif 'pingce' in filename or 'airport' in filename:
        return 'pingce'
    elif 'tutorial' in filename:
        return 'tutorial'
    elif 'blog' in filename or 'jichang-' in filename:
        return 'blog'
    elif 'tool-' in filename:
        return 'tool'
    return 'blog'  # 默认

def extract_airport_name(filename):
    """从文件名提取机场名称"""
    # 例如: yuntu-jichang-pingce.html -> 云图
    name_map = {
        'yuntu': '云图',
        'jisuyun': '极速云',
        'huanyuyun': '寰宇云',
        'shunyun': '瞬云',
        'shanhai': '山海',
        'nexitaly': 'Nexitaly',
        'kunpeng': '鲲鹏',
        'jiuyun': '玖云',
        'baoyun': '豹云',
        'cailuyun': '财路云',
        'jinyun': '锦云',
        'liyun': '鲤云',
        'miaomiaoyun': '秒秒云',
        'shanshuiyun': '山水云',
        'cloudflux': 'Cloudflux',
        'stargate': 'Stargate',
        'orbital': 'Orbital',
        'nimbus': 'Nimbus',
        'vortex': 'Vortex',
        'helios': 'Helios',
        'phantom': 'Phantom',
    }

    for key, name in name_map.items():
        if key in filename:
            return name
    return None

def generate_keywords(filename):
    """为页面生成关键词"""
    page_type = get_page_type(filename)
    keywords = KEYWORDS.get(page_type, KEYWORDS['blog']).copy()

    # 如果是机场评测页,添加机场名称相关关键词
    if page_type == 'pingce':
        airport_name = extract_airport_name(filename)
        if airport_name:
            keywords = [kw.format(name=airport_name) for kw in keywords]

    return ','.join(keywords)

def update_keywords_in_html(filepath):
    """更新 HTML 文件中的 keywords meta 标签"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    new_keywords = generate_keywords(filename)

    # 查找现有的 keywords meta 标签
    keywords_pattern = r'<meta name="keywords" content="[^"]*"'

    if re.search(keywords_pattern, content):
        # 更新现有的 keywords
        old_match = re.search(r'<meta name="keywords" content="([^"]*)"', content)
        old_keywords = old_match.group(1) if old_match else ''

        # 如果已经有类似的关键词,跳过
        if '机场推荐' in old_keywords and len(old_keywords) > 50:
            print(f"⏭️  跳过 {filename} (已有优化关键词)")
            return False

        content = re.sub(
            keywords_pattern,
            f'<meta name="keywords" content="{new_keywords}"',
            content,
            count=1
        )
    else:
        # 没有 keywords 标签,在 description 后添加
        description_pattern = r'(<meta name="description" content="[^"]*">)'
        if re.search(description_pattern, content):
            content = re.sub(
                description_pattern,
                r'\1\n  <meta name="keywords" content="' + new_keywords + '">',
                content,
                count=1
            )
        else:
            # 在 viewport 后添加
            viewport_pattern = r'(<meta name="viewport"[^>]*>)'
            content = re.sub(
                viewport_pattern,
                r'\1\n  <meta name="keywords" content="' + new_keywords + '">',
                content,
                count=1
            )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ {filename}: 更新关键词")
    return True

def main():
    html_files = glob.glob('*.html')
    print(f"🚀 机场推荐关键词 SEO 优化\n")
    print(f"📊 找到 {len(html_files)} 个 HTML 文件\n")

    updated_count = 0
    for filepath in sorted(html_files):
        if update_keywords_in_html(filepath):
            updated_count += 1

    print(f"\n🎉 完成! 更新了 {updated_count} 个文件的关键词")
    print(f"\n📈 关键词优化策略:")
    print(f"   • 主页: 聚焦'机场推荐2026'、'机场排名'等核心词")
    print(f"   • 评测页: 机场名+关键词组合")
    print(f"   • 教程页: 'Clash教程'、'机场使用'等长尾词")
    print(f"   • 科普页: '机场科普'、'IEPL'等知识类词")

if __name__ == '__main__':
    main()
