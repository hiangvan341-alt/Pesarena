(function(){
  const page=document.querySelector('[data-lb3-page]');
  if(!page) return;
  const openButton=page.querySelector('[data-lb3-open]');
  const againButton=page.querySelector('[data-lb3-open-again]');
  const resultPanel=page.querySelector('[data-lb3-result]');
  const resultGrid=page.querySelector('[data-lb3-result-grid]');
  const resultNote=page.querySelector('[data-lb3-result-note]');
  const openingLink=page.querySelector('[data-lb3-opening-link]');
  const errorBox=page.querySelector('[data-lb3-error]');
  const balanceNode=page.querySelector('[data-lb3-balance]');
  const previewMode=page.dataset.previewMode==='1';
  const formatter=new Intl.NumberFormat('vi-VN');

  function requestId(){
    if(window.crypto&&crypto.randomUUID) return crypto.randomUUID();
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g,c=>{
      const r=Math.random()*16|0,v=c==='x'?r:(r&3|8);return v.toString(16);
    });
  }
  function escapeHtml(value){
    return String(value??'').replace(/[&<>'"]/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[ch]));
  }
  function showError(message){
    errorBox.textContent=message||'Không thể mở Lucky Box lúc này.';
    errorBox.hidden=false;
    window.setTimeout(()=>{errorBox.hidden=true;},5000);
  }
  function rewardCard(reward,index){
    const amount=Number(reward.reward_amount||0);
    const duplicate=Number(reward.duplicate_conversion||0);
    const rarity=reward.rarity_label||reward.reward_rarity||reward.rarity||'Phần thưởng';
    const image=reward.image_url||'';
    return `<article class="lb3-result-card rarity-${escapeHtml(reward.reward_rarity||reward.rarity||'common')}">
      ${image?`<img src="${escapeHtml(image)}" alt="${escapeHtml(reward.reward_name||'Phần thưởng')}">`:''}
      <small>Ô ${escapeHtml(reward.reward_slot||reward.slot||index+1)} · ${escapeHtml(rarity)}</small>
      <h3>${escapeHtml(reward.reward_name||'Phần thưởng')}</h3>
      ${amount?`<strong>${formatter.format(amount)} Zcoin</strong>`:''}
      ${duplicate?`<p>Đã quy đổi vật phẩm trùng: ${formatter.format(duplicate)} Zcoin</p>`:''}
    </article>`;
  }
  async function openBox(){
    if(!openButton||openButton.disabled) return;
    if(!previewMode){
      const price=Number(page.dataset.openPrice||0);
      if(!window.confirm(`Mở Lucky Box với ${formatter.format(price)} Zcoin?`)) return;
    }
    openButton.disabled=true;
    if(againButton) againButton.disabled=true;
    errorBox.hidden=true;
    try{
      const payload=previewMode
        ?{rate_version_id:page.dataset.rateVersionId}
        :{request_id:requestId(),box_code:page.dataset.boxCode};
      const response=await fetch(page.dataset.openUrl,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
      const data=await response.json().catch(()=>({ok:false,message:'Server không trả về dữ liệu hợp lệ.'}));
      if(!response.ok||!data.ok) throw new Error(data.message||'Không thể mở Lucky Box.');
      const rewards=Array.isArray(data.rewards)?data.rewards:[];
      resultGrid.innerHTML=rewards.map(rewardCard).join('');
      resultNote.textContent=previewMode?'Kết quả mô phỏng · Không thay đổi dữ liệu':`Rate Version ${data.rate_version||'-'}`;
      resultPanel.hidden=false;
      resultPanel.scrollIntoView({behavior:'smooth',block:'start'});
      if(!previewMode&&balanceNode&&Number.isFinite(Number(data.balance_after))){
        balanceNode.textContent=`${formatter.format(Number(data.balance_after))} Zcoin`;
        document.querySelectorAll('.topbar-zcoin strong').forEach(node=>{node.textContent=formatter.format(Number(data.balance_after));});
      }
      if(openingLink){
        if(!previewMode&&data.opening_id){openingLink.href=`/lucky-box/openings/${encodeURIComponent(data.opening_id)}`;openingLink.hidden=false;}
        else{openingLink.href='/lucky-box/history';openingLink.textContent='Lịch sử Lucky Box';}
      }
    }catch(error){showError(error.message);}
    finally{openButton.disabled=false;if(againButton) againButton.disabled=false;}
  }
  openButton?.addEventListener('click',openBox);
  againButton?.addEventListener('click',openBox);
})();
