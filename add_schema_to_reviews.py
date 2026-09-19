#!/usr/bin/env python3
"""
为机场评测页面批量添加 Schema.org 结构化数据
"""

import re
import sys

# 机场数据映射（从 app.js 中提取）
airports_data = {
    'yuntu-jichang-pingce.html': {
        'name': '云图机场',
        'brand': '云图',
        'description': '金融级专线传输，158 MB/s实测速度，14ms超低延迟，160个优质节点覆盖港日新美台',
        'lowPrice': '20',
        'highPrice': '68',
        'rating': '4.9',
        'reviewBody': '云图机场采用金融级专线传输，三网优化节点倍率统一1倍。实测速度158 MB/s，延迟14ms，稳定率99.9%。完美解锁ChatGPT、Netflix、Disney+、TikTok等全球流媒体，适合追求极致速度与稳定性的用户。'
    },
    'jisuyun-jichang-pingce.html': {
        'name': '极速云机场',
        'brand': '极速云',
        'description': '全内网IEPL三网专线，148 MB/s实测速度，18ms低延迟，180+节点覆盖5地区',
        'lowPrice': '25',
        'highPrice': '78',
        'rating': '4.8',
        'reviewBody': '极速云采用全内网IEPL三网专线，实测速度148 MB/s，延迟18ms，稳定率99.9%。三网回程专线保障晚高峰4K流畅，全解锁Netflix/Disney+/ChatGPT，适合高频使用的办公与娱乐用户。'
    },
    'huanyuyun-jichang-pingce.html': {
        'name': '寰宇云机场',
        'brand': '寰宇云',
        'description': '全球130+节点，BGP高速中转，132 MB/s实测速度，26ms低延迟',
        'lowPrice': '18',
        'highPrice': '60',
        'rating': '4.7',
        'reviewBody': '寰宇云拥有全球130+节点，BGP高速中转线路，实测速度132 MB/s，延迟26ms，稳定率99.8%。八折优惠码hy888，解锁Netflix/ChatGPT，性价比极高的中转线路机场，适合预算有限的学生党与轻度用户。'
    },
    'shunyun-jichang-pingce.html': {
        'name': '瞬云机场',
        'brand': '瞬云',
        'description': '全内网专线接入，125 MB/s实测速度，28ms低延迟，150+节点覆盖港日新美台',
        'lowPrice': '20',
        'highPrice': '68',
        'rating': '4.7',
        'reviewBody': '瞬云采用全内网专线接入，实测速度125 MB/s，延迟28ms，稳定率99.9%。内网专线架构保障数据安全，完美解锁Netflix/Disney+/ChatGPT，适合注重隐私与稳定性的用户。'
    },
    'shanhai-jichang-pingce.html': {
        'name': '山海机场',
        'brand': '山海',
        'description': '三网IEPL专线，115 MB/s实测速度，35ms低延迟，140+节点覆盖港日新美台',
        'lowPrice': '15',
        'highPrice': '325',
        'rating': '4.6',
        'reviewBody': '山海机场采用三网IEPL专线，实测速度115 MB/s，延迟35ms，稳定率99.9%。¥15/月起，IEPL专线中价格最低，最多支持40台设备，解锁Netflix/Disney+/ChatGPT，超高性价比专线机场。'
    }
}

def add_schema_to_file(filename):
    """为单个文件添加 Schema.org 结构化数据"""
    if filename not in airports_data:
        print(f"⊙ {filename}: 无数据配置，跳过")
        return False

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否已经有 Schema.org 标记
        if 'application/ld+json' in content:
            print(f"✓ {filename}: 已包含结构化数据，跳过")
            return False

        data = airports_data[filename]

        # 构建 Schema.org JSON-LD
        schema = f'''
  <!-- Schema.org 结构化数据 -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "{data['name']}",
    "description": "{data['description']}",
    "brand": {{
      "@type": "Brand",
      "name": "{data['brand']}"
    }},
    "offers": {{
      "@type": "AggregateOffer",
      "lowPrice": "{data['lowPrice']}",
      "highPrice": "{data['highPrice']}",
      "priceCurrency": "CNY",
      "availability": "https://schema.org/InStock"
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "{data['rating']}",
      "bestRating": "5",
      "ratingCount": "1"
    }},
    "review": {{
      "@type": "Review",
      "reviewRating": {{
        "@type": "Rating",
        "ratingValue": "{data['rating']}",
        "bestRating": "5"
      }},
      "author": {{
        "@type": "Organization",
        "name": "SpeedRank"
      }},
      "reviewBody": "{data['reviewBody']}"
    }}
  }}
  </script>
'''

        # 在 canonical 标签后插入
        pattern = re.compile(r'(<link rel="canonical"[^>]*>)\n')
        new_content = pattern.sub(r'\1\n' + schema + '\n', content)

        if new_content == content:
            print(f"✗ {filename}: 未找到插入位置")
            return False

        # 写回文件
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✓ {filename}: 成功添加结构化数据")
        return True

    except Exception as e:
        print(f"✗ {filename}: 处理失败 - {e}")
        return False

def main():
    print("=== 批量添加 Schema.org 结构化数据 ===\n")

    success_count = 0
    for filename in airports_data.keys():
        if add_schema_to_file(filename):
            success_count += 1

    print(f"\n总结：成功添加 {success_count}/{len(airports_data)} 个页面的结构化数据")

if __name__ == '__main__':
    main()
