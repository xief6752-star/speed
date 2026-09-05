#!/usr/bin/env python3
"""
补充修复剩余过短的 meta description
"""

import re
import os

# 定义需要扩展的描述
descriptions = {
    "airport28-jichang-pingce.html": "疾风云深度评测：顶级IPLC全专线机场，148 MB/s实测速度，19ms超低延迟，190个优质节点，稳定率99.8%。优惠码JF2026，¥38/月起。全IPLC专线接入保障晚高峰4K流畅，解锁Netflix/Disney+/ChatGPT，适合追求极致速度与稳定性的高端用户。",

    "airport29-jichang-pingce.html": "光年云深度评测：BGP优化线路机场，124 MB/s实测速度，29ms超低延迟，125个优质节点，稳定率99.5%。优惠码GN888，¥20/月起。BGP三网优化保障高峰期稳定，解锁Netflix/ChatGPT，¥20/月性价比均衡之选，适合日常办公与轻度娱乐用户。",

    "airport30-jichang-pingce.html": "暗影云深度评测：IPLC中速专线机场，136 MB/s实测速度，23ms超低延迟，165个优质节点，稳定率99.7%。优惠码AY2026，¥26/月起。IPLC专线保障高稳定性，完美解锁Netflix/Disney+/ChatGPT，速度与价格均衡的旗舰级专线机场选择。",

    "zenme-xuanze-jichang.html": "选机场完整指南：从实测下载速度、节点覆盖（港日新美核心线路）、晚高峰稳定性、性价比套餐、客户端兼容性、售后响应六个维度系统评估。附新手首选推荐策略与常见误区分析，帮你找到最适合自身需求的高速稳定代理服务，告别踩坑。",

    "jichang-paolu-fangkeng.html": "识别机场跑路7大预警信号：价格远低于市场、无法联系客服、过度强推年付套餐、频繁更换域名。本文从真实跑路案例出发，教你系统识别高风险机场特征，掌握月付起步、至少备用两家机场的防坑策略，将资金损失与流量数据泄露风险降至最低。",
}

def fix_description(file_path, new_desc):
    """修复单个文件的 meta description"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 查找并替换 meta description，处理可能的空格变化
        pattern = r'(<meta\s+name="description"\s+(?:id="[^"]*"\s+)?content=")([^"]*)(")'

        def replace_desc(match):
            return match.group(1) + new_desc + match.group(3)

        new_content = re.sub(pattern, replace_desc, content)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, len(new_desc.encode('utf-8'))
        return False, 0
    except Exception as e:
        return False, str(e)

def main():
    """主函数"""
    updated = 0
    failed = 0

    for filename, new_desc in descriptions.items():
        if os.path.exists(filename):
            success, length = fix_description(filename, new_desc)
            if success:
                print(f"✓ {filename}: 已更新为 {length} 字节")
                updated += 1
            else:
                print(f"✗ {filename}: 更新失败或无需更新 - {length}")
                failed += 1
        else:
            print(f"⊘ {filename}: 文件不存在")
            failed += 1

    print(f"\n完成：{updated} 个文件已更新，{failed} 个失败或无需更新")

if __name__ == "__main__":
    main()
