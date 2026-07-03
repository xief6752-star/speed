/* ==================== Airport Data ==================== */
const AIRPORTS = [
  {
    id: 'shunyun',
    name: '瞬云',
    emoji: '⚡',
    description: '极速稳定，全内网专线接入，无缝流媒体解锁',
    tags: ['fast', 'pro', 'stable'],
    tagLabels: ['极速', '专业', '稳定'],
    baseSpeed: 125,
    baseLatency: 28,
    uptime: 99.9,
    price: '¥20/月',
    link: 'https://ccc.jichang.best/#/register?code=KlIpTDPe',
    discount: '新客优惠码：20OFF',
    plans: [
      { name: '限时年付小包', desc: '59G 流量 / 月', price: '¥99.00 / 年' },
      { name: '行者', desc: '150G 流量 / 月', price: '¥20.00 / 月' },
      { name: '纵横', desc: '300G 流量 / 月', price: '¥36.00 / 月' },
      { name: '凌霄', desc: '800G 流量 / 月', price: '¥68.00 / 月' },
      { name: '2000G不限时', desc: '一次性流量包', price: '¥260.00 / 永久' },
      { name: '5000G不限时', desc: '一次性流量包', price: '¥600.00 / 永久' }
    ],
    nodeCount: 150,
    protocols: ['VLESS', 'Trojan', 'SS'],
    regions: [
      { flag: '🇭🇰', name: '香港', count: 40 },
      { flag: '🇯🇵', name: '日本', count: 35 },
      { flag: '🇸🇬', name: '新加坡', count: 30 },
      { flag: '🇺🇸', name: '美国', count: 25 },
      { flag: '🇹🇼', name: '台湾', count: 20 },
    ],
    nodes: generateNodes('shunyun', 150),
    color: 'linear-gradient(135deg, #0ea5e9, #0284c7)',
  },
  {
    id: 'huanyuyun',
    name: '寰宇云',
    emoji: '🌍',
    description: '全球节点覆盖，超高性价比，晚高峰秒开4K',
    tags: ['fast', 'value'],
    tagLabels: ['极速', '性价比'],
    baseSpeed: 110,
    baseLatency: 45,
    uptime: 99.8,
    price: '¥18/月',
    link: 'https://huanyuyunbest.com/#/register?code=CPBmzXgk',
    discount: '八折优惠码：hy888',
    plans: [
      { name: '年付小包', desc: '60GB 流量 / 月', price: '¥79.00 / 年' },
      { name: '基础版', desc: '150GB 流量 / 月', price: '¥18.00 / 月' },
      { name: '进阶版', desc: '300GB 流量 / 月', price: '¥34.00 / 月' },
      { name: '恒星', desc: '600GB 流量 / 月', price: '¥60.00 / 月' },
      { name: '巨量不限时', desc: '1000GB 永不过期', price: '¥158.00 / 永久' },
      { name: '海量不限时', desc: '3000GB 永不过期', price: '¥368.00 / 永久' }
    ],
    nodeCount: 130,
    protocols: ['Vmess', 'Reality', 'Trojan'],
    regions: [
      { flag: '🇺🇸', name: '美国', count: 35 },
      { flag: '🇭🇰', name: '香港', count: 30 },
      { flag: '🇯🇵', name: '日本', count: 25 },
      { flag: '🇬🇧', name: '英国', count: 20 },
      { flag: '🇸🇬', name: '新加坡', count: 20 },
    ],
    nodes: generateNodes('huanyuyun', 130),
    color: 'linear-gradient(135deg, #8b5cf6, #7c3aed)',
  },
  {
    id: 'shanhai',
    name: '山海机场',
    emoji: '🏔️',
    description: '三网IEPL专线，低倍高速直连，全流媒体解锁',
    tags: ['fast', 'pro', 'stable'],
    tagLabels: ['极速', '专线', '稳定'],
    baseSpeed: 115,
    baseLatency: 35,
    uptime: 99.9,
    price: '¥15/月',
    link: 'https://shanhai.cfd/#/register?code=3LM4SBu1',
    plans: [
      { name: '入门套餐', desc: '128GB 流量 / 月 (15台设备)', price: '¥15.00 / 月' },
      { name: '基础套餐', desc: '256GB 流量 / 月 (20台设备)', price: '¥25.00 / 月' },
      { name: '标准套餐', desc: '512GB 流量 / 月 (25台设备)', price: '¥45.00 / 月' },
      { name: '进阶套餐', desc: '1024GB 流量 / 月 (30台设备)', price: '¥85.00 / 月' },
      { name: '高级套餐', desc: '2048GB 流量 / 月 (35台设备)', price: '¥165.00 / 月' },
      { name: '豪华套餐', desc: '4096GB 流量 / 月 (40台设备)', price: '¥325.00 / 月' },
      { name: '限时至尊', desc: '海量专线大流量 / 月', price: '¥645.00 / 月' }
    ],
    nodeCount: 140,
    protocols: ['Vmess', 'Trojan', 'Shadowsocks'],
    regions: [
      { flag: '🇭🇰', name: '香港', count: 35 },
      { flag: '🇯🇵', name: '日本', count: 30 },
      { flag: '🇸🇬', name: '新加坡', count: 25 },
      { flag: '🇺🇸', name: '美国', count: 25 },
      { flag: '🇹🇼', name: '台湾', count: 25 },
    ],
    nodes: generateNodes('shanhai', 140),
    color: 'linear-gradient(135deg, #14b8a6, #0f766e)',
  },
  {
    id: 'nexitaly',
    name: 'NexITaly',
    emoji: '🚀',
    description: '意大利团队运营，国际BGP中转',
    tags: ['fast', 'pro'],
    tagLabels: ['极速', '专业'],
    baseSpeed: 105,
    baseLatency: 38,
    uptime: 99.8,
    price: '¥88/月',
    nodeCount: 120,
    protocols: ['Vmess', 'VLESS', 'Trojan'],
    regions: [
      { flag: '🇺🇸', name: '美国', count: 28 },
      { flag: '🇭🇰', name: '香港', count: 22 },
      { flag: '🇯🇵', name: '日本', count: 20 },
      { flag: '🇸🇬', name: '新加坡', count: 18 },
      { flag: '🇹🇼', name: '台湾', count: 14 },
      { flag: '🇬🇧', name: '英国', count: 10 },
      { flag: '🇩🇪', name: '德国', count: 8 },
    ],
    nodes: generateNodes('nexitaly', 120),
    color: 'linear-gradient(135deg, #6366f1, #8b5cf6)',
  },
  {
    id: 'cloudflux',
    name: 'CloudFlux',
    emoji: '⚡',
    description: 'IEPL/IPLC专线接入，低延迟保障',
    tags: ['stable', 'fast'],
    tagLabels: ['稳定', '极速'],
    baseSpeed: 92,
    baseLatency: 45,
    uptime: 99.6,
    price: '¥66/月',
    nodeCount: 86,
    protocols: ['Trojan', 'Shadowsocks', 'VLESS'],
    regions: [
      { flag: '🇭🇰', name: '香港', count: 20 },
      { flag: '🇯🇵', name: '日本', count: 18 },
      { flag: '🇺🇸', name: '美国', count: 16 },
      { flag: '🇸🇬', name: '新加坡', count: 14 },
      { flag: '🇰🇷', name: '韩国', count: 10 },
      { flag: '🇫🇷', name: '法国', count: 8 },
    ],
    nodes: generateNodes('cloudflux', 86),
    color: 'linear-gradient(135deg, #3b82f6, #06b6d4)',
  },
  {
    id: 'stargate',
    name: 'StarGate',
    emoji: '🌟',
    description: '全球30+地区节点，流媒体解锁',
    tags: ['value', 'stable'],
    tagLabels: ['高性价比', '稳定'],
    baseSpeed: 78,
    baseLatency: 62,
    uptime: 99.2,
    price: '¥39/月',
    nodeCount: 200,
    protocols: ['Shadowsocks', 'V2Ray', 'Trojan'],
    regions: [
      { flag: '🇺🇸', name: '美国', count: 40 },
      { flag: '🇬🇧', name: '英国', count: 30 },
      { flag: '🇯🇵', name: '日本', count: 28 },
      { flag: '🇩🇪', name: '德国', count: 24 },
      { flag: '🇦🇺', name: '澳大利亚', count: 20 },
      { flag: '🇳🇱', name: '荷兰', count: 18 },
      { flag: '🇸🇬', name: '新加坡', count: 16 },
      { flag: '🇨🇦', name: '加拿大', count: 12 },
      { flag: '🇫🇷', name: '法国', count: 12 },
    ],
    nodes: generateNodes('stargate', 200),
    color: 'linear-gradient(135deg, #10b981, #059669)',
  },
  {
    id: 'orbital',
    name: 'Orbital',
    emoji: '🛸',
    description: '高端商业专线，企业级SLA保障',
    tags: ['pro', 'fast'],
    tagLabels: ['专业', '极速'],
    baseSpeed: 88,
    baseLatency: 32,
    uptime: 99.9,
    price: '¥158/月',
    nodeCount: 60,
    protocols: ['VLESS', 'Reality', 'Trojan'],
    regions: [
      { flag: '🇭🇰', name: '香港', count: 16 },
      { flag: '🇯🇵', name: '日本', count: 14 },
      { flag: '🇺🇸', name: '美国', count: 12 },
      { flag: '🇸🇬', name: '新加坡', count: 10 },
      { flag: '🇹🇼', name: '台湾', count: 8 },
    ],
    nodes: generateNodes('orbital', 60),
    color: 'linear-gradient(135deg, #f59e0b, #ef4444)',
  },
  {
    id: 'nimbus',
    name: 'Nimbus',
    emoji: '☁️',
    description: '新手友好，简洁订阅，多平台客户端',
    tags: ['newbie', 'value'],
    tagLabels: ['新手友好', '高性价比'],
    baseSpeed: 55,
    baseLatency: 88,
    uptime: 98.5,
    price: '¥19/月',
    nodeCount: 50,
    protocols: ['Shadowsocks', 'V2Ray'],
    regions: [
      { flag: '🇭🇰', name: '香港', count: 12 },
      { flag: '🇺🇸', name: '美国', count: 10 },
      { flag: '🇯🇵', name: '日本', count: 10 },
      { flag: '🇸🇬', name: '新加坡', count: 8 },
      { flag: '🇬🇧', name: '英国', count: 10 },
    ],
    nodes: generateNodes('nimbus', 50),
    color: 'linear-gradient(135deg, #06b6d4, #3b82f6)',
  },
  {
    id: 'vortex',
    name: 'Vortex',
    emoji: '🌀',
    description: 'CN2 GIA回程，高峰期稳定性优秀',
    tags: ['stable', 'fast'],
    tagLabels: ['稳定', '极速'],
    baseSpeed: 71,
    baseLatency: 54,
    uptime: 99.4,
    price: '¥49/月',
    nodeCount: 75,
    protocols: ['Vmess', 'Trojan', 'Shadowsocks'],
    regions: [
      { flag: '🇺🇸', name: '美国', count: 18 },
      { flag: '🇯🇵', name: '日本', count: 15 },
      { flag: '🇭🇰', name: '香港', count: 12 },
      { flag: '🇸🇬', name: '新加坡', count: 10 },
      { flag: '🇩🇪', name: '德国', count: 10 },
      { flag: '🇦🇺', name: '澳大利亚', count: 10 },
    ],
    nodes: generateNodes('vortex', 75),
    color: 'linear-gradient(135deg, #8b5cf6, #ec4899)',
  },
  {
    id: 'helios',
    name: 'Helios',
    emoji: '☀️',
    description: '直连日本线路，解锁Netflix/Disney+',
    tags: ['fast', 'stable'],
    tagLabels: ['极速', '稳定'],
    baseSpeed: 64,
    baseLatency: 42,
    uptime: 99.1,
    price: '¥58/月',
    nodeCount: 65,
    protocols: ['Trojan', 'VLESS', 'Vmess'],
    regions: [
      { flag: '🇯🇵', name: '日本', count: 24 },
      { flag: '🇰🇷', name: '韩国', count: 14 },
      { flag: '🇺🇸', name: '美国', count: 12 },
      { flag: '🇭🇰', name: '香港', count: 10 },
      { flag: '🇸🇬', name: '新加坡', count: 5 },
    ],
    nodes: generateNodes('helios', 65),
    color: 'linear-gradient(135deg, #f59e0b, #10b981)',
  },
  {
    id: 'phantom',
    name: 'Phantom',
    emoji: '👻',
    description: '隐私优先，零日志政策，匿名支付',
    tags: ['stable'],
    tagLabels: ['稳定'],
    baseSpeed: 42,
    baseLatency: 110,
    uptime: 97.8,
    price: '¥35/月',
    nodeCount: 40,
    protocols: ['Shadowsocks', 'V2Ray'],
    regions: [
      { flag: '🇺🇸', name: '美国', count: 10 },
      { flag: '🇩🇪', name: '德国', count: 10 },
      { flag: '🇳🇱', name: '荷兰', count: 8 },
      { flag: '🇨🇭', name: '瑞士', count: 6 },
      { flag: '🇸🇪', name: '瑞典', count: 6 },
    ],
    nodes: generateNodes('phantom', 40),
    color: 'linear-gradient(135deg, #6b7280, #374151)',
  },
];

/* ==================== Node generator ==================== */
function generateNodes(airportId, count) {
  const countryPool = [
    { flag: '🇺🇸', name: '美国', prefix: 'US' },
    { flag: '🇭🇰', name: '香港', prefix: 'HK' },
    { flag: '🇯🇵', name: '日本', prefix: 'JP' },
    { flag: '🇸🇬', name: '新加坡', prefix: 'SG' },
    { flag: '🇹🇼', name: '台湾', prefix: 'TW' },
    { flag: '🇬🇧', name: '英国', prefix: 'UK' },
    { flag: '🇩🇪', name: '德国', prefix: 'DE' },
    { flag: '🇰🇷', name: '韩国', prefix: 'KR' },
    { flag: '🇫🇷', name: '法国', prefix: 'FR' },
    { flag: '🇦🇺', name: '澳大利亚', prefix: 'AU' },
    { flag: '🇨🇦', name: '加拿大', prefix: 'CA' },
    { flag: '🇳🇱', name: '荷兰', prefix: 'NL' },
    { flag: '🇮🇹', name: '意大利', prefix: 'IT' },
    { flag: '🇨🇭', name: '瑞士', prefix: 'CH' },
  ];
  const protos = ['Trojan', 'VLESS', 'Vmess', 'Shadowsocks', 'Reality'];
  const nodes = [];
  for (let i = 0; i < count; i++) {
    const c = countryPool[i % countryPool.length];
    const num = Math.floor(i / countryPool.length) + 1;
    const latency = Math.floor(Math.random() * 200) + 20;
    const online = Math.random() > 0.12;
    nodes.push({
      id: `${airportId}-${i}`,
      flag: c.flag,
      name: `${c.prefix}-${String(num).padStart(2,'0')}`,
      country: c.name,
      protocol: protos[i % protos.length],
      latency: online ? latency : null,
      speed: online ? parseFloat((Math.random() * 80 + 10).toFixed(1)) : null,
      online,
      type: latency < 80 ? '直连' : '中转',
    });
  }
  return nodes;
}

/* ==================== State ==================== */
let airports = AIRPORTS.map(a => ({ ...a, currentSpeed: null, testing: false }));
let currentFilter = 'all';
let currentAirport = null;
let nodeRegionFilter = 'all';
let testingInterval = null;

/* ==================== Particles ==================== */
function initParticles() {
  const container = document.getElementById('bgParticles');
  const colors = ['#6366f1','#8b5cf6','#06b6d4','#3b82f6','#10b981'];
  for (let i = 0; i < 18; i++) {
    const el = document.createElement('div');
    el.className = 'particle';
    const size = Math.random() * 5 + 2;
    const x = Math.random() * 100;
    const dur = Math.random() * 12 + 10;
    const delay = Math.random() * 12;
    const color = colors[Math.floor(Math.random() * colors.length)];
    el.style.cssText = `
      width:${size}px;height:${size}px;
      left:${x}%;
      background:${color};
      box-shadow:0 0 ${size*3}px ${color};
      animation-duration:${dur}s;
      animation-delay:-${delay}s;
    `;
    container.appendChild(el);
  }
}

/* ==================== Speed Test ==================== */
async function startSpeedTest() {
  const btn = document.getElementById('refreshBtn');
  btn.classList.add('spinning');
  btn.disabled = true;

  document.getElementById('progressBanner').style.display = 'block';
  updateStats();

  const total = airports.length;
  for (let i = 0; i < total; i++) {
    const a = airports[i];
    a.testing = true;
    a.currentSpeed = null;
    renderCard(a);

    // Update progress
    const pct = Math.round((i / total) * 100);
    document.getElementById('progressFill').style.width = pct + '%';
    document.getElementById('progressPct').textContent = pct + '%';
    document.getElementById('progressText').textContent = `正在测速 ${a.name}...`;

    // Simulate speed test (random jitter around base)
    await sleep(400 + Math.random() * 600);
    const jitter = (Math.random() - 0.3) * 30;
    a.currentSpeed = Math.max(1, +(a.baseSpeed + jitter).toFixed(1));
    a.testing = false;
    renderCard(a);
    updateStats();
  }

  // Done
  document.getElementById('progressFill').style.width = '100%';
  document.getElementById('progressPct').textContent = '100%';
  document.getElementById('progressText').textContent = '测速完成！';
  await sleep(800);
  document.getElementById('progressBanner').style.display = 'none';

  btn.classList.remove('spinning');
  btn.disabled = false;

  // Update timestamp
  const now = new Date();
  document.getElementById('updateTime').textContent =
    `上次测速 ${now.getHours().toString().padStart(2,'0')}:${now.getMinutes().toString().padStart(2,'0')}`;

  sortAndRender();
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

/* ==================== Render ==================== */
function getSpeedColor(speed) {
  if (speed >= 80) return 'linear-gradient(90deg, #2563eb, #0ea5e9)';
  if (speed >= 50) return 'linear-gradient(90deg, #0ea5e9, #10b981)';
  if (speed >= 25) return 'linear-gradient(90deg, #10b981, #f59e0b)';
  return 'linear-gradient(90deg, #ef4444, #f59e0b)';
}

function getSpeedText(speed) {
  if (speed === null) return '—';
  return speed >= 1000 ? (speed/1000).toFixed(1)+' GB/s' : speed.toFixed(1)+' MB/s';
}

function getLatencyClass(lat) {
  if (lat <= 60) return 'latency-low';
  if (lat <= 120) return 'latency-mid';
  return 'latency-high';
}

function getUptimeDots(uptime) {
  const filled = Math.round(uptime / 10);
  let html = '';
  for (let i = 0; i < 10; i++) {
    const opacity = i < filled ? 1 : 0.15;
    const color = uptime >= 99 ? '#10b981' : uptime >= 97 ? '#f59e0b' : '#ef4444';
    html += `<div class="uptime-dot" style="background:${color};opacity:${opacity};"></div>`;
  }
  return html;
}

function getRankBadgeClass(rank) {
  if (rank === 1) return 'gold';
  if (rank === 2) return 'silver';
  if (rank === 3) return 'bronze';
  return 'normal';
}

function getRankEmoji(rank) {
  if (rank === 1) return '🥇';
  if (rank === 2) return '🥈';
  if (rank === 3) return '🥉';
  return '#' + rank;
}

function renderCard(airport) {
  const el = document.getElementById('card-' + airport.id);
  if (!el) return;

  const speedPct = airport.currentSpeed ? Math.min(100, (airport.currentSpeed / 120) * 100) : 0;
  const speedColor = airport.currentSpeed ? getSpeedColor(airport.currentSpeed) : 'rgba(255,255,255,0.15)';
  const speedTxt = airport.testing ? '<span class="testing-text">测速中...</span>' : getSpeedText(airport.currentSpeed);

  el.querySelector('.speed-fill').style.width = speedPct + '%';
  el.querySelector('.speed-fill').style.background = speedColor;
  el.querySelector('.speed-label').innerHTML = `
    <span style="color:${airport.currentSpeed ? speedPct >= 67 ? '#2563eb' : speedPct >= 42 ? '#0ea5e9' : '#f59e0b' : '#94a3b8'}">${speedTxt}</span>
  `;
  el.classList.toggle('card-testing', airport.testing);
}

function renderTagHtml(tags, tagLabels) {
  const classMap = { fast:'tag-fast', stable:'tag-stable', value:'tag-value', newbie:'tag-newbie', pro:'tag-pro' };
  return tags.map((t, i) => `<span class="tag ${classMap[t] || ''}">${tagLabels[i]}</span>`).join('');
}

function renderList(list) {
  const container = document.getElementById('rankingList');
  if (!list.length) {
    container.innerHTML = `
      <div class="empty-state">
        <svg viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" stroke="currentColor" stroke-width="2"/><path d="M20 32h24M32 20v24" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        <p>没有找到匹配的机场</p>
      </div>`;
    return;
  }
  container.innerHTML = list.map((airport, idx) => {
    const rank = idx + 1;
    const rankClass = rank <= 3 ? 'rank-' + rank : '';
    const badgeClass = getRankBadgeClass(rank);
    const speedPct = airport.currentSpeed ? Math.min(100, (airport.currentSpeed / 120) * 100) : 0;
    const speedColor = airport.currentSpeed ? getSpeedColor(airport.currentSpeed) : '#e2e8f0';
    const onlineNodes = airport.nodes.filter(n => n.online).length;
    return `
    <div class="rank-card ${rankClass}" id="card-${airport.id}" onclick="location.href='airport.html?id=${airport.id}'">
      <div class="rank-badge ${badgeClass}">${getRankEmoji(rank)}</div>
      <div class="card-body">
        <div class="card-top">
          <span class="airport-name">${airport.emoji} ${airport.name}</span>
          <div class="airport-tags">${renderTagHtml(airport.tags, airport.tagLabels)}</div>
        </div>
        <div class="speed-row">
          <div class="speed-track">
            <div class="speed-fill" style="width:${speedPct}%;background:${speedColor};"></div>
          </div>
          <span class="speed-label" style="color:${airport.currentSpeed ? '#2563eb' : '#94a3b8'};">
            ${airport.currentSpeed ? airport.currentSpeed.toFixed(1) + ' MB/s' : '待测速'}
          </span>
        </div>
        <div class="card-meta">
          <span class="meta-item">
            <svg class="meta-icon" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="1.3"/><path d="M8 5v3l2 2" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
            <span class="meta-value">${airport.baseLatency}ms</span> 延迟
          </span>
          <span class="meta-item">
            <svg class="meta-icon" viewBox="0 0 16 16" fill="none"><rect x="2" y="6" width="3" height="8" rx="1" fill="currentColor" opacity=".4"/><rect x="6.5" y="4" width="3" height="10" rx="1" fill="currentColor" opacity=".7"/><rect x="11" y="2" width="3" height="12" rx="1" fill="currentColor"/></svg>
            <span class="meta-value">${onlineNodes}/${airport.nodeCount}</span> 节点在线
          </span>
          <span class="meta-item">
            <svg class="meta-icon" viewBox="0 0 16 16" fill="none"><path d="M8 2a6 6 0 1 0 0 12A6 6 0 0 0 8 2zm0 0v6l3 2" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
            <span class="meta-value">${airport.uptime}%</span> 在线率
          </span>
          <span class="meta-item">
            <svg class="meta-icon" viewBox="0 0 16 16" fill="none"><path d="M2 8h12M8 2c-2 2-3 4-3 6s1 4 3 6M8 2c2 2 3 4 3 6s-1 4-3 6" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
            <span class="meta-value">${airport.protocols[0]}</span>+
          </span>
          <span class="meta-item" style="margin-left:auto;font-weight:700;color:#818cf8;">${airport.price}</span>
        </div>
      </div>
      <div class="card-right">
        <div class="latency-badge ${getLatencyClass(airport.baseLatency)}">${airport.baseLatency} ms</div>
        <div class="uptime-wrap">
          <div class="uptime-dots">${getUptimeDots(airport.uptime)}</div>
        </div>
        <button class="view-btn" onclick="event.stopPropagation();location.href='airport.html?id=${airport.id}'">查看节点</button>
      </div>
    </div>
    `;
  }).join('');
}

/* ==================== Sort & Filter ==================== */
function getFilteredSorted() {
  const search = document.getElementById('searchInput').value.toLowerCase();
  const sort = document.getElementById('sortSelect').value;

  let list = airports.filter(a => {
    const matchSearch = !search || a.name.toLowerCase().includes(search) || a.description.includes(search);
    const matchFilter =
      currentFilter === 'all' ? true :
      currentFilter === 'fast' ? a.tags.includes('fast') :
      currentFilter === 'stable' ? a.tags.includes('stable') :
      currentFilter === 'affordable' ? a.tags.includes('value') : true;
    return matchSearch && matchFilter;
  });

  list.sort((a, b) => {
    if (sort === 'speed') return (b.currentSpeed ?? b.baseSpeed) - (a.currentSpeed ?? a.baseSpeed);
    if (sort === 'latency') return a.baseLatency - b.baseLatency;
    if (sort === 'nodes') return b.nodeCount - a.nodeCount;
    if (sort === 'uptime') return b.uptime - a.uptime;
    return 0;
  });
  return list;
}

function sortAndRender() { renderList(getFilteredSorted()); }
function filterAirports() { sortAndRender(); }
function setFilter(filter, el) {
  currentFilter = filter;
  document.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
  sortAndRender();
}

/* ==================== Stats ==================== */
function updateStats() {
  const tested = airports.filter(a => a.currentSpeed !== null);
  const speeds = tested.map(a => a.currentSpeed);
  const avgSpeed = speeds.length ? (speeds.reduce((s,v) => s+v,0) / speeds.length).toFixed(1) : 0;
  const topSpeed = speeds.length ? Math.max(...speeds).toFixed(1) : 0;
  const totalNodes = airports.reduce((s,a) => s + a.nodeCount, 0);
  document.getElementById('statTotal').textContent = airports.length;
  document.getElementById('statOnline').textContent = tested.length;
  document.getElementById('statAvgSpeed').textContent = avgSpeed > 0 ? avgSpeed + ' MB/s' : '—';
  document.getElementById('statTopSpeed').textContent = topSpeed > 0 ? topSpeed + ' MB/s' : '—';
  document.getElementById('statNodes').textContent = totalNodes;
}

/* ==================== Modal ==================== */
function openModal(airportId) {
  const airport = airports.find(a => a.id === airportId);
  if (!airport) return;
  currentAirport = airport;
  nodeRegionFilter = 'all';

  // Header
  document.getElementById('modalBadge').textContent = airport.emoji;
  document.getElementById('modalBadge').style.background = airport.color;
  document.getElementById('modalTitle').textContent = airport.name;
  document.getElementById('modalSubtitle').textContent = airport.description;

  // Stats
  const onlineNodes = airport.nodes.filter(n => n.online).length;
  document.getElementById('modalStats').innerHTML = `
    <div class="modal-stat">
      <span class="modal-stat-value" style="color:#1d4ed8;">${airport.currentSpeed ? airport.currentSpeed.toFixed(1)+' MB/s' : airport.baseSpeed+' MB/s'}</span>
      <span class="modal-stat-label">下载速度</span>
    </div>
    <div class="modal-stat">
      <span class="modal-stat-value" style="color:${airport.baseLatency<=60?'#34d399':airport.baseLatency<=120?'#fcd34d':'#f87171'};">${airport.baseLatency} ms</span>
      <span class="modal-stat-label">平均延迟</span>
    </div>
    <div class="modal-stat">
      <span class="modal-stat-value" style="color:#818cf8;">${onlineNodes} / ${airport.nodeCount}</span>
      <span class="modal-stat-label">节点在线</span>
    </div>
    <div class="modal-stat">
      <span class="modal-stat-value" style="color:#10b981;">${airport.uptime}%</span>
      <span class="modal-stat-label">在线率</span>
    </div>
  `;

  // Region filters
  const regions = ['all', ...new Set(airport.nodes.map(n => n.country))];
  document.getElementById('nodeFilters').innerHTML = regions.slice(0, 8).map(r => {
    const label = r === 'all' ? '全部' : r;
    return `<button class="node-filter-btn ${r === nodeRegionFilter ? 'active' : ''}" onclick="setNodeFilter('${r}', this)">${label}</button>`;
  }).join('');

  renderNodeGrid(airport);

  // Region chart
  const regionTotals = {};
  airport.nodes.forEach(n => { regionTotals[n.country] = (regionTotals[n.country] || 0) + 1; });
  const sortedRegions = Object.entries(regionTotals).sort((a,b) => b[1]-a[1]).slice(0, 8);
  const maxR = sortedRegions[0]?.[1] || 1;
  const flagMap = {};
  airport.nodes.forEach(n => { flagMap[n.country] = n.flag; });

  const gradients = [
    'linear-gradient(90deg,#2563eb,#0ea5e9)',
    'linear-gradient(90deg,#4f46e5,#2563eb)',
    'linear-gradient(90deg,#0ea5e9,#10b981)',
    'linear-gradient(90deg,#10b981,#059669)',
    'linear-gradient(90deg,#7c3aed,#4f46e5)',
    'linear-gradient(90deg,#f59e0b,#0ea5e9)',
    'linear-gradient(90deg,#0ea5e9,#2563eb)',
    'linear-gradient(90deg,#ec4899,#7c3aed)',
  ];
  document.getElementById('regionChart').innerHTML = sortedRegions.map(([name, count], i) => `
    <div class="region-row">
      <span class="region-flag">${flagMap[name] || '🌐'}</span>
      <span class="region-name">${name}</span>
      <div class="region-bar-track">
        <div class="region-bar-fill" style="width:${(count/maxR*100).toFixed(1)}%;background:${gradients[i % gradients.length]};"></div>
      </div>
      <span class="region-count">${count}</span>
    </div>
  `).join('');

  document.getElementById('modalOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function setNodeFilter(region, el) {
  nodeRegionFilter = region;
  document.querySelectorAll('.node-filter-btn').forEach(b => b.classList.remove('active'));
  el.classList.add('active');
  renderNodeGrid(currentAirport);
}

function renderNodeGrid(airport) {
  let nodes = airport.nodes;
  if (nodeRegionFilter !== 'all') nodes = nodes.filter(n => n.country === nodeRegionFilter);
  const display = nodes.slice(0, 48);

  document.getElementById('nodeGrid').innerHTML = display.map(node => {
    const latPct = node.latency ? Math.min(100, (node.latency / 300) * 100) : 0;
    const latColor = !node.latency ? '#94a3b8' : node.latency < 80 ? '#059669' : node.latency < 160 ? '#d97706' : '#dc2626';
    const protoColors = {
      Trojan:'#4f46e5', VLESS:'#0ea5e9', Vmess:'#059669', Shadowsocks:'#d97706', Reality:'#7c3aed'
    };
    return `
    <div class="node-card ${node.online ? '' : 'node-offline'}">
      <div class="node-header">
        <span class="node-flag">${node.flag}</span>
        <span class="node-name">${node.name}</span>
        <span class="node-status-dot ${node.online ? 'status-online' : 'status-offline'}"></span>
      </div>
      <div class="node-info">
        <div class="node-info-row">
          <span class="node-info-key">协议</span>
          <span class="node-info-val" style="color:${protoColors[node.protocol]||'#818cf8'}">${node.protocol}</span>
        </div>
        <div class="node-info-row">
          <span class="node-info-key">延迟</span>
          <span class="node-info-val" style="color:${latColor}">${node.latency ? node.latency+'ms' : '离线'}</span>
        </div>
        <div class="node-info-row">
          <span class="node-info-key">类型</span>
          <span class="node-info-val">${node.type}</span>
        </div>
        ${node.speed ? `<div class="node-info-row">
          <span class="node-info-key">速度</span>
          <span class="node-info-val" style="color:#06b6d4">${node.speed} MB/s</span>
        </div>` : ''}
      </div>
      <div class="node-latency-bar">
        <div class="node-latency-fill" style="width:${latPct}%;background:${latColor};"></div>
      </div>
    </div>
    `;
  }).join('');

  if (nodes.length > 48) {
    document.getElementById('nodeGrid').insertAdjacentHTML('beforeend',
      `<div style="grid-column:1/-1;text-align:center;padding:12px;font-size:13px;color:var(--text-muted);">还有 ${nodes.length - 48} 个节点未显示</div>`
    );
  }
}

function closeModal() {
  document.getElementById('modalOverlay').classList.remove('open');
  document.body.style.overflow = '';
}

/* ==================== Init ==================== */
function init() {
  updateStats();
  renderList(getFilteredSorted());
  // Auto start speed test after small delay
  setTimeout(startSpeedTest, 600);
}

document.addEventListener('DOMContentLoaded', init);

// Keyboard close
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeModal();
});

/* ==================== Tutorial Content ==================== */
const tutorials = {
  windows: [
    { id: "clash-verge-rev", name: "Clash Verge Rev", desc: "目前 Windows 上最推荐的代理客户端，基于 Tauri 框架，支持几乎所有协议，界面美观且功能强大。", img: "img_app.jpg", download: "https://github.com/clash-verge-rev/clash-verge-rev/releases" },
    { id: "v2rayn", name: "v2rayN", desc: "老牌经典的 Windows 客户端，支持 V2Ray、Trojan 等多种协议，资源占用极低，适合老电脑使用。", img: "img_app.jpg", download: "https://github.com/2dust/v2rayN/releases" },
    { id: "default", name: "NekoBox", desc: "基于 sing-box 核心的通用代理工具，支持最新的 VLESS-Reality 等协议，适合进阶用户。", img: "img_app.jpg", download: "https://github.com/MatsuriDayo/nekoray/releases" }
  ],
  macos: [
    { id: "clash-verge-rev", name: "Clash Verge Rev for Mac", desc: "Mac 端目前最好用的 Clash 客户端，完美支持 Apple Silicon，提供优秀的 UI 交互体验。", img: "img_app.jpg", download: "https://github.com/clash-verge-rev/clash-verge-rev/releases" },
    { id: "clashx", name: "ClashX", desc: "轻量级的 Mac 代理工具，常驻状态栏，操作简单直接，适合新手快速上手。", img: "img_app.jpg", download: "https://github.com/yichengchen/clashX/releases" },
    { id: "default", name: "Surge Mac", desc: "Mac 平台最强大的网络调试与代理工具，功能极其丰富，但属于付费软件且价格较高。", img: "img_app.jpg", download: "https://nssurge.com/" }
  ],
  ios: [
    { id: "shadowrocket", name: "Shadowrocket", desc: "俗称“小火箭”，iOS 端最普及的代理软件。需使用非国区 Apple ID 在 App Store 付费下载（约 $2.99）。", img: "img_app.jpg", download: "https://apps.apple.com/us/app/shadowrocket/id932747118" },
    { id: "default", name: "Quantumult X", desc: "俗称“圈X”，进阶用户首选，拥有强大的复写、脚本功能和优美的 UI，同样需要外区 ID 下载。", img: "img_app.jpg", download: "https://apps.apple.com/us/app/quantumult-x/id1443988620" },
    { id: "default", name: "Loon", desc: "界面现代、功能全面的 iOS 代理客户端，支持丰富的插件与脚本，适合折腾。", img: "img_app.jpg", download: "https://apps.apple.com/us/app/loon/id1373567447" },
    { id: "default", name: "ClashMi", desc: "免费的 iOS Clash 客户端替代品，如果你不想购买付费软件可以尝试。", img: "img_app.jpg", download: "https://apps.apple.com/us/app/clashmi/id1663032709" }
  ],
  android: [
    { id: "clash-for-android", name: "Clash for Android", desc: "安卓端最经典的 Clash 客户端，由于原作者删库，建议寻找可靠的备份镜像下载使用。", img: "img_app.jpg", download: "https://github.com/Kr328/ClashForAndroid/releases" },
    { id: "v2rayng", name: "v2rayNG", desc: "安卓端使用最广泛的 V2Ray 客户端，支持最新协议，界面简洁，配置简单。", img: "img_app.jpg", download: "https://github.com/2dust/v2rayNG/releases" },
    { id: "default", name: "Surfboard", desc: "冲浪板，完全兼容 Surge 格式配置文件的安卓客户端，设计现代，支持丰富的规则分流。", img: "img_app.jpg", download: "https://github.com/getsurfboard/surfboard/releases" }
  ]
};

function setPlatform(platform, btn) {
  // Update active tab
  document.querySelectorAll('.platform-tab').forEach(t => t.classList.remove('active'));
  if (btn) btn.classList.add('active');
  else document.getElementById('pt' + platform.charAt(0).toUpperCase() + platform.slice(1))?.classList.add('active');

  // Render content
  const clients = tutorials[platform];
  const container = document.getElementById('tutorialContent');
  if (!container || !clients) return;

  container.innerHTML = `<div class="software-grid">` + clients.map((client) => `
    <div class="software-card">
      <div class="soft-img-wrap">
        <img src="${client.img}" alt="${client.name} 界面预览" />
      </div>
      <div class="soft-body">
        <h3 class="soft-title">${client.name}</h3>
        <p class="soft-desc">${client.desc}</p>
        <div class="soft-actions">
          <a href="${client.download}" target="_blank" rel="nofollow noreferrer" class="soft-btn soft-btn-primary">
            <svg viewBox="0 0 20 20" fill="currentColor" class="soft-icon"><path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
            下载客户端
          </a>
          <button class="soft-btn soft-btn-secondary" onclick="location.href='tutorial.html?id=${client.id}'">
            <svg viewBox="0 0 20 20" fill="none" class="soft-icon"><path d="M4 4h12v12H4V4z" stroke="currentColor" stroke-width="2"/><path d="M4 8h12M8 4v12" stroke="currentColor" stroke-width="2"/></svg>
            配置教程
          </button>
        </div>
      </div>
    </div>
  `).join('') + `</div>`;
}

// Initialize tutorial content if on tutorial page
document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('tutorialContent')) {
    setPlatform('windows', document.getElementById('ptWindows'));
  }
  
  // Check hash for direct page navigation
  const hash = window.location.hash.replace('#', '');
  if (hash === 'article' || hash === 'tutorial') {
    switchPage(hash);
  }
});

/* ==================== Navigation ==================== */
function switchPage(page) {
  // Hide all pages
  document.getElementById('pageRank').style.display = 'none';
  document.getElementById('pageArticle').style.display = 'none';
  document.getElementById('pageTutorial').style.display = 'none';

  // Remove active class from all tabs
  document.getElementById('navRank').classList.remove('active');
  document.getElementById('navArticle').classList.remove('active');
  document.getElementById('navTutorial').classList.remove('active');

  // Show target page and activate tab
  let targetId = 'pageRank';
  let tabId = 'navRank';
  
  if (page === 'article') {
    targetId = 'pageArticle';
    tabId = 'navArticle';
  } else if (page === 'tutorial') {
    targetId = 'pageTutorial';
    tabId = 'navTutorial';
  }

  document.getElementById(targetId).style.display = 'block';
  document.getElementById(tabId).classList.add('active');
  
  // Update URL hash for sharing/linking
  window.history.replaceState(null, null, page === 'rank' ? window.location.pathname : '#' + page);
}

function toggleFaq(el) {
  const item = el.closest('.faq-item');
  const answer = item.querySelector('.faq-a');
  
  if (item.classList.contains('open')) {
    item.classList.remove('open');
    answer.style.maxHeight = null;
  } else {
    // Close others
    document.querySelectorAll('.faq-item.open').forEach(openItem => {
      openItem.classList.remove('open');
      openItem.querySelector('.faq-a').style.maxHeight = null;
    });
    item.classList.add('open');
    answer.style.maxHeight = answer.scrollHeight + "px";
  }
}

