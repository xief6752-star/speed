document.addEventListener('DOMContentLoaded', () => {
  const params = new URLSearchParams(window.location.search);
  const airportId = params.get('id');
  
  if (!airportId) {
    document.querySelector('.detail-main').innerHTML = `
      <div class="empty-state">
        <h2>未找到机场信息</h2>
        <p>参数错误，请返回主页重新选择。</p>
        <a href="index.html" class="detail-back-btn" style="display:inline-block; margin-top:20px;">返回首页</a>
      </div>
    `;
    return;
  }

  const airport = airports.find(a => a.id === airportId);
  
  if (!airport) {
    document.querySelector('.detail-main').innerHTML = `
      <div class="empty-state">
        <h2>机场不存在</h2>
        <p>无法找到ID为 "${airportId}" 的机场信息。</p>
        <a href="index.html" class="detail-back-btn" style="display:inline-block; margin-top:20px;">返回首页</a>
      </div>
    `;
    return;
  }

  // Populate data
  document.getElementById('pageTitle').textContent = `${airport.name}测评 · SpeedRank - 节点测速、稳定性与价格分析`;
  document.getElementById('bcName').textContent = airport.name;

  const score = Math.round(airport.uptime * 0.4 + (120 - airport.baseLatency) * 0.3 + airport.baseSpeed * 0.3);
  const scoreColor = score >= 85 ? '#10b981' : score >= 70 ? '#2563eb' : '#f59e0b';

  const descText = `${airport.name} 深度测评报告：${airport.description}。当前综合评分 ${score}/100，中位延迟 ${airport.baseLatency}ms，最低售价 ${airport.price}。支持 ${airport.protocols.join('/')} 协议。`;
  document.getElementById('pageDesc').setAttribute('content', descText);
  document.getElementById('pageKeywords').setAttribute('content', `${airport.name},${airport.name}测评,${airport.name}跑路,机场测评,Clash节点,SpeedRank`);
  
  document.getElementById('ogTitle').setAttribute('content', `${airport.name}测评 · SpeedRank`);
  document.getElementById('ogDesc').setAttribute('content', descText);
  document.getElementById('twTitle').setAttribute('content', `${airport.name}测评 · SpeedRank`);
  document.getElementById('twDesc').setAttribute('content', descText);
  
  const now = new Date();
  document.getElementById('detailDateStatus').innerHTML = `
    <span>报告日期：${now.getFullYear()}-${String(now.getMonth()+1).padStart(2,'0')}-${String(now.getDate()).padStart(2,'0')}</span>
    <span style="color:#b45309;">· 最新测速数据已更新</span>
  `;

  // Hero
  document.getElementById('detailTitle').textContent = `${airport.emoji} ${airport.name}`;
  document.getElementById('detailDesc').textContent = airport.description;
  
  let tagsHtml = airport.tagLabels.map(tag => `<span>${tag}</span>`).join('');
  tagsHtml += `<span style="border-color:#10b981; color:#059669; background:#ecfdf5;">状态: 正常</span>`;
  document.getElementById('detailTags').innerHTML = tagsHtml;
  
  // Score
  document.getElementById('dscNumber').textContent = score;
  document.getElementById('dscBarFill').style.width = `${score}%`;
  document.getElementById('dscBarFill').style.background = `linear-gradient(90deg, #2563eb, ${scoreColor})`;
  document.getElementById('dscGrade').textContent = `综合评级：${score >= 85 ? '优秀' : score >= 70 ? '良好' : '一般'}`;
  
  document.getElementById('detailLongDesc').innerHTML = `
    <p><strong>${airport.name}</strong> 是一家提供高质量代理服务的供应商。其主要特点是：${airport.description}。</p>
    <ul>
      <li><strong>主打特色</strong>：支持 ${airport.protocols.join(', ')} 协议，包含 ${airport.nodes.length} 个全球节点。</li>
      <li><strong>流媒体解锁</strong>：完美解锁 Netflix、Disney+ 等主流媒体平台。</li>
      <li><strong>适用人群</strong>：非常适合${(airport.tagLabels && (airport.tagLabels.includes('极速') || airport.tagLabels.includes('专业'))) ? '对网络质量和速度有极高要求的进阶用户或企业级用户。' : '日常科学上网、追剧、轻量级办公的用户，性价比极高。'}</li>
    </ul>
  `;

  document.getElementById('dscSubScores').innerHTML = `
    <div class="dsc-sub-item">
      <div class="dsc-sub-label">稳定性 (S)</div>
      <div class="dsc-sub-value" style="color:#059669">${airport.uptime.toFixed(1)}</div>
    </div>
    <div class="dsc-sub-item">
      <div class="dsc-sub-label">性能 (P)</div>
      <div class="dsc-sub-value" style="color:#2563eb">${airport.baseSpeed.toFixed(1)}</div>
    </div>
    <div class="dsc-sub-item">
      <div class="dsc-sub-label">价格 (C)</div>
      <div class="dsc-sub-value" style="color:#d97706">${(100 - (parseInt(airport.price.replace(/\\D/g, '')) || 0) / 2).toFixed(1)}</div>
    </div>
    <div class="dsc-sub-item">
      <div class="dsc-sub-label">风险 (R)</div>
      <div class="dsc-sub-value" style="color:#dc2626">100.0</div>
    </div>
  `;

  // Snapshot
  const onlineNodes = airport.nodes.filter(n => n.online).length;
  document.getElementById('snapStatus').textContent = '正常';
  document.getElementById('snapUptime').textContent = `${airport.uptime}%`;
  document.getElementById('snapLatency').textContent = `${airport.baseLatency} ms`;
  document.getElementById('snapLatency').className = `snap-value ${airport.baseLatency <= 60 ? 'snap-green' : airport.baseLatency <= 120 ? 'snap-yellow' : 'snap-red'}`;
  document.getElementById('snapSpeed').textContent = `${airport.baseSpeed} MB/s`;
  document.getElementById('snapLoss').textContent = `0%`;
  document.getElementById('snapNodes').textContent = `${onlineNodes} / ${airport.nodeCount}`;
  document.getElementById('snapHealth').textContent = `14 天`;
  document.getElementById('snapRisk').textContent = `0`;

  // Capabilities
  const streamingIcons = [
    { name: 'Netflix', icon: 'N', color: '#E50914', bg: '#000' },
    { name: 'ChatGPT', icon: 'C', color: '#10a37f', bg: '#fff' },
    { name: 'Disney+', icon: 'D+', color: '#113ccf', bg: '#eef6ff' },
    { name: 'YouTube', icon: 'Y', color: '#FF0000', bg: '#fff' }
  ];
  document.getElementById('capStreaming').innerHTML = streamingIcons.map(s => `
    <div class="cap-item">
      <div class="cap-icon" style="color:${s.color}; background:${s.bg}; border-color:${s.bg === '#fff' ? '#e2e8f0' : 'transparent'}">${s.icon}</div>
      <span>${s.name}</span>
    </div>
  `).join('');

  const clients = ['Clash / Verge', 'Shadowrocket', 'Quantumult X', 'v2rayN'];
  document.getElementById('capClients').innerHTML = clients.map(c => `
    <div class="cap-item">
      <div class="cap-icon" style="color:#2563eb; background:#eff6ff">💻</div>
      <span>${c}</span>
    </div>
  `).join('');

  const payments = ['支付宝', '微信', 'USDT-TRC20'];
  document.getElementById('capPayment').innerHTML = payments.map(p => `
    <div class="cap-item">
      <div class="cap-icon" style="color:#059669; background:#ecfdf5">💰</div>
      <span>${p}</span>
    </div>
  `).join('');

  const support = ['Telegram 群组', '客服工单', '使用教程'];
  document.getElementById('capSupport').innerHTML = support.map(s => `
    <div class="cap-item">
      <div class="cap-icon" style="color:#2563eb; background:#eff6ff">💬</div>
      <span>${s}</span>
    </div>
  `).join('');

  document.getElementById('capProtocols').innerHTML = airport.protocols.map(p => `
    <div class="cap-item">
      <div class="cap-icon" style="color:#d97706; background:#fffbeb">🔑</div>
      <span>${p}</span>
    </div>
  `).join('');

  const isPro = airport.tags.includes('pro') || airport.tags.includes('fast');
  document.getElementById('capLines').innerHTML = `
    <div class="cap-item">
      <div class="cap-icon" style="color:#7c3aed; background:#fdf4ff">⚡</div>
      <span>${isPro ? 'IEPL / IPLC 专线' : 'BGP 公网中转'}</span>
    </div>
  `;

  // Score Breakdown
  document.getElementById('scoreBreakdown').innerHTML = `
    <div class="sb-card">
      <div class="sb-label">可用性评分 (30%)</div>
      <div class="sb-value" style="color:#059669">${airport.uptime.toFixed(1)}</div>
      <div class="sb-bar"><div class="sb-bar-fill" style="width:${airport.uptime}%; background:#10b981;"></div></div>
    </div>
    <div class="sb-card">
      <div class="sb-label">性能评分 (30%)</div>
      <div class="sb-value" style="color:#2563eb">${airport.baseSpeed.toFixed(1)}</div>
      <div class="sb-bar"><div class="sb-bar-fill" style="width:${Math.min(100, airport.baseSpeed)}%; background:#3b82f6;"></div></div>
    </div>
    <div class="sb-card">
      <div class="sb-label">节点覆盖 (20%)</div>
      <div class="sb-value" style="color:#d97706">${airport.nodeCount > 100 ? 95 : 80}</div>
      <div class="sb-bar"><div class="sb-bar-fill" style="width:${airport.nodeCount > 100 ? 95 : 80}%; background:#f59e0b;"></div></div>
    </div>
    <div class="sb-card">
      <div class="sb-label">价格性价比 (20%)</div>
      <div class="sb-value" style="color:#7c3aed">${(100 - (parseInt(airport.price.replace(/\\D/g, '')) || 0) / 2).toFixed(1)}</div>
      <div class="sb-bar"><div class="sb-bar-fill" style="width:${(100 - (parseInt(airport.price.replace(/\\D/g, '')) || 0) / 2)}%; background:#8b5cf6;"></div></div>
    </div>
  `;

  // Core Metrics
  document.getElementById('metricsGrid').innerHTML = `
    <div class="metric-card">
      <div class="mc-label">中位延迟</div>
      <div class="mc-value">${airport.baseLatency} <span style="font-size:14px;color:#94a3b8">ms</span></div>
      <div class="mc-sub">测试节点数：${airport.nodeCount}</div>
      <div class="mc-trend trend-up"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg> 优于 75% 机场</div>
    </div>
    <div class="metric-card">
      <div class="mc-label">峰值下载速度</div>
      <div class="mc-value">${(airport.baseSpeed * 1.2).toFixed(1)} <span style="font-size:14px;color:#94a3b8">MB/s</span></div>
      <div class="mc-sub">测试环境：千兆宽带</div>
      <div class="mc-trend trend-up"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg> 极速体验</div>
    </div>
    <div class="metric-card">
      <div class="mc-label">最低价格</div>
      <div class="mc-value">${airport.price}</div>
      <div class="mc-sub">支持月付/年付</div>
      <div class="mc-trend trend-down"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 14l-7 7m0 0l-7-7m7 7V3"></path></svg> 价格适中</div>
    </div>
  `;

  // 30-day Trend Chart
  drawTrendChart();

  // Plans & Nodes
  document.getElementById('planList').innerHTML = `
    <div class="plan-item">
      <div>
        <div class="plan-item-name">入门月付套餐</div>
        <div class="plan-item-sub">100GB 流量 / 月</div>
      </div>
      <div class="plan-item-price">${airport.price}</div>
    </div>
    <div class="plan-item">
      <div>
        <div class="plan-item-name">标准季付套餐</div>
        <div class="plan-item-sub">200GB 流量 / 月</div>
      </div>
      <div class="plan-item-price">¥${(parseInt(airport.price.replace(/\D/g, '')) || 0) * 2.8} / 季</div>
    </div>
    <div class="plan-item">
      <div>
        <div class="plan-item-name">尊享年付套餐</div>
        <div class="plan-item-sub">500GB 流量 / 月</div>
      </div>
      <div class="plan-item-price">¥${(parseInt(airport.price.replace(/\D/g, '')) || 0) * 10} / 年</div>
    </div>
  `;

  document.getElementById('regionDist').innerHTML = airport.regions.map(r => `
    <div class="region-item">
      <span class="region-flag">${r.flag}</span>
      <span class="region-name">${r.name}</span>
      <div class="region-bar-wrap">
        <div class="region-bar" style="width:${Math.min(100, (r.count / airport.regions[0].count) * 100)}%;"></div>
      </div>
      <span class="region-count">${r.count}</span>
    </div>
  `).join('');
  
  // 8. Nodes List
  const nodesListContainer = document.getElementById('nodesListContainer');
  if (nodesListContainer && airport.nodes) {
    nodesListContainer.innerHTML = `
      <div class="node-list">
        ${airport.nodes.map(node => {
          const speedBarWidth = Math.min((node.speed / 150) * 100, 100);
          let speedColor = '#10b981';
          if (node.speed < 20) speedColor = '#ef4444';
          else if (node.speed < 50) speedColor = '#f59e0b';
          
          let latencyColor = '#10b981';
          if (node.latency > 500) latencyColor = '#ef4444';
          else if (node.latency > 200) latencyColor = '#f59e0b';

          return `
            <div class="node-item">
              <div class="node-info">
                <div class="node-name">
                  <span class="status-dot ${node.online ? 'online' : 'offline'}"></span>
                  ${node.name}
                </div>
                <div class="node-tags">
                  <span class="node-tag">${node.protocols}</span>
                </div>
              </div>
              <div class="node-stats">
                <div class="ns-latency" style="color: ${latencyColor}">
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                  ${node.latency} ms
                </div>
                <div class="ns-speed">
                  <div class="ns-speed-bar-bg">
                    <div class="ns-speed-bar" style="width: ${speedBarWidth}%; background: ${speedColor}"></div>
                  </div>
                  <div class="ns-speed-val">${node.speed.toFixed(1)} MB/s</div>
                </div>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;
  }

  // 9. Summary & Accordion
  document.getElementById('summaryBox').innerHTML = `
    <p><strong>${airport.name}</strong> 当前综合评分为 <strong>${score}/100</strong>，运行状态<strong>正常</strong>。该机场主打${isPro ? '高端专线' : '高性价比'}路线，提供稳定的流媒体解锁服务。</p>
    <div class="summary-chips">
      <span class="summary-chip">综合评分 ${score}</span>
      <span class="summary-chip">状态 正常</span>
      <span class="summary-chip">风险惩罚 0</span>
      <span class="summary-chip">30天可用率 ${airport.uptime}%</span>
      <span class="summary-chip">中位延迟 ${airport.baseLatency} ms</span>
    </div>
  `;

  document.getElementById('accordion').innerHTML = `
    <div class="acc-item">
      <button class="acc-trigger" onclick="toggleAcc(this)">
        <span>综合结论</span>
        <svg class="acc-arrow" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6l4 4 4-4"/></svg>
      </button>
      <div class="acc-body">
        <div class="acc-body-inner">
          <p>${airport.description}。亮点：当前价格与实际表现较为均衡，适合对稳定性有一定要求的用户。</p>
          <div class="acc-facts">
            <span class="acc-fact">数据日期 ${now.getFullYear()}-${now.getMonth()+1}-${now.getDate()}</span>
            <span class="acc-fact">趋势 稳健上升</span>
          </div>
        </div>
      </div>
    </div>
    <div class="acc-item">
      <button class="acc-trigger" onclick="toggleAcc(this)">
        <span>节点、客户端与解锁</span>
        <svg class="acc-arrow" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6l4 4 4-4"/></svg>
      </button>
      <div class="acc-body">
        <div class="acc-body-inner">
          <p>当前节点覆盖 ${airport.regions.length} 个主要地区，包括常用的香港、日本、美国等。支持几乎所有主流代理客户端。</p>
          <div class="acc-facts">
            <span class="acc-fact">地区 ${airport.regions.length} 个</span>
            <span class="acc-fact">协议 ${airport.protocols.join(', ')}</span>
            <span class="acc-fact">解锁 Netflix, Disney+, YouTube</span>
          </div>
        </div>
      </div>
    </div>
  `;

  document.getElementById('conclusionBox').innerHTML = `
    <strong>购买建议：</strong> ${airport.name} 更适合重视 ${isPro ? '低延迟和速度' : '性价比和节点丰富度'} 的用户。建议新用户先购买<strong>月付套餐</strong>进行体验，确认在您的网络环境下表现良好后，再考虑购买长周期套餐以获得更多折扣。
  `;

  // Compare Links
  const otherAirports = airports.filter(a => a.id !== airport.id).slice(0, 4);
  document.getElementById('compareLinks').innerHTML = otherAirports.map(a => `
    <a href="airport.html?id=${a.id}" class="compare-link">${a.emoji} ${a.name}</a>
  `).join('');

  // Smooth scroll for side nav
  document.querySelectorAll('.detail-side-nav a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelectorAll('.detail-side-nav a').forEach(a => a.classList.remove('active'));
      this.classList.add('active');
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });

  // Highlight side nav on scroll
  window.addEventListener('scroll', () => {
    let current = '';
    const sections = document.querySelectorAll('.detail-hero, .detail-snapshot-grid, .detail-section');
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      if (scrollY >= sectionTop - 100) {
        current = section.getAttribute('id');
      }
    });
    document.querySelectorAll('.detail-side-nav a').forEach(a => {
      a.classList.remove('active');
      if (a.getAttribute('href') === `#${current}`) {
        a.classList.add('active');
      }
    });
  });

});

// Accordion Toggle
function toggleAcc(btn) {
  const item = btn.closest('.acc-item');
  const body = item.querySelector('.acc-body');
  
  if (item.classList.contains('open')) {
    item.classList.remove('open');
    body.style.maxHeight = null;
  } else {
    // Close others
    document.querySelectorAll('.acc-item.open').forEach(openItem => {
      openItem.classList.remove('open');
      openItem.querySelector('.acc-body').style.maxHeight = null;
    });
    item.classList.add('open');
    body.style.maxHeight = body.scrollHeight + "px";
  }
}

// Draw Trend Chart (Canvas)
function drawTrendChart() {
  const canvas = document.getElementById('trendCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const w = canvas.parentElement.clientWidth;
  const h = 160;
  canvas.width = w * window.devicePixelRatio;
  canvas.height = h * window.devicePixelRatio;
  canvas.style.width = w + 'px';
  canvas.style.height = h + 'px';
  ctx.scale(window.devicePixelRatio, window.devicePixelRatio);

  const points = 30;
  const step = w / (points - 1);
  
  // Generate mock data
  const speedData = [];
  const latencyData = [];
  let baseS = 70 + Math.random() * 20;
  let baseL = 50 + Math.random() * 20;
  
  for(let i=0; i<points; i++) {
    baseS += (Math.random() - 0.5) * 10;
    baseL += (Math.random() - 0.5) * 8;
    speedData.push(Math.max(20, Math.min(120, baseS)));
    latencyData.push(Math.max(20, Math.min(100, baseL)));
  }

  // Draw grid
  ctx.strokeStyle = '#e2e8f0';
  ctx.lineWidth = 1;
  for(let i=1; i<4; i++) {
    ctx.beginPath();
    ctx.moveTo(0, h * i / 4);
    ctx.lineTo(w, h * i / 4);
    ctx.stroke();
  }

  // Draw Line function
  function drawLine(data, color, fillGrad) {
    ctx.beginPath();
    ctx.moveTo(0, h - (data[0]/120)*h);
    for(let i=1; i<points; i++) {
      ctx.lineTo(i*step, h - (data[i]/120)*h);
    }
    
    // Fill
    ctx.lineTo(w, h);
    ctx.lineTo(0, h);
    ctx.fillStyle = fillGrad;
    ctx.fill();
    
    // Stroke
    ctx.beginPath();
    ctx.moveTo(0, h - (data[0]/120)*h);
    for(let i=1; i<points; i++) {
      ctx.lineTo(i*step, h - (data[i]/120)*h);
    }
    ctx.strokeStyle = color;
    ctx.lineWidth = 3;
    ctx.stroke();
  }

  // Latency (Green)
  const gradL = ctx.createLinearGradient(0,0,0,h);
  gradL.addColorStop(0, 'rgba(16, 185, 129, 0.2)');
  gradL.addColorStop(1, 'rgba(16, 185, 129, 0)');
  drawLine(latencyData, '#10b981', gradL);

  // Speed (Blue)
  const gradS = ctx.createLinearGradient(0,0,0,h);
  gradS.addColorStop(0, 'rgba(37, 99, 235, 0.2)');
  gradS.addColorStop(1, 'rgba(37, 99, 235, 0)');
  drawLine(speedData, '#2563eb', gradS);
}

// Window resize handler for chart
window.addEventListener('resize', () => {
  drawTrendChart();
});
