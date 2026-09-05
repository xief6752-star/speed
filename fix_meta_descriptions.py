#!/usr/bin/env python3
"""
修复 SEO 问题：扩展过短的 meta description
目标长度：150-160 字符
"""

import re
import os

# 定义每个页面的扩展描述
descriptions = {
    "index.html": "2026年最新机场推荐排名，实时测速对比专线与中转机场。收录云图、极速云、寰宇云等热门机场深度评测，附机场科普、免费vs付费对比、跑路防坑指南、Clash使用教程。帮你快速找到稳定高速的科学上网工具，避免踩坑。",

    "yuntu-jichang-pingce.html": "云图机场深度评测：金融级专线传输，香港节点14ms超低延迟，158 MB/s实测速度，三网优化节点倍率统一1倍。开业优惠码yt88，¥20/月起。完美解锁ChatGPT、Netflix、Disney+、TikTok等全球流媒体，适合追求极致速度与稳定性的用户。",

    "jisuyun-jichang-pingce.html": "极速云机场深度评测：全内网IEPL三网专线，香港节点18ms低延迟，148 MB/s实测速度，180+节点覆盖5地区。新用户优惠码JSY888，¥25/月起。全解锁Netflix/Disney+/ChatGPT，三网回程专线保障晚高峰4K流畅，适合高频使用的办公与娱乐用户。",

    "huanyuyun-jichang-pingce.html": "寰宇云机场深度评测：全球130+节点，BGP高速中转，香港26ms低延迟，132 MB/s实测速度，¥18/月起，永久流量包最低¥158。八折优惠码hy888，解锁Netflix/ChatGPT。性价比极高的中转线路机场，适合预算有限的学生党与轻度用户。",

    "shunyun-jichang-pingce.html": "瞬云机场深度评测：全内网专线接入，香港节点28ms低延迟，125 MB/s实测速度，150+节点覆盖港日新美台。¥20/月起，新客优惠码20OFF，完美解锁Netflix/Disney+/ChatGPT。内网专线架构保障数据安全，适合注重隐私与稳定性的用户。",

    "shanhai-jichang-pingce.html": "山海机场深度评测：三网IEPL专线，香港35ms低延迟，115 MB/s实测速度，140+节点覆盖港日新美台，最多支持40台设备。¥15/月起，IEPL专线中价格最低，解锁Netflix/Disney+/ChatGPT。超高性价比专线机场，适合多设备家庭用户与小团队。",

    "compare.html": "2026年13家机场横向对比：下载速度、节点延迟、30天在线率、套餐价格、线路类型、协议支持、优惠码一表汇总。覆盖云图机场、极速云、寰宇云、山海机场等，帮你快速找到最适合自己的机场。提供客观数据对比，避免选择困难症。",

    "rank-stable.html": "2026年最稳定机场排行榜：按99天在线率、历史跑路记录、运营时长综合评分。云图机场、极速云、疾速云等长期稳定运营机场推荐，避免选到跑路机场。基于真实监控数据排名，帮你选择可长期信赖的科学上网服务。",

    "rank-value.html": "2026年性价比机场排行榜：综合流量/价格/速度/稳定性评分，筛选最划算的机场套餐。寰宇云、瞬云、极速云等高性价比机场对比，月付最低¥18起，附详细评测。帮预算有限用户找到物超所值的选择，避免花冤枉钱。",

    "coupon.html": "2026年最新机场优惠码汇总：云图机场、极速云、寰宇云、瞬云等13家机场官方优惠码，含注册折扣、新用户专享码、限时活动。每周更新，拒绝过期码。所有优惠码均经人工验证有效，帮你节省每一分钱。",

    "status.html": "2026年机场跑路预警与实时状态监测。收录13家机场当前运行状态、历史跑路记录、风险评级，帮你第一时间发现异常，及时切换备用机场避免断网。每日更新在线率数据，提供客观的机场健康度评估与预警提醒。",

    "jichang-tuijian-2026.html": "2026年最新机场推荐榜单，综合速度、稳定性、性价比、解锁能力五维评分。精选云图机场（金融专线）、极速云（IEPL三网）、寰宇云（高性价比）等，附使用建议和优惠码。基于真实测试数据推荐，帮你从众多机场中快速筛选出最适合的选择。",

    "jichang-shime.html": "机场是国内对代理服务商的俗称，基于Shadowsocks、VLESS、Trojan等协议实现加密隧道翻墙。本文图解机场工作原理、IEPL/CN2/BGP线路类型区别，帮你从零理解代理服务。新手必读科普文章，解答机场与VPN的本质区别。",

    "zenme-xuanze-jichang.html": "选机场完整指南：从实测下载速度、节点覆盖（港日新美核心线路）、晚高峰稳定性、性价比套餐、客户端兼容性、售后响应六个维度系统评估。附新手首选推荐策略与常见误区分析，帮你找到最适合自身需求的高速稳定代理服务，告别踩坑。",

    "jichang-paolu-fangkeng.html": "识别机场跑路7大预警信号：价格远低于市场、无法联系客服、过度强推年付套餐、频繁更换域名。本文从真实跑路案例出发，教你系统识别高风险机场特征，掌握月付起步、至少备用两家机场的防坑策略，将资金损失与流量数据泄露风险降至最低。",

    "jichang-changjian-wenti.html": "机场和VPN区别、能否看Netflix、为什么晚上速度慢、使用机场安全吗、机场跑路怎么办——五大常见问题详细解答，帮你避开机场使用的常见坑。覆盖新手最关心的协议选择、流媒体解锁、安全隐私、故障排查等实用话题。",

    "mianfei-vs-fuifei-jichang.html": "免费机场速度慢、隐私风险高、节点极少；付费机场专线高速、99%+在线率、全流媒体解锁。本文六维度对比告诉你免费机场适用场景，以及为什么日常应选付费专线机场。附真实测速数据对比，帮你理性评估免费与付费的实际差距。",

    "daili-xieyi-jiexi.html": "深度解析GFW流量检测手段（IP黑名单、特征检测、主动探测），以及Trojan、VLESS+Reality如何通过TLS伪装突破封锁。帮助你理解为什么2026年Reality是最难被封锁的协议。技术向深度文章，适合想了解底层原理的进阶用户。",

    "blog-iepl-vs-iplc.html": "详细解析IEPL和IPLC的区别：技术标准、延迟、价格、稳定性对比，与BGP中转/公网中转的横向对比，附2026年识别伪专线的方法和真实专线机场推荐。帮你理解专线类型差异，避免被商家虚假宣传误导，选到真正的高质量专线服务。",

    "blog-jichang-scenes.html": "2026年机场使用场景完整指南：日常上网/远程办公/Netflix追剧/ChatGPT/游戏/外贸6大场景拆解，每个场景的节点选择建议、机场推荐和配置要点，附场景对应推荐总表。帮你根据实际需求匹配最合适的机场类型与套餐档位。",

    "blog-netflix-jichang.html": "2026年机场解锁Netflix实测排名：云图机场/极速云/Helios等13家对比，分析Netflix检测原理、原生IP节点选择、各地区内容库差异、4K播放要求，附解锁验证方法。追剧党必读，教你如何稳定观看奈飞4K HDR内容。",

    "blog-chatgpt-jichang.html": "2026年机场使用 ChatGPT 完整指南：为什么普通节点不能用、如何选对原生IP美国节点、实测可用机场推荐、注册账号注意事项，帮你稳定访问 ChatGPT 和 Claude。解决IP被封、地区不支持等常见问题，AI用户必备攻略。",

    "blog-jichang-avoid-traps.html": "2026年机场选购避坑完全指南：超低价诱饵、无限流量骗局、伪专线宣传、强推长期套餐、山寨仿冒、虚假测速数据6大陷阱识别方法，附避坑选购检查清单。帮新手识破常见营销套路，避免被不良商家收割智商税。",

    "blog-clash-complete.html": "2026年Clash完整配置教程：推荐 Clash Verge Rev，覆盖 Windows 和 macOS 双平台，图文讲解下载安装、导入机场订阅、节点测速、开启系统代理与TUN模式，附常见问题解答。最详细的Clash客户端配置指南，5分钟完成所有设置。",

    "blog-google-play-android.html": "2026年安卓手机安装Google Play完整教程：为什么国内手机没有谷歌商店、APK直接安装方法（新手推荐）、谷歌三件套（GMS）安装步骤、登录Google账号常见问题解决。涵盖华为、小米、OPPO、vivo等主流品牌的具体安装方案。",

    "blog-hongmeng-google-play.html": "鸿蒙HarmonyOS无法安装Google Play的原因与解决方案：确认设备型号、为什么无法安装GMS、直接下载APK安装v2rayNG的完整步骤、鸿蒙推荐代理客户端列表。华为鸿蒙用户科学上网专用教程，提供替代方案。",

    "blog-telegram-register.html": "2026年国内注册 Telegram 完整教程：为什么无法直接注册、需要什么准备、手机号注册5步流程、+86手机号技巧、没有外国号码如何用接码平台、注册后安全设置指南。覆盖iOS和Android双平台，附隐私保护建议与常见错误解决方法。",

    "faq.html": "2026年机场使用全面FAQ：机场原理、如何选购、节点延迟倍率解读、晚高峰卡顿解决、流媒体AI解锁、跑路防坑、故障排查等40+常见问题，分8大类详细解答。从入门到进阶，覆盖机场使用的方方面面，新老用户疑问一站式解决。",

    "monthly-report-2026-07.html": "2026年7月机场月度报告：云图、极速云、寰宇云等13家机场7月测速数据汇总，含速度/延迟/在线率/流媒体解锁综合评分。七月高温季节机场稳定性全面评测。提供当月排名变化分析，帮你了解各家机场的真实表现趋势。",

    "monthly-report-2026-08.html": "2026年8月机场月度报告：云图、极速云、寰宇云等13家机场8月测速数据汇总，含速度/延迟/在线率/流媒体解锁综合评分。本月新增工具页面，助力用户更好选择机场。每月持续追踪，为你提供最新的机场表现数据参考。",

    "tutorial.html": "SpeedRank 代理客户端详细配置教程，覆盖 Windows、macOS、iOS、Android 四大平台。图文讲解 Clash Verge Rev、v2rayN、Shadowrocket、ClashX 等主流软件的订阅导入与节点设置，5 分钟完成配置。新手小白也能轻松上手的傻瓜式教程。",

    "tutorial-clash-verge-rev.html": "Clash Verge Rev 图文配置教程，覆盖 Windows/macOS 双平台：下载安装、语言设置、机场订阅导入、节点测速选择、系统代理与 TUN 模式开启，5 步完成配置。2026年最推荐的Clash客户端，界面美观功能强大，支持全协议。",

    "tutorial-v2rayn.html": "v2rayN 图文配置教程：解压安装、添加订阅链接、更新订阅并测速、选择节点开启代理，4 步搞定 Windows 端 V2Ray 代理客户端配置。支持 VLESS/Trojan/Shadowsocks。轻量级客户端，占用资源少，适合配置较低的电脑。",

    "tutorial-v2rayng.html": "v2rayNG 图文配置教程：APK下载安装、添加订阅链接、更新订阅测速、选节点启动VPN，4步完成安卓端V2Ray代理配置。支持最新VLESS/Reality防封锁协议，完全免费开源。安卓平台最流行的代理客户端之一。",

    "tutorial-clashx.html": "ClashX 图文配置教程：macOS 安装授权、一键/手动导入机场配置、开启系统代理与规则分流，4 步完成 Mac 端 Clash 代理设置，国内直连国外走代理。macOS平台经典客户端，稳定可靠，适合Mac用户日常使用。",

    "tutorial-clash-android.html": "Clash for Android 图文配置教程：APK下载安装、从URL导入机场配置、激活配置文件、启动代理选择节点，4步完成安卓端Clash代理设置，支持VLESS/Trojan/Shadowsocks。功能全面的安卓Clash客户端。",

    "tutorial-shadowrocket.html": "Shadowrocket 小火箭使用教程：获取外区Apple ID、下载安装、一键导入机场订阅、连通性测试选节点、首次连接安装VPN配置，iPhone/iPad 完整5步操作指南。iOS平台最强代理客户端，功能丰富界面简洁。",

    "toolbox.html": "SpeedRank工具箱：免费提供IP地址查询、DNS泄露检测、流媒体解锁检测等在线工具，帮助机场用户验证代理节点是否正常工作，检测隐私泄露风险。实用工具集合，帮你全面检测机场节点质量与安全性。",

    "tool-ip-check.html": "免费在线IP地址查询工具：一键查看当前IP地址、IP归属地（国家/城市）、运营商ISP、是否使用代理/VPN/机场节点。支持IPv4和IPv6检测，翻墙用户必备工具。帮你快速验证代理是否生效，节点IP归属是否正确。",

    "tool-dns-leak.html": "检测您的机场/代理是否存在DNS泄露或WebRTC IP泄露。DNS泄露会暴露真实DNS服务器，WebRTC泄露会暴露真实IP地址，即使开启代理也无法隐藏。一键检测，结果直观。保护隐私的必备检测工具，避免真实身份暴露。",

    "tool-stream-check.html": "一键检测当前机场节点是否解锁Netflix、Disney+、YouTube Premium、HBO Max、Hulu、Prime Video等主流流媒体平台。显示解锁区域、内容库版本，帮您找到真正能看正版流媒体的机场节点。追剧党必备检测工具。",

    "tool-calculator.html": "机场选购计算器：输入使用场景（看剧/游戏/办公）与预算，智能计算流量需求并推荐最适合的机场套餐。基于实测数据提供个性化建议，避免选错套餐浪费钱。帮你科学评估流量需求，找到最经济实惠的套餐方案。",

    "airport.html": "SpeedRank 深度测评报告：实时下载速度、中位延迟、在线率、套餐价格、支持协议（VLESS/Trojan/Reality）与跑路风险评分一览。覆盖香港、日本、新加坡、美国等热门节点，帮你快速判断该机场是否值得长期订阅。客观数据说话，拒绝软文推广。",

    # 机场评测页面
    "cloudflux-jichang-pingce.html": "CloudFlux机场深度评测：IEPL/IPLC双线专线接入，86个节点覆盖6地区（含韩国/法国特色节点），香港45ms延迟，92 MB/s实测速度，99.6%在线率。¥66/月起。双线专线保障，特色地区节点丰富，适合需要多地区覆盖的用户。",

    "helios-jichang-pingce.html": "Helios机场深度评测：直连日本专线，日本节点24个+韩国14个，深度解锁Netflix日区/Disney+JP/亚马逊日本，香港42ms延迟，64 MB/s实测速度。¥58/月，日区流媒体首选。日本动漫游戏爱好者专属机场。",

    "nexitaly-jichang-pingce.html": "NexITaly机场深度评测：意大利团队运营，国际BGP中转，120+节点覆盖7地区，香港38ms延迟，105 MB/s实测速度，欧洲节点（英国/德国）覆盖是本站最全之一。¥88/月起。欧洲商务与留学用户的理想选择。",

    "nimbus-jichang-pingce.html": "Nimbus机场深度评测：新手友好，配置流程极简，50个节点覆盖港美日新英，¥19/月入门价格，支持Shadowsocks/V2Ray协议，适合偶尔轻度使用的初学者。零基础也能快速上手的傻瓜式机场。",

    "orbital-jichang-pingce.html": "Orbital机场深度评测：高端商业专线，企业级SLA保障，香港32ms超低延迟，88 MB/s实测速度，60个精品节点覆盖港日美新台，99.9%在线率。¥158/月，适合商务用户。企业团队与高要求用户的专业选择。",

    "phantom-jichang-pingce.html": "Phantom机场深度评测：隐私优先设计，零日志政策，支持加密货币匿名支付，40个节点覆盖美德荷瑞士瑞典欧洲5地，97.8%在线率。¥35/月，适合隐私敏感用户。注重数据安全与匿名性的用户首选。",

    "stargate-jichang-pingce.html": "StarGate机场深度评测：全球200+节点覆盖9大地区（美英日德澳荷加法新），流媒体解锁全覆盖，78 MB/s实测速度，¥39/月起。节点数量是本站最多的机场。全球出差党与多地区需求用户的理想选择。",

    "vortex-jichang-pingce.html": "Vortex机场深度评测：CN2 GIA回程线路，高峰期稳定性出色，75个节点覆盖6地区含澳大利亚，香港54ms延迟，71 MB/s实测速度，99.4%在线率。¥49/月起。CN2线路保障晚高峰稳定，适合对稳定性要求高的用户。",
}

def fix_description(file_path, new_desc):
    """修复单个文件的 meta description"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 查找并替换 meta description
        pattern = r'(<meta\s+name="description"\s+(?:id="[^"]*"\s+)?content=")([^"]*)(")'

        def replace_desc(match):
            return match.group(1) + new_desc + match.group(3)

        new_content = re.sub(pattern, replace_desc, content)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, len(new_desc)
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
                print(f"✓ {filename}: 已更新为 {length} 字符")
                updated += 1
            else:
                print(f"✗ {filename}: 更新失败 - {length}")
                failed += 1
        else:
            print(f"⊘ {filename}: 文件不存在")
            failed += 1

    print(f"\n完成：{updated} 个文件已更新，{failed} 个失败")

if __name__ == "__main__":
    main()

