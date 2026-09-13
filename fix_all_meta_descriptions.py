#!/usr/bin/env python3
"""
批量修复所有 HTML 文件的 meta description，统一到 150-160 字符
"""

import re

descriptions = {
    # SHORT 文件 (当前 < 150)
    "coupon.html": "2026年最新机场优惠码汇总：云图机场、极速云、寰宇云、瞬云等13家机场官方优惠码，含注册折扣、新用户专享码、限时活动与续费优惠。每周更新，拒绝过期码。所有优惠码均经人工验证有效，帮你节省每一分钱，获得最优购买价格。",

    "tool-calculator.html": "2026年机场流量计算器在线工具：根据每日使用时长、视频画质（1080p/4K）、视频平台类型智能估算月流量需求，帮你选择合适的机场套餐档位，避免流量浪费或不够用。支持Netflix、YouTube、日常浏览等多场景计算，提供精准套餐推荐。",

    "airport23-jichang-pingce.html": "Helios 机场深度评测：全内网专线架构，140 MB/s实测速度，20ms超低延迟，170个优质节点覆盖港日新美台，稳定率99.7%。优惠码HELIOS2026，¥30/月起。全IEPL专线保障晚高峰4K流畅，解锁Netflix/Disney+/ChatGPT，适合追求极致速度与稳定性的专业用户。",

    "blog-iepl-vs-iplc.html": "详细解析IEPL和IPLC的区别：技术标准、延迟、价格、稳定性对比，与BGP中转/公网中转的横向对比，附2026年识别伪专线的方法和真实专线机场推荐清单。帮你理解专线类型差异，避免被商家虚假宣传误导，选到真正的高质量专线服务。",

    "airport16-jichang-pingce.html": "Vortex 机场深度评测：BGP三网优化线路，128 MB/s实测速度，27ms低延迟，115个优质节点覆盖港日新美，稳定率99.5%。优惠码VX2026，¥18/月起。BGP智能路由保障高峰期稳定连接，解锁Netflix/Disney+/ChatGPT流媒体，入门性价比之选，适合预算有限的日常用户。",

    "airport17-jichang-pingce.html": "Nimbus 机场深度评测：优质中转线路机场，126 MB/s实测速度，28ms低延迟，120个优质节点覆盖港日新美，稳定率99.5%。优惠码NB888，¥19/月起。中转线路稳定保障日常使用流畅，解锁Netflix/Disney+/ChatGPT流媒体，适合预算有限的轻中度用户。",

    "airport21-jichang-pingce.html": "Phantom 机场深度评测：精品中转线路，134 MB/s实测速度，25ms低延迟，145个优质节点覆盖港日新美，稳定率99.6%。优惠码PH2026，¥22/月起。精品线路保障高峰期稳定连接，完美解锁Netflix/Disney+/ChatGPT流媒体，适合追求稳定体验的日常用户。",

    "blog-jichang-scenes.html": "2026年机场使用场景完整指南：日常上网/远程办公/Netflix追剧/ChatGPT/游戏/外贸6大场景拆解，每个场景的节点选择建议、机场推荐和配置要点，附场景对应推荐总表。帮你根据实际需求匹配最合适的机场类型与套餐档位，避免选择困难症。",

    "rank-stable.html": "2026年最稳定机场排行榜：按99天在线率、历史跑路记录、运营时长综合评分。云图机场、极速云、Helios等长期稳定运营机场推荐，避免选到跑路机场。基于真实监控数据排名，帮你选择可长期信赖的科学上网服务，降低跑路风险。",

    "airport15-jichang-pingce.html": "Stargate 机场深度评测：BGP高速中转线路，130 MB/s实测速度，26ms低延迟，125个优质节点覆盖港日新美，稳定率99.5%。优惠码SG2026，¥20/月起。BGP智能路由保障高峰期稳定，解锁Netflix/Disney+/ChatGPT流媒体，性价比均衡之选，适合日常办公娱乐用户。",

    "blog-netflix-jichang.html": "2026年机场解锁Netflix实测排名：云图机场/极速云/Helios等13家对比，分析Netflix检测原理、原生IP节点选择、各地区内容库差异、4K播放要求，附解锁验证方法。追剧党必读，教你如何稳定观看奈飞4K HDR内容，避免黑屏问题。",

    "airport19-jichang-pingce.html": "Cloudflux 机场深度评测：BGP优化线路机场，127 MB/s实测速度，28ms低延迟，110个优质节点覆盖港日新美，稳定率99.5%。优惠码CF888，¥18/月起。BGP三网优化保障日常使用流畅，解锁Netflix/Disney+/ChatGPT流媒体，适合预算有限的入门用户。",

    "airport20-jichang-pingce.html": "Nexitaly 机场深度评测：精品中转线路机场，132 MB/s实测速度，25ms低延迟，135个优质节点覆盖港日新美欧，稳定率99.6%。优惠码NX2026，¥23/月起。精品中转线路保障高峰期稳定，解锁Netflix/Disney+/ChatGPT流媒体，适合追求稳定体验的用户。",

    "blog-jichang-avoid-traps.html": "2026年机场选购避坑完全指南：超低价诱饵、无限流量骗局、伪专线宣传、强推长期套餐、山寨仿冒、虚假测速数据6大陷阱识别方法，附避坑选购检查清单。帮新手识破常见营销套路，避免被不良商家收割智商税，保护资金与隐私安全。",

    "rank-value.html": "2026年性价比机场排行榜：综合流量/价格/速度/稳定性评分，筛选最划算的机场套餐。寰宇云、瞬云、极速云等高性价比机场对比，月付最低¥18起，附详细评测与优惠码。帮预算有限用户找到物超所值的选择，避免花冤枉钱，实现性能与价格最优平衡。",

    "airport18-jichang-pingce.html": "Orbital 机场深度评测：优质中转线路机场，129 MB/s实测速度，27ms低延迟，118个优质节点覆盖港日新美，稳定率99.5%。优惠码OB888，¥19/月起。中转线路稳定保障日常使用流畅体验，解锁Netflix/Disney+/ChatGPT流媒体，适合预算有限的日常用户。",

    "blog-telegram-register.html": "2026年Telegram注册完整教程：解决+86手机号无法收验证码问题，提供免费接码平台推荐、虚拟号码注册方法、注册常见问题排查。图文详解从下载到登录全流程，5分钟完成注册。新手必读，附隐私设置建议与安全使用技巧，避免账号被封。",

    "jichang-changjian-wenti.html": "机场和VPN区别、能否看Netflix、为什么晚上速度慢、使用机场安全吗、机场跑路怎么办——五大常见问题详细解答，帮你避开机场使用的常见坑。覆盖新手最关心的协议选择、流媒体解锁、安全隐私、故障排查等实用话题，提供可操作的解决方案。",

    "mianfei-vs-fuifei-jichang.html": "免费机场速度慢、隐私风险高、节点极少；付费机场专线高速、99%+在线率、全流媒体解锁。本文六维度对比告诉你免费机场适用场景，以及为什么日常应选付费专线机场。附真实测速数据对比，帮你理性评估免费与付费的实际差距，做出明智选择。",

    "blog-google-play-android.html": "2026年安卓手机安装Google Play完整教程：为什么国内手机没有谷歌商店、APK直接安装方法（新手推荐）、谷歌三件套（GMS）安装步骤、登录Google账号常见问题解决。涵盖华为、小米、OPPO、vivo等主流品牌的具体安装方案，5分钟完成配置。",

    "compare.html": "2026年13家机场横向对比：下载速度、节点延迟、30天在线率、套餐价格、线路类型、协议支持、优惠码一表汇总。覆盖云图机场、极速云、寰宇云、山海机场等热门机场，帮你快速找到最适合自己的机场。提供客观数据对比，避免选择困难症，快速筛选。",

    "daili-xieyi-jiexi.html": "深度解析GFW流量检测手段（IP黑名单、特征检测、主动探测），以及Trojan、VLESS+Reality如何通过TLS伪装突破封锁。帮助你理解为什么2026年Reality是最难被封锁的协议。技术向深度文章，适合想了解底层原理的进阶用户，提升安全意识。",

    "tutorial-clash-android.html": "2026年安卓 Clash 完整配置教程：推荐 Clash Meta for Android，图文讲解下载安装、导入机场订阅链接、节点测速与切换、开启代理模式，附常见问题解答。安卓手机科学上网最详细的教程，5分钟完成所有设置，新手也能轻松上手。",

    "cloudflux-jichang-pingce.html": "Cloudflux 机场深度评测：BGP优化线路机场，127 MB/s实测速度，28ms低延迟，110个优质节点覆盖港日新美，稳定率99.5%。优惠码CF888，¥18/月起。BGP三网优化保障日常使用流畅，解锁Netflix/Disney+/ChatGPT流媒体，适合预算有限的入门用户。",

    "tool-stream-check.html": "2026年在线流媒体解锁检测工具：一键检测当前IP是否可访问Netflix、Disney+、HBO Max、ChatGPT、TikTok等热门平台，实时验证机场节点解锁能力。支持查看IP归属地、检测DNS泄露，帮你快速判断节点是否满足观看需求，避免购买后无法使用。",

    "airport14-jichang-pingce.html": "山海机场深度评测：三网IEPL专线，香港35ms低延迟，115 MB/s实测速度，140+节点覆盖港日新美台，最多支持40台设备。¥15/月起，IEPL专线中价格最低，解锁Netflix/Disney+/ChatGPT。超高性价比专线机场，适合多设备家庭用户与小团队协作使用。",

    "monthly-report-2026-07.html": "2026年7月机场监测月报：13家机场在线率、速度波动、跑路预警综合评估。云图机场、极速云等头部机场7月表现分析，新增机场风险提示，当月优惠活动汇总。基于真实监控数据，帮你及时发现异常机场，调整订阅策略，避免断网风险，保持稳定连接。",

    "monthly-report-2026-08.html": "2026年8月机场监测月报：13家机场在线率、速度波动、跑路预警综合评估。云图机场、极速云等头部机场8月表现分析，新增机场风险提示，当月优惠活动汇总。基于真实监控数据，帮你及时发现异常机场，调整订阅策略，避免断网风险，保持稳定连接。",

    "nimbus-jichang-pingce.html": "Nimbus 机场深度评测：优质中转线路机场，126 MB/s实测速度，28ms低延迟，120个优质节点覆盖港日新美，稳定率99.5%。优惠码NB888，¥19/月起。中转线路稳定保障日常使用流畅，解锁Netflix/Disney+/ChatGPT流媒体，适合预算有限的轻中度用户。",

    "tutorial-clash-verge-rev.html": "2026年 Clash Verge Rev 完整配置教程：Windows 和 macOS 双平台图文讲解，覆盖下载安装、导入机场订阅、节点测速与切换、开启系统代理与TUN模式，附常见问题解答。最详细的 Clash Verge Rev 客户端配置指南，5分钟完成所有设置，新手也能轻松上手。",

    "tutorial-v2rayn.html": "2026年 v2rayN 完整配置教程：Windows 平台最流行的代理客户端，图文讲解下载安装、导入机场订阅链接、节点测速与切换、开启系统代理模式，附常见问题排查。最详细的 v2rayN 使用指南，5分钟完成所有设置，新手小白也能轻松上手科学上网。",

    "stargate-jichang-pingce.html": "Stargate 机场深度评测：BGP高速中转线路，130 MB/s实测速度，26ms低延迟，125个优质节点覆盖港日新美，稳定率99.5%。优惠码SG2026，¥20/月起。BGP智能路由保障高峰期稳定，解锁Netflix/Disney+/ChatGPT流媒体，性价比均衡之选，适合日常办公娱乐用户。",

    "huanyuyun-jichang-pingce.html": "寰宇云机场深度评测：全球130+节点，BGP高速中转，香港26ms低延迟，132 MB/s实测速度，¥18/月起，永久流量包最低¥158。八折优惠码hy888，解锁Netflix/ChatGPT。性价比极高的中转线路机场，适合预算有限的学生党与轻度用户，入门首选。",

    "blog-clash-complete.html": "2026年Clash完整配置教程：推荐 Clash Verge Rev，覆盖 Windows 和 macOS 双平台，图文讲解下载安装、导入机场订阅、节点测速、开启系统代理与TUN模式，附常见问题解答。最详细的Clash客户端配置指南，5分钟完成所有设置，新手也能轻松上手科学上网。",

    "nexitaly-jichang-pingce.html": "Nexitaly 机场深度评测：精品中转线路机场，132 MB/s实测速度，25ms低延迟，135个优质节点覆盖港日新美欧，稳定率99.6%。优惠码NX2026，¥23/月起。精品中转线路保障高峰期稳定，解锁Netflix/Disney+/ChatGPT流媒体，适合追求稳定体验的用户。",

    "zenme-xuanze-jichang.html": "选机场完整指南：从实测下载速度、节点覆盖（港日新美核心线路）、晚高峰稳定性、性价比套餐、客户端兼容性、售后响应六个维度系统评估。附新手首选推荐策略与常见误区分析，帮你找到最适合自身需求的高速稳定代理服务，告别踩坑。",

    "jichang-paolu-fangkeng.html": "识别机场跑路7大预警信号：价格远低于市场、无法联系客服、过度强推年付套餐、频繁更换域名。本文从真实跑路案例出发，教你系统识别高风险机场特征，掌握月付起步、至少备用两家机场的防坑策略，将资金损失与流量数据泄露风险降至最低。",

    "orbital-jichang-pingce.html": "Orbital 机场深度评测：优质中转线路机场，129 MB/s实测速度，27ms低延迟，118个优质节点覆盖港日新美，稳定率99.5%。优惠码OB888，¥19/月起。中转线路稳定保障日常使用流畅体验，解锁Netflix/Disney+/ChatGPT流媒体，适合预算有限的日常用户。",

    "shunyun-jichang-pingce.html": "瞬云机场深度评测：全内网专线接入，香港节点28ms低延迟，125 MB/s实测速度，150+节点覆盖港日新美台。¥20/月起，新客优惠码20OFF，完美解锁Netflix/Disney+/ChatGPT。内网专线架构保障数据安全，适合注重隐私与稳定性的用户，提供企业级安全保障。",

    "jichang-tuijian-2026.html": "2026年最新机场推荐榜单，综合速度、稳定性、性价比、解锁能力五维评分。精选云图机场（金融专线）、极速云（IEPL三网）、寰宇云（高性价比）等，附使用建议和优惠码。基于真实测试数据推荐，帮你从众多机场中快速筛选出最适合的选择，避免踩坑。",

    "tool-dns-leak.html": "2026年在线DNS泄露检测工具：一键检测代理连接是否存在DNS泄露风险，验证真实DNS服务器地址，确保隐私安全。支持IPv4/IPv6双栈检测，实时显示DNS查询路径，帮你判断机场节点是否泄露真实位置信息，保护上网隐私，避免ISP监控与流量分析风险。",

    "yuntu-jichang-pingce.html": "云图机场深度评测：金融级专线传输，香港节点14ms超低延迟，158 MB/s实测速度，三网优化节点倍率统一1倍。开业优惠码yt88，¥20/月起。完美解锁ChatGPT、Netflix、Disney+、TikTok等全球流媒体，适合追求极致速度与稳定性的用户，企业级专线保障。",

    "airport22-jichang-pingce.html": "疾风云深度评测：顶级IPLC全专线机场，148 MB/s实测速度，19ms超低延迟，190个优质节点覆盖全球主要地区，稳定率99.8%。优惠码JF2026，¥38/月起。全IPLC专线接入保障晚高峰4K流畅，解锁Netflix/Disney+/ChatGPT，适合追求极致速度与稳定性的高端用户。",

    "airport29-jichang-pingce.html": "光年云深度评测：BGP优化线路机场，124 MB/s实测速度，29ms延迟，125个优质节点覆盖港日新美，稳定率99.5%。优惠码GN888，¥20/月起。BGP三网优化保障高峰期稳定连接，解锁Netflix/ChatGPT流媒体，¥20/月性价比均衡之选，适合日常办公与轻度娱乐用户。",

    "blog-hongmeng-google-play.html": "2026年鸿蒙HarmonyOS手机安装Google Play完整教程：华为鸿蒙系统为什么没有谷歌服务、APK直接安装方法、GMS安装器使用步骤、登录Google账号常见问题解决。覆盖Mate/P/Nova系列机型具体安装方案，附隐私风险提示与替代方案推荐。",

    "shanhai-jichang-pingce.html": "山海机场深度评测：三网IEPL专线，香港35ms低延迟，115 MB/s实测速度，140+节点覆盖港日新美台，最多支持40台设备。¥15/月起，IEPL专线中价格最低，解锁Netflix/Disney+/ChatGPT。超高性价比专线机场，适合多设备家庭用户与小团队协作使用。",

    "tool-ip-check.html": "2026年在线IP地址查询工具：一键检测当前真实IP地址、归属地、ISP运营商、IP类型（住宅/数据中心）、代理状态。实时验证机场节点是否生效，支持IPv4/IPv6双栈检测，帮你快速判断代理连接是否成功，确保科学上网正常工作，避免IP泄露风险。",

    "airport30-jichang-pingce.html": "暗影云深度评测：IPLC中速专线机场，136 MB/s实测速度，23ms超低延迟，165个优质节点覆盖全球主要地区，稳定率99.7%。优惠码AY2026，¥26/月起。IPLC专线保障高稳定性，完美解锁Netflix/Disney+/ChatGPT，速度与价格均衡的旗舰级专线机场选择。",

    "faq.html": "机场常见问题FAQ：机场是什么、机场和VPN区别、如何选择机场、能否看Netflix、为什么晚上速度慢、使用机场安全吗、机场跑路怎么办、如何导入订阅链接——8大常见问题详细解答。新手必读，覆盖协议选择、流媒体解锁、安全隐私、故障排查等实用话题。",

    "vortex-jichang-pingce.html": "Vortex 机场深度评测：BGP三网优化线路，128 MB/s实测速度，27ms低延迟，115个优质节点覆盖港日新美，稳定率99.5%。优惠码VX2026，¥18/月起。BGP智能路由保障高峰期稳定连接，解锁Netflix/Disney+/ChatGPT流媒体，入门性价比之选，适合预算有限的日常用户。",

    "jisuyun-jichang-pingce.html": "极速云机场深度评测：全内网IEPL三网专线，香港节点18ms低延迟，148 MB/s实测速度，180+节点覆盖5地区。新用户优惠码JSY888，¥25/月起。全解锁Netflix/Disney+/ChatGPT，三网回程专线保障晚高峰4K流畅，适合高频使用的办公与娱乐用户，企业级专线保障。",

    "airport28-jichang-pingce.html": "疾风云深度评测：顶级IPLC全专线机场，148 MB/s实测速度，19ms超低延迟，190个优质节点覆盖全球主要地区，稳定率99.8%。优惠码JF2026，¥38/月起。全IPLC专线接入保障晚高峰4K流畅，解锁Netflix/Disney+/ChatGPT，适合追求极致速度与稳定性的高端用户。",

    "helios-jichang-pingce.html": "Helios 机场深度评测：全内网专线架构，140 MB/s实测速度，20ms超低延迟，170个优质节点覆盖港日新美台，稳定率99.7%。优惠码HELIOS2026，¥30/月起。全IEPL专线保障晚高峰4K流畅，解锁Netflix/Disney+/ChatGPT，适合追求极致速度与稳定性的专业用户。",

    "tutorial-clashx.html": "2026年 ClashX 完整配置教程：macOS 平台最流行的代理客户端，图文讲解下载安装、导入机场订阅链接、节点测速与切换、开启系统代理与增强模式，附常见问题排查。最详细的 ClashX 使用指南，5分钟完成所有设置，Mac用户科学上网首选工具。",

    "jichang-shime.html": "机场是国内对代理服务商的俗称，基于Shadowsocks、VLESS、Trojan等协议实现加密隧道翻墙。本文图解机场工作原理、IEPL/CN2/BGP线路类型区别，帮你从零理解代理服务。新手必读科普文章，解答机场与VPN的本质区别，理解科学上网的底层原理。",

    "airport24-jichang-pingce.html": "光速云深度评测：BGP高速中转线路机场，128 MB/s实测速度，27ms低延迟，120个优质节点覆盖港日新美，稳定率99.5%。优惠码GS888，¥19/月起。BGP三网优化保障高峰期稳定连接，解锁Netflix/Disney+/ChatGPT流媒体，性价比均衡之选，适合日常办公与娱乐用户。",

    "tutorial-shadowrocket.html": "2026年 Shadowrocket 完整配置教程：iOS 平台最受欢迎的代理客户端，图文讲解 App Store 购买下载、导入机场订阅链接、节点测速与切换、开启代理模式，附常见问题排查。最详细的小火箭使用指南，5分钟完成所有设置，iPhone/iPad 科学上网首选。",

    # LONG 文件 (当前 > 160) - 缩短到 150-160
    "index.html": "2026年最新机场推荐排名，实时测速对比专线与中转机场。收录云图、极速云、寰宇云等热门机场深度评测，附机场科普、免费vs付费对比、跑路防坑指南、Clash使用教程。帮你快速找到稳定高速的科学上网工具，避免踩坑，基于真实监控数据客观推荐。",

    "airport25-jichang-pingce.html": "天际云深度评测：精品中转线路机场，135 MB/s实测速度，24ms低延迟，150个优质节点覆盖港日新美，稳定率99.6%。优惠码TJ2026，¥22/月起。精品中转线路保障高峰期稳定连接，完美解锁Netflix/Disney+/ChatGPT流媒体，适合追求稳定体验的日常用户。",

    "phantom-jichang-pingce.html": "Phantom 机场深度评测：精品中转线路，134 MB/s实测速度，25ms低延迟，145个优质节点覆盖港日新美，稳定率99.6%。优惠码PH2026，¥22/月起。精品线路保障高峰期稳定连接，完美解锁Netflix/Disney+/ChatGPT流媒体，适合追求稳定体验的日常用户。",

    "airport27-jichang-pingce.html": "星际云深度评测：IPLC精品专线机场，142 MB/s实测速度，21ms超低延迟，175个优质节点覆盖全球主要地区，稳定率99.7%。优惠码XJ2026，¥28/月起。IPLC专线保障晚高峰4K流畅，解锁Netflix/Disney+/ChatGPT，性能与价格均衡的专线机场选择。",

    "toolbox.html": "2026年机场工具箱：IP地址查询、流媒体解锁检测、DNS泄露检测、流量计算器4大在线工具，帮你验证机场节点是否生效、检测隐私安全风险、规划套餐流量。实时检测Netflix/Disney+/ChatGPT解锁状态，确保科学上网正常工作，保护隐私安全。",
}

pattern = re.compile(r'(<meta name="description"(?:\s+id="[^"]*")?\s+content=")([^"]*)(")')

def main():
    updated = 0
    failed = 0

    for filename, new_desc in descriptions.items():
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content, n = pattern.subn(
                lambda m: m.group(1) + new_desc + m.group(3),
                content,
                count=1
            )

            if n == 1 and new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✓ {filename}: 已更新为 {len(new_desc)} 字符")
                updated += 1
            else:
                print(f"⊙ {filename}: 无需更新或未找到匹配")

        except Exception as e:
            print(f"✗ {filename}: 更新失败 - {e}")
            failed += 1

    print(f"\n总结：成功更新 {updated} 个文件，失败 {failed} 个")

if __name__ == "__main__":
    main()
