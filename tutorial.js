const tutorialData = {
  'clash-verge-rev': {
    title: 'Clash Verge Rev 详细配置教程',
    desc: '基于 Tauri 框架的现代化 Clash 客户端，支持 Windows 和 macOS。性能优越，UI 现代，是目前最推荐的电脑端代理软件。',
    steps: [
      { title: '1. 下载与安装', desc: '前往 Clash Verge Rev 的 GitHub Releases 页面或机场提供的下载中心。Windows 用户请下载 `.exe` 安装包（推荐）或便携版压缩包。macOS 用户请下载 `.dmg` 文件（注意区分 Intel 芯片和 Apple Silicon M 系列芯片）。下载后双击按照默认提示完成安装。', img: 'img_steps.jpg' },
      { title: '2. 语言与基础设置', desc: '安装完成后启动 Clash Verge Rev。首次打开可能是英文界面，点击左侧菜单栏的 `Settings`（设置），在 `General`（通用）中找到 `Language` 并将其修改为 `zh-CN`（简体中文）。建议同时在设置中开启「开机自启」选项。' },
      { title: '3. 导入机场订阅', desc: '保持软件后台运行。打开浏览器登录您的机场官方网站后台，在用户中心或仪表盘找到「一键订阅」区域。点击「复制 Clash 订阅链接」。回到 Clash Verge 软件，点击左侧「订阅」面板，在右上角输入框粘贴刚刚复制的链接，然后点击「导入」或「保存」。', img: 'img_app.jpg' },
      { title: '4. 选择代理节点', desc: '订阅更新成功后，点击左侧的「代理」面板。在顶部的模式选择中，建议选择「规则」（Rule）模式（这样可以实现国内直连，国外走代理）。然后点击右上角的「测速」图标（闪电或波浪线），等待几秒钟后，列表中的节点会显示延迟数字（如 50ms）。选择一个数字较小且呈绿色的节点。' },
      { title: '5. 开启系统代理与 TUN 模式', desc: '最后一步，回到左侧的「设置」面板。找到「系统代理」（System Proxy）开关并将其打开。此时，您的浏览器和绝大部分软件已经可以科学上网了。<br/><br/>**进阶（TUN模式）**：如果您需要让游戏、终端命令行或者一些不走系统代理的软件也经过代理，请在设置中找到「TUN 模式」，点击安装虚拟网卡（服务模式），然后开启 TUN 模式开关。这会接管电脑的所有网络流量。' }
    ]
  },
  'v2rayn': {
    title: 'v2rayN 详细配置教程',
    desc: 'Windows 平台上最经典、最轻量级的代理客户端，支持 V2Ray、Trojan、Shadowsocks 等众多协议，适合老电脑或追求极致轻量的用户。',
    steps: [
      { title: '1. 下载与解压缩', desc: '下载 v2rayN-Core.zip 压缩包。注意：v2rayN 是一款绿色免安装软件，**千万不要直接在压缩包内双击运行**。请将整个压缩包解压到一个「纯英文路径」的文件夹中（例如 D:\\v2rayN）。解压后，找到带有蓝色 V 字图标的 `v2rayN.exe` 双击运行。如果提示缺少 .NET 框架，请按照提示前往微软官网下载安装。', img: 'img_steps.jpg' },
      { title: '2. 添加订阅链接', desc: '登录机场后台，找到并点击「复制 V2Ray 订阅链接」。回到 v2rayN 主界面，点击顶部菜单栏的「订阅」 -> 「订阅设置」。在弹出的窗口中点击左下角的「添加」，在备注处随便填写一个名字，在 `Url` 处粘贴您复制的订阅链接，点击确定保存。', img: 'img_app.jpg' },
      { title: '3. 更新订阅并测速', desc: '再次点击顶部菜单栏的「订阅」，选择「更新订阅（不通过代理）」。此时软件下方日志栏会提示获取成功，主界面会加载出几十个节点。按 `Ctrl+A` 全选所有节点，右键选择「测试服务器真连接延迟（多线程）」，等待几秒钟过滤出可用的节点。' },
      { title: '4. 选择节点并开启代理', desc: '在列表中选择一个延迟较低（有数字显示）的节点，按下 `回车键（Enter）` 将其设为活动节点，被选中的节点前面会出现一个 `√` 号。<br/><br/>最后，在电脑桌面右下角任务栏托盘找到 v2rayN 的图标，**右键点击图标**：<br/>1. 系统代理：选择「自动配置系统代理」（图标会变成红色）<br/>2. 路由：选择「绕过大陆(Whitelist)」模式。现在您可以正常上网了。' }
    ]
  },
  'clashx': {
    title: 'ClashX 详细配置教程',
    desc: 'Mac 平台上老牌的轻量级代理工具，原生支持 macOS，常驻状态栏，极简高效。',
    steps: [
      { title: '1. 下载与安装', desc: '下载 `ClashX.dmg` 文件。双击打开 DMG 文件后，会弹出一个安装窗口，鼠标左键按住左侧的 ClashX 图标，将其拖拽到右侧的 `Applications`（应用程序）文件夹中即完成安装。', img: 'img_steps.jpg' },
      { title: '2. 首次启动与授权', desc: '打开 Mac 的「启动台」，找到 ClashX 图标点击运行。首次打开时系统会提示「是从互联网下载的App，是否打开？」，请点击「打开」。接着可能会提示需要安装一个小工具（Helper），请输入您的 Mac 电脑开机密码并允许。启动成功后，屏幕右上角的菜单栏会出现一个灰色的小猫咪图标。' },
      { title: '3. 导入机场配置', desc: '推荐：在浏览器登录机场后台，直接点击「一键导入 ClashX」，如果系统弹出提示，选择「允许打开 ClashX」。<br/><br/>手动导入：如果一键导入失败，请复制 Clash 订阅链接。点击顶部状态栏的 ClashX 小猫咪图标，选择 `配置` -> `托管配置` -> `管理`，在弹出的窗口中点击「添加」，粘贴链接并点击确定，等待更新完成。', img: 'img_app.jpg' },
      { title: '4. 开启系统代理与分流', desc: '再次点击状态栏的 ClashX 图标。<br/>1. 勾选菜单中的「设置为系统代理」（Set as system proxy）。此时灰色图标会变色。<br/>2. 确保「出站模式」（Mode）选择为「规则」（Rule），这代表智能分流。<br/>3. 展开菜单中的「Proxy」或「Global」策略组，在里面选择一个您想连接的国家地区节点。' }
    ]
  },
  'shadowrocket': {
    title: 'Shadowrocket (小火箭) 详细配置教程',
    desc: 'iOS (iPhone/iPad) 端最普及、最好用的全能代理软件。注意：该软件在国区 App Store 已下架，必须使用外区 Apple ID 付费下载。',
    steps: [
      { title: '1. 获取非国区 Apple ID', desc: '您需要准备一个美区、港区或日区的 Apple ID。如果您没有，可以通过网页端自行注册（国家选择美国，付款方式填无即可）。请注意，**绝对不要在手机的 iCloud 中登录他人的 Apple ID**，这可能会导致您的手机被恶意锁机。**只能在 App Store 中登录。**' },
      { title: '2. 下载 Shadowrocket', desc: '打开手机上的 `App Store`，点击右上角的个人头像，滑到底部点击「退出登录」。然后登录您准备好的外区 Apple ID。搜索 `Shadowrocket`，认准开发者为 `Shadow Launch Technology Limited` 的应用。该软件售价约为 2.99 美元，需要购买后才能下载。', img: 'img_steps.jpg' },
      { title: '3. 一键导入节点订阅', desc: '打开 Safari 浏览器，登录您的机场后台网站。找到「一键订阅」功能，点击「导入到 Shadowrocket」。系统会自动拉起小火箭应用，并且在列表里出现您的机场节点名称。', img: 'img_app.jpg' },
      { title: '4. 连通性测试与配置修改', desc: '在小火箭首页，点击底部的「连通性测试」，节点右侧会出现数字（如 150ms），数字越小速度越快，超时的节点请不要选择。<br/><br/>接着，点击顶部的「全局路由」，确保勾选的是「配置」（Config）模式。如果是「代理」模式，会导致访问国内网站也绕路国外，变得非常卡顿。' },
      { title: '5. 首次连接与安装 VPN 配置', desc: '在节点列表中点击选择一个有延迟数字的节点（前面会出现小黄点）。然后点击右上角最顶部的未连接开关，将其拨向右侧。首次开启会弹出「想要添加 VPN 配置」的系统提示，点击「允许」，并输入您的 iPhone 锁屏密码或使用 FaceID 进行授权。连接成功后，手机屏幕顶部状态栏会出现 `VPN` 图标。' }
    ]
  },
  'clash-for-android': {
    title: 'Clash for Android 详细配置教程',
    desc: '安卓端最经典、用户基数最大的 Clash 客户端，支持智能分流与丰富的策略组管理。',
    steps: [
      { title: '1. 下载并安装', desc: '由于原作者已经删除了项目，您现在只能从机场提供的下载中心，或者一些可靠的第三方备份仓库（如 GitHub 上的开源备份）下载 `app-universal-release.apk` 安装包。下载后在安卓手机上进行常规安装。', img: 'img_steps.jpg' },
      { title: '2. 获取订阅与导入配置', desc: '打开手机浏览器，登录机场后台，点击复制「Clash 订阅链接」。<br/>打开 Clash for Android 应用，点击进入「配置」（Profiles）。<br/>点击右上角的 `+` 号「新配置」。<br/>选择「从 URL 导入」（URL）。<br/>在「名称」处随便填入机场名字，在「URL」处长按粘贴刚才复制的订阅链接。<br/>点击右上角的保存图标（软盘图标）。', img: 'img_app.jpg' },
      { title: '3. 激活配置文件', desc: '保存成功后，会自动返回到「配置」列表页面。此时您会看到刚才添加的配置文件。**点击该配置文件选中它**，配置文件的右侧会出现一个圆点被选中的状态。然后点击左上角的返回箭头，回到软件主界面。' },
      { title: '4. 启动代理与选择节点', desc: '在主界面，点击顶部那个灰色的、写着「已停止 / Tap to start」的圆形按钮。<br/>系统会弹出「网络连接请求」的警告（想要设置一个 VPN 连接），请点击「确定」或「允许」。<br/>当按钮变成蓝色并显示「运行中」时，表示代理已经开启。<br/><br/>最后，点击主界面的「代理」（Proxies）面板，点击右下角的闪电图标测试延迟，然后在一个展开的策略组中选择一个带有绿色数字的节点即可。' }
    ]
  },
  'v2rayng': {
    title: 'v2rayNG 详细配置教程',
    desc: '安卓端非常纯粹且强大的 V2Ray 协议客户端，支持最新的 VLESS/Reality 等防封锁协议，并且完全免费开源。',
    steps: [
      { title: '1. 下载与安装', desc: '前往 GitHub 搜索 v2rayNG 进入官方 Releases 页面，下载最新的 `v2rayNG_xxx_universal.apk`。如果您无法访问 GitHub，可以从机场后台的软件库获取。下载完毕后进行安装并打开。', img: 'img_steps.jpg' },
      { title: '2. 添加订阅链接', desc: '登录机场后台，复制专用于 v2rayNG 的「V2Ray 订阅链接」或通用订阅链接。打开 v2rayNG 应用，点击左上角的汉堡菜单 `≡`（三条横线），选择「订阅设置」。<br/><br/>点击右上角的 `+` 号。<br/>备注填写机场名字，地址（Url）粘贴你复制的订阅链接。<br/>点击右上角的 `√` 保存。', img: 'img_app.jpg' },
      { title: '3. 更新订阅并测速', desc: '按下手机的返回键回到 v2rayNG 的主界面。点击右上角的三个点 `⋮`，选择「更新订阅」。稍等几秒，屏幕上会刷出一长串节点列表。<br/><br/>再次点击右上角的三个点 `⋮`，选择「测试全部配置真连接」。等待测试完毕，挑选一个右侧显示有数字（延迟）的节点，点击选中它，此时该节点左侧会出现一条竖线表示已被选中。' },
      { title: '4. 启动 VPN 服务', desc: '点击右下角的 `V` 字形灰色圆形按钮。<br/>首次连接会弹出「网络连接请求」系统提示，这是正常现象，点击「确定」授权 VPN 权限。<br/>此时 `V` 字形按钮会变成绿色，并在手机状态栏出现 VPN 钥匙图标，代表您已经成功连接并可以科学上网了。' }
    ]
  },
  'default': {
    title: '客户端配置通用指南',
    desc: '无论您使用哪款代理软件，其核心逻辑基本是完全一致的。',
    steps: [
      { title: '1. 获取与安装客户端', desc: '首先，您需要前往机场提供的教程页面或 GitHub 下载对应操作系统的代理客户端。国内的 App Store 或应用商店通常无法搜索到这类软件，需要借助外区账号或下载 APK/EXE 独立安装包。', img: 'img_steps.jpg' },
      { title: '2. 复制订阅链接', desc: '所有的机场都会提供一个以 `http` 或 `https` 开头的“订阅链接”（Subscription Link）。这个链接里包含了该机场所有的服务器节点信息、密码和端口。请在机场后台找到“一键订阅”或“复制订阅链接”按钮。', img: 'img_app.jpg' },
      { title: '3. 在软件中添加并更新订阅', desc: '打开您下载好的代理软件，找到“配置”、“订阅设置”或“Profiles”相关的菜单，新建一个配置，并将刚才复制的订阅链接粘贴进去并保存。然后执行“更新”（Update）操作，软件就会通过该链接把成百上千个节点拉取到本地。' },
      { title: '4. 开启系统代理与规则分流', desc: '为了不影响国内 App（如微信、淘宝）的访问速度，请务必在软件中将代理模式（Mode）或路由（Routing）设置为“规则”（Rule）或“绕过局域网及大陆”（Bypass LAN & China）。最后，打开软件的总开关（System Proxy / Start），即可畅游网络。' }
    ]
  }
};

document.addEventListener('DOMContentLoaded', () => {
  const params = new URLSearchParams(window.location.search);
  const appId = params.get('id') || 'default';
  
  const data = tutorialData[appId] || tutorialData['default'];
  
  document.getElementById('pageTitle').textContent = `${data.title} · SpeedRank`;
  document.getElementById('tutTitle').textContent = data.title;
  document.getElementById('tutDesc').textContent = data.desc;
  
  const stepsContainer = document.getElementById('tutSteps');
  stepsContainer.innerHTML = data.steps.map((step, idx) => `
    <div class="tut-step">
      <div class="tut-step-num">${idx + 1}</div>
      <div class="tut-step-content">
        <h3>${step.title}</h3>
        <p>${step.desc}</p>
        ${step.img ? `
        <div class="tut-step-img">
          <img src="${step.img}" alt="步骤 ${idx + 1}" />
        </div>` : ''}
      </div>
    </div>
  `).join('');
});
