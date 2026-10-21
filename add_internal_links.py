#!/usr/bin/env python3
"""
内链优化脚本 - 为机场评测页面添加智能推荐链接
提升 SEO 权重传递和用户体验
"""
import os
import glob
import re
from typing import List, Dict

# 机场数据库 - 包含分类和特征
AIRPORTS = {
    'yuntu': {'name': '云图', 'type': '高端专线', 'price': 20, 'speed': 'extreme', 'features': ['IEPL', 'ChatGPT', 'Netflix']},
    'jisuyun': {'name': '极速云', 'type': '高端专线', 'price': 15, 'speed': 'high', 'features': ['IPLC', 'Netflix']},
    'huanyuyun': {'name': '寰宇云', 'type': '高端专线', 'price': 18, 'speed': 'high', 'features': ['IEPL', 'ChatGPT']},
    'shunyun': {'name': '瞬云', 'type': '中端专线', 'price': 12, 'speed': 'medium', 'features': ['专线', 'Netflix']},
    'shanhai': {'name': '山海', 'type': '高端专线', 'price': 25, 'speed': 'extreme', 'features': ['IEPL', 'ChatGPT', 'Netflix']},
    'kunpeng': {'name': '鲲鹏', 'type': '高性价比', 'price': 9, 'speed': 'medium', 'features': ['CN2', '入门']},
    'jiuyun': {'name': '玖云', 'type': '高性价比', 'price': 10, 'speed': 'medium', 'features': ['专线', '稳定']},
    'baoyun': {'name': '豹云', 'type': '中端专线', 'price': 15, 'speed': 'high', 'features': ['IPLC']},
    'nexitaly': {'name': 'Nexitaly', 'type': '高端专线', 'price': 22, 'speed': 'extreme', 'features': ['IEPL', 'Netflix']},
    'cloudflux': {'name': 'Cloudflux', 'type': '高端专线', 'price': 20, 'speed': 'extreme', 'features': ['IEPL']},
}

# 相关教程映射
RELATED_TUTORIALS = {
    'default': [
        {'url': 'tutorial-clash-verge-rev.html', 'title': 'Clash Verge Rev 配置教程'},
        {'url': 'tutorial-v2rayn.html', 'title': 'V2rayN 使用教程'},
        {'url': 'tutorial-shadowrocket.html', 'title': 'Shadowrocket iOS 教程'},
    ]
}

# 相关科普文章
RELATED_ARTICLES = [
    {'url': 'jichang-shime.html', 'title': '什么是机场？机场科普指南'},
    {'url': 'zenme-xuanze-jichang.html', 'title': '如何选择适合自己的机场'},
    {'url': 'blog-iepl-vs-iplc.html', 'title': 'IEPL vs IPLC 线路对比'},
]

def get_similar_airports(airport_key: str, limit: int = 3) -> List[Dict]:
    """获取相似机场推荐"""
    if airport_key not in AIRPORTS:
        return []

    current = AIRPORTS[airport_key]
    recommendations = []

    for key, info in AIRPORTS.items():
        if key == airport_key:
            continue

        # 计算相似度得分
        score = 0
        if info['type'] == current['type']:
            score += 3
        if abs(info['price'] - current['price']) <= 5:
            score += 2
        if info['speed'] == current['speed']:
            score += 2

        # 特征重叠
        common_features = set(info['features']) & set(current['features'])
        score += len(common_features)

        recommendations.append({
            'key': key,
            'name': info['name'],
            'score': score,
            'url': f'{key}-jichang-pingce.html'
        })

    # 按得分排序并返回
    recommendations.sort(key=lambda x: x['score'], reverse=True)
    return recommendations[:limit]

def generate_internal_links_html(airport_key: str) -> str:
    """生成内链推荐 HTML"""
    similar = get_similar_airports(airport_key, 3)

    html = '''
  <!-- 内链推荐区块 (SEO优化) -->
  <section class="related-section" style="margin: 40px 0; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 16px;">
    <h2 style="color: white; font-size: 24px; margin-bottom: 20px; text-align: center;">🔗 相关推荐</h2>

    <div class="related-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 30px;">
'''

    # 添加相似机场推荐
    if similar:
        html += '      <!-- 相似机场 -->\n'
        html += '      <div style="background: rgba(255,255,255,0.95); padding: 20px; border-radius: 12px;">\n'
        html += '        <h3 style="color: #667eea; font-size: 18px; margin-bottom: 15px;">📊 同类型机场</h3>\n'
        for airport in similar:
            html += f'        <a href="{airport["url"]}" style="display: block; color: #333; text-decoration: none; padding: 8px 0; border-bottom: 1px solid #eee; transition: color 0.2s;">\n'
            html += f'          → {airport["name"]}机场评测\n'
            html += '        </a>\n'
        html += '      </div>\n'

    # 添加教程链接
    html += '      <!-- 使用教程 -->\n'
    html += '      <div style="background: rgba(255,255,255,0.95); padding: 20px; border-radius: 12px;">\n'
    html += '        <h3 style="color: #667eea; font-size: 18px; margin-bottom: 15px;">📚 使用教程</h3>\n'
    for tutorial in RELATED_TUTORIALS['default']:
        html += f'        <a href="{tutorial["url"]}" style="display: block; color: #333; text-decoration: none; padding: 8px 0; border-bottom: 1px solid #eee; transition: color 0.2s;">\n'
        html += f'          → {tutorial["title"]}\n'
        html += '        </a>\n'
    html += '      </div>\n'

    # 添加科普文章
    html += '      <!-- 机场科普 -->\n'
    html += '      <div style="background: rgba(255,255,255,0.95); padding: 20px; border-radius: 12px;">\n'
    html += '        <h3 style="color: #667eea; font-size: 18px; margin-bottom: 15px;">💡 机场科普</h3>\n'
    for article in RELATED_ARTICLES[:3]:
        html += f'        <a href="{article["url"]}" style="display: block; color: #333; text-decoration: none; padding: 8px 0; border-bottom: 1px solid #eee; transition: color 0.2s;">\n'
        html += f'          → {article["title"]}\n'
        html += '        </a>\n'
    html += '      </div>\n'

    html += '    </div>\n'
    html += '  </section>\n'

    return html

def add_internal_links_to_file(filepath: str) -> bool:
    """为单个文件添加内链"""
    filename = os.path.basename(filepath)

    # 提取机场标识
    airport_key = None
    for key in AIRPORTS.keys():
        if key in filename:
            airport_key = key
            break

    if not airport_key:
        print(f"⏭️  跳过 {filename} (非机场评测页)")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查是否已有内链区块
    if '<!-- 内链推荐区块 (SEO优化) -->' in content:
        print(f"⏭️  跳过 {filename} (已有内链)")
        return False

    # 生成内链 HTML
    links_html = generate_internal_links_html(airport_key)

    # 在 footer 前插入
    if '<footer' in content:
        content = content.replace('<footer', links_html + '\n  <footer')
    else:
        # 在 </body> 前插入
        content = content.replace('</body>', links_html + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ {filename}: 添加内链推荐")
    return True

def main():
    print("🚀 内链优化 - 提升 SEO 权重传递\n")

    # 获取所有机场评测页面
    review_files = glob.glob('*-jichang-pingce.html')
    print(f"📊 找到 {len(review_files)} 个机场评测页面\n")

    updated_count = 0
    for filepath in sorted(review_files):
        if add_internal_links_to_file(filepath):
            updated_count += 1

    print(f"\n🎉 完成! 为 {updated_count} 个页面添加了内链推荐")
    print(f"\n📈 SEO 优化效果:")
    print(f"   • 降低跳出率")
    print(f"   • 提升页面停留时间")
    print(f"   • 增强权重传递")
    print(f"   • 改善用户体验")

if __name__ == '__main__':
    main()
