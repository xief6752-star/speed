#!/usr/bin/env python3
"""
为教程页面批量添加 HowTo Schema.org 结构化数据
"""

import re

tutorials_data = {
    'tutorial-clash-verge-rev.html': {
        'name': 'Clash Verge Rev 完整配置教程 2026',
        'description': 'Windows 和 macOS 双平台图文讲解，覆盖下载安装、导入机场订阅、节点测速与切换、开启系统代理与TUN模式',
        'steps': [
            {'name': '下载 Clash Verge Rev 客户端', 'text': '访问官网下载适合你操作系统的版本（Windows 或 macOS），解压后运行安装程序。'},
            {'name': '导入机场订阅链接', 'text': '从你的机场官网复制订阅链接，在 Clash Verge Rev 中点击"配置" → "新建" → "从 URL 导入"，粘贴订阅链接。'},
            {'name': '节点测速与选择', 'text': '点击"代理"标签，选择"延迟测试"对所有节点进行测速，选择延迟最低的节点。'},
            {'name': '开启系统代理', 'text': '点击顶部的"系统代理"开关，启用后所有流量将通过代理节点转发。'},
            {'name': '配置 TUN 模式（可选）', 'text': '在设置中启用 TUN 模式，实现全局透明代理，无需手动配置每个应用的代理设置。'}
        ]
    },
    'tutorial-v2rayn.html': {
        'name': 'v2rayN 完整配置教程 2026',
        'description': 'Windows 平台最流行的代理客户端，图文讲解下载安装、导入机场订阅链接、节点测速与切换、开启系统代理模式',
        'steps': [
            {'name': '下载 v2rayN 客户端', 'text': '访问 GitHub 下载最新版 v2rayN，同时下载 v2ray-core，解压到同一目录。'},
            {'name': '导入订阅链接', 'text': '右键点击托盘图标，选择"订阅" → "订阅设置"，添加你的机场订阅链接，点击"更新订阅"。'},
            {'name': '节点测速', 'text': '在主界面选择所有服务器，右键点击"测试服务器真延迟"，等待测速完成。'},
            {'name': '选择节点并启用代理', 'text': '双击选择延迟最低的节点，右键托盘图标，选择"系统代理" → "自动配置系统代理"。'},
            {'name': '验证连接', 'text': '打开浏览器访问 Google 或其他国外网站，确认代理生效。'}
        ]
    },
    'tutorial-shadowrocket.html': {
        'name': 'Shadowrocket 完整配置教程 2026',
        'description': 'iOS 平台最受欢迎的代理客户端，图文讲解 App Store 购买下载、导入机场订阅链接、节点测速与切换、开启代理模式',
        'steps': [
            {'name': '购买并下载 Shadowrocket', 'text': '在 App Store 搜索"Shadowrocket"（小火箭），购买并下载（需要美区账号，价格 $2.99）。'},
            {'name': '添加订阅链接', 'text': '打开 Shadowrocket，点击右上角 "+" 号，选择"类型" → "Subscribe"，粘贴机场订阅链接，点击"完成"。'},
            {'name': '更新订阅并测速', 'text': '在首页下拉刷新订阅，点击"连通性测试"对所有节点进行延迟测试。'},
            {'name': '选择节点并连接', 'text': '点击延迟最低的节点，然后点击顶部的连接开关，首次连接会要求添加 VPN 配置。'},
            {'name': '验证连接', 'text': '打开 Safari 访问 Google，确认代理已生效。可在"设置"中配置分流规则。'}
        ]
    },
    'tutorial-clashx.html': {
        'name': 'ClashX 完整配置教程 2026',
        'description': 'macOS 平台最流行的代理客户端，图文讲解下载安装、导入机场订阅链接、节点测速与切换、开启系统代理与增强模式',
        'steps': [
            {'name': '下载 ClashX 客户端', 'text': '访问 GitHub 下载 ClashX.dmg 安装包，打开后将应用拖到"应用程序"文件夹。'},
            {'name': '导入订阅配置', 'text': '点击菜单栏 ClashX 图标，选择"配置" → "托管配置" → "管理"，添加机场订阅链接。'},
            {'name': '更新订阅并测速', 'text': '点击"配置" → "更新"刷新订阅，然后在"代理"菜单中选择"测速"。'},
            {'name': '启用系统代理', 'text': '点击"设置为系统代理"，所有系统流量将通过 ClashX 转发。'},
            {'name': '配置增强模式（可选）', 'text': '启用"增强模式"实现更强大的流量劫持能力，需要输入密码授权。'}
        ]
    }
}

def generate_howto_schema(data):
    """生成 HowTo Schema.org JSON-LD"""
    steps_json = []
    for i, step in enumerate(data['steps'], 1):
        step_item = f'''    {{
      "@type": "HowToStep",
      "position": {i},
      "name": "{step['name']}",
      "text": "{step['text']}"
    }}'''
        steps_json.append(step_item)

    steps_str = ',\n'.join(steps_json)
    schema = f'''
  <!-- Schema.org 结构化数据 -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "HowTo",
    "name": "{data['name']}",
    "description": "{data['description']}",
    "step": [
{steps_str}
    ]
  }}
  </script>
'''
    return schema

def add_howto_schema(filename):
    """为教程页面添加 HowTo Schema"""
    if filename not in tutorials_data:
        print(f"⊙ {filename}: 无数据配置，跳过")
        return False

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否已经有 Schema
        if 'application/ld+json' in content:
            print(f"✓ {filename}: 已包含结构化数据，跳过")
            return False

        data = tutorials_data[filename]
        schema = generate_howto_schema(data)

        # 在 canonical 标签后插入
        pattern = re.compile(r'(<link rel="canonical"[^>]*>)\n')
        new_content = pattern.sub(r'\1\n' + schema + '\n', content)

        if new_content == content:
            print(f"✗ {filename}: 未找到插入位置")
            return False

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✓ {filename}: 成功添加 HowTo Schema")
        return True

    except Exception as e:
        print(f"✗ {filename}: 处理失败 - {e}")
        return False

def main():
    print("=== 批量添加 HowTo Schema.org 结构化数据 ===\n")

    success_count = 0
    for filename in tutorials_data.keys():
        if add_howto_schema(filename):
            success_count += 1

    print(f"\n总结：成功添加 {success_count}/{len(tutorials_data)} 个教程页面的结构化数据")

if __name__ == '__main__':
    main()
