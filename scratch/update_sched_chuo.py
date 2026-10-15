import os
import re
from bs4 import BeautifulSoup

def update_index():
    with open(r"scratch\remote_schedule_chuoshinsa.html", 'r', encoding='utf-8') as f:
        remote_soup = BeautifulSoup(f.read(), 'html.parser')
        
    remote_table = remote_soup.find('table')
    remote_rows = remote_table.find_all('tr')
    
    tbody_rows = []
    
    for i, r in enumerate(remote_rows[1:], 1):
        tds = r.find_all('td')
        if len(tds) < 6:
            continue
        date_text = tds[0].get_text(strip=True)
        name_td = tds[1]
        name_text = name_td.get_text(strip=True)
        name_a = name_td.find('a')
        
        detail_href = name_a.get('href', '') if name_a else ''
        m = re.search(r'chuoshinsa/detail/([^/]+)/?', detail_href)
        slug = m.group(1) if m else ''
        
        venue_text = tds[2].get_text(strip=True)
        
        guidance_a = tds[3].find('a')
        guidance_href = guidance_a.get('href', '') if guidance_a else ''
        if guidance_href.startswith('/'):
            guidance_href = 'https://www.kyudo.jp' + guidance_href
            
        timetable_a = tds[4].find('a')
        timetable_href = timetable_a.get('href', '') if timetable_a else ''
        if timetable_href.startswith('/'):
            timetable_href = 'https://www.kyudo.jp' + timetable_href
            
        result_a = tds[5].find('a')
        result_href = result_a.get('href', '') if result_a else ''
        if result_href.startswith('/'):
            result_href = 'https://www.kyudo.jp' + result_href
            
        td_date = f'<td class="d">{date_text}</td>'
        
        if slug:
            td_name = f'<td><a href="../../chuoshinsa/detail/{slug}/">{name_text}</a></td>'
        else:
            td_name = f'<td>{name_text}</td>'
            
        td_venue = f'<td>{venue_text}</td>'
        
        if guidance_href:
            td_guidance = f'<td><a href="{guidance_href}">実施要項<span class="pdf">PDF</span></a></td>'
        else:
            td_guidance = '<td></td>'
            
        if timetable_href:
            td_timetable = f'<td><a href="{timetable_href}">立会<span class="pdf">PDF</span></a></td>'
        else:
            td_timetable = '<td></td>'
            
        if result_href:
            td_result = f'<td><a href="{result_href}">結果<span class="pdf">PDF</span></a></td>'
        else:
            td_result = '<td></td>'
            
        row_html = f'<tr>{td_date}{td_name}{td_venue}{td_guidance}{td_timetable}{td_result}</tr>'
        tbody_rows.append(row_html)
        
    table_tbody_content = '\n'.join(tbody_rows)
    
    html = f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="全国で開かれる定期の審査会はもちろん、臨時の審査会の日程を発表します。"><meta name="keywords" content="弓道,kyudo,全弓連,全日本弓道連盟,武道,審査,スケジュール,昇段,昇級"><title>中央審査会(年間スケジュール)｜大会・審査情報｜公益財団法人 全日本弓道連盟</title><link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;600&display=swap" rel="stylesheet"><style>
:root{{color-scheme:dark;--bg:#14121c;--ink:#f3eef8;--sub:rgba(243,238,248,.72);--line:rgba(243,238,248,.18);--accent:#b79be0}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:"Shippori Mincho","Yu Mincho",serif;line-height:1.9}}a{{color:inherit;text-decoration:none}}a:hover{{color:var(--accent)}}a:focus-visible{{outline:2px solid var(--accent);outline-offset:4px}}.top{{padding:30px 7vw 24px;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:24px}}.brand b{{display:block;font-size:18px;letter-spacing:.16em}}.brand span{{font:11px Arial,sans-serif;letter-spacing:.12em;color:var(--sub)}}.top nav{{display:flex;gap:24px;flex-wrap:wrap;font-size:13px;letter-spacing:.12em}}.wrap{{width:min(900px,86vw);margin:0 auto;padding:8vh 0 12vh}}.crumb{{font-size:12px;letter-spacing:.1em;color:var(--sub);margin-bottom:8vh}}.crumb span{{padding:0 .7em;color:var(--accent)}}.eyebrow{{font-size:12px;letter-spacing:.22em;color:var(--accent)}}h1{{font-size:clamp(30px,5vw,56px);font-weight:600;line-height:1.5;letter-spacing:.14em;margin:.5em 0 .7em;overflow-wrap:anywhere}}.meta{{display:flex;gap:1.5em;align-items:center;color:var(--sub);font-size:13px;border-bottom:1px solid var(--line);padding-bottom:1.5em}}.summary{{font-size:17px;line-height:2.1;max-width:42em;margin:3em 0 4em}}.materials{{margin-bottom:4em}}.materials h2{{font-size:19px;letter-spacing:.16em;font-weight:600;margin:0 0 1em}}.materials ul{{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}}.materials li{{padding:1em 0;border-bottom:1px solid var(--line)}}.materials ul+.note,.materials .note+.tbl{{margin-top:1.5em}}.note{{font-size:13px;letter-spacing:.08em;color:var(--sub);margin:2.5em 0 1em}}.tbl{{overflow-x:auto;border-top:1px solid var(--line);-webkit-overflow-scrolling:touch}}.tbl table{{width:100%;min-width:780px;border-collapse:collapse;font-size:14px;line-height:1.7}}.tbl th{{text-align:left;font-weight:400;font-size:12px;letter-spacing:.14em;color:var(--sub);padding:.9em .8em;border-bottom:1px solid var(--line);white-space:nowrap}}.tbl td{{padding:1em .8em;border-bottom:1px solid var(--line);vertical-align:top}}.tbl td.d{{white-space:nowrap;color:var(--sub)}}.tbl td a{{display:inline-block}}.tbl td:nth-child(n+4){{white-space:nowrap}}.pdf{{display:inline-block;font:10px Arial,sans-serif;letter-spacing:.1em;line-height:1.6;color:var(--accent);border:1px solid var(--accent);padding:0 .5em;margin-left:.8em;vertical-align:middle}}.tbl .pdf{{margin-left:.5em}}.more{{font-size:13px;letter-spacing:.14em;color:var(--sub);margin-left:1em}}.quiet{{color:var(--sub);font-size:14px}}.source{{margin-top:4em;font-size:13px;color:var(--sub)}}.source a{{border-bottom:1px solid var(--accent);padding-bottom:.2em}}.bottom{{border-top:1px solid var(--line);padding:24px 7vw 42px;color:var(--sub);font-size:12px;display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}}.bottom .links{{display:flex;gap:8px 24px;flex-wrap:wrap}}@media(max-width:650px){{.top{{align-items:flex-start;flex-direction:column}}.top nav{{gap:12px 18px}}.wrap{{padding-top:6vh}}.crumb{{margin-bottom:5vh}}.summary{{font-size:15px}}}}

/* ===== 共通メニューバー（的場の水鏡.html と同一） ===== */
button{{all:unset;cursor:pointer}}
button:focus-visible{{outline:2px solid var(--accent);outline-offset:4px}}
header.site{{position:sticky;top:0;z-index:5;display:flex;justify-content:space-between;align-items:flex-start;gap:20px;padding:calc(env(safe-area-inset-top,0px) + 3vh) 5vw 2vh;background:var(--bg);border-bottom:1px solid var(--line);text-shadow:none;transition:background .3s ease,border-color .3s ease}}header.site.menu-open{{background:transparent;border-bottom-color:transparent;text-shadow:0 1px 16px rgba(20,18,28,.7)}}
header.site .mark b{{display:block;font-size:19px;letter-spacing:.16em;line-height:1.9}}
header.site .mark span{{font:11px "Shippori Mincho","Yu Mincho",serif;letter-spacing:.12em;color:var(--sub)}}
.nav{{display:none;gap:2.2em}}
.nav button{{font-size:15px;letter-spacing:.2em;padding:.5em 0;position:relative;color:var(--ink)}}
.nav button::after{{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:var(--ink);transform:scaleX(0);transform-origin:left;transition:transform .5s cubic-bezier(.2,.8,.2,1)}}
.nav button:hover::after,.nav button.on::after{{transform:scaleX(1)}}
#mb{{font-size:15px;letter-spacing:.3em;padding:.4em 0;border-bottom:1px solid var(--ink)}}
#cur{{position:fixed;z-index:4;top:0;left:0;right:0;max-height:100vh;overflow:auto;visibility:hidden;clip-path:inset(0 0 100% 0);padding:calc(env(safe-area-inset-top,0px) + 13vh) 7vw 6vh;background:repeating-linear-gradient(90deg,rgba(255,255,255,.07) 0 2px,transparent 2px 6.5vw),linear-gradient(#5a4096,#43307a)}}
#cur a:hover{{color:inherit}}
.grp{{display:none}}
.grp.on{{display:grid;grid-template-columns:minmax(9em,1fr) 3fr;gap:4vw}}
.grp h3{{margin:0;font-size:clamp(28px,4vw,52px);font-weight:600;letter-spacing:.18em;line-height:1.3}}
.grp h3 button{{font:inherit;letter-spacing:inherit;cursor:default}}
.grp ul{{list-style:none;margin:0;padding:0;columns:2;column-gap:4vw}}
.grp li{{break-inside:avoid;border-bottom:1px solid rgba(255,255,255,.22)}}
.grp a{{display:flex;align-items:center;gap:.8em;padding:.7em 0;font-size:clamp(16px,1.6vw,21px);letter-spacing:.12em}}
.grp a::after{{content:"";height:1px;width:0;background:#fff;transition:width .45s cubic-bezier(.2,.8,.2,1)}}
.grp a:hover::after,.grp a:focus-visible::after{{width:2.6em}}
.util{{margin-top:5vh;display:flex;gap:1.8em;flex-wrap:wrap;font-size:13px;letter-spacing:.12em;color:rgba(255,255,255,.82)}}
@media (min-width:900px){{.nav{{display:flex}}#mb{{display:none}}}}
@media (max-width:899px){{.grp,.grp.on{{display:block;border-bottom:1px solid rgba(255,255,255,.22)}}.grp h3{{font-size:19px}}.grp h3 button{{display:flex;justify-content:space-between;width:100%;padding:.9em 0;cursor:pointer}}.grp h3 button::after{{content:"＋"}}.grp.on h3 button::after{{content:"－"}}.grp ul{{display:none;columns:1;padding-bottom:.6em}}.grp.on ul{{display:block}}}}
@media (max-width:600px){{header.site .mark b{{font-size:16px}}}}
/* ===== /共通メニューバー ===== */
</style></head><body><header class="site">
  <a class="mark" href="../../../的場の水鏡.html"><b>全日本弓道連盟</b><span>All Nippon Kyudo Federation</span></a>
  <nav class="nav" id="nav" aria-label="メインメニュー"></nav>
  <button id="mb" aria-expanded="false" aria-controls="cur">メニュー</button>
</header>
<div id="cur" aria-label="サイトメニュー"><div id="cw"></div>
  <div class="util"><a href="../../notice/">連盟からのお知らせ</a><a href="../../info/contact.html">お問い合わせ</a><a href="../../info/english.html">English</a><a href="https://www.kyudo-shop.com/">オンラインショップ</a><a href="https://www.youtube.com/channel/UCtZ76XJWUih0kaEYcI06oYQ">YouTube</a><a href="https://x.com/ANKF0522">X</a><a href="https://www.facebook.com/profile.php?id=61564607121764">Facebook</a><a href="https://www.instagram.com/ankf0522?igsh=MXZ2dnJrMDVpbGt5dg==">Instagram</a></div>
</div><main class="wrap"><div class="crumb"><a href="../../index.html">HOME</a><span>›</span>中央審査会(年間スケジュール)</div><p class="eyebrow">大会・審査情報</p><h1>中央審査会(年間スケジュール)</h1><div class="meta"><span>公益財団法人 全日本弓道連盟</span></div><p class="summary">全国で開かれる定期の審査会はもちろん、臨時の審査会の日程を発表します。</p><section class="materials"><h2>令和8年度中央審査会 年間スケジュール</h2><ul><li><a href="https://www.kyudo.jp/pdf/schedule/chuoshinsa/2026_guideline_chuoshinsa.pdf">令和８年度 中央審査会受審にあたって</a></li>
<li><a href="https://www.kyudo.jp/pdf/schedule/chuoshinsa/2025_shinsa_touan.pdf">中央審査会 学科試験答案用紙（指定様式）</a></li>
<li><a href="https://www.kyudo.jp/pdf/documents/application_over6dan_2025.xlsx">審査申込書（称号・六段以上）</a></li>
<li><a href="https://www.kyudo.jp/pdf/documents/application_under5dan_2025.xlsx">審査申込書（級位・五段以下用）</a></li></ul><p class="note">▼審査会名をクリックすると審査会の詳細や関係書類がご確認いただけます。</p><div class="tbl"><table><thead><tr><th>日程</th><th>審査会名</th><th>会場</th><th>実施要項</th><th>進行表</th><th>結果</th></tr></thead><tbody>
{table_tbody_content}
</tbody></table></div><p class="note"><a href="overview.html">中央道場概要と使用日程<span class="more">詳しく見る</span></a></p></section><section class="materials"><h2>年度別スケジュール</h2><ul><li><a href="./">令和8年度中央審査会 年間スケジュール</a></li>
<li><a href="../../category/chuoshinsa/2025chuoshinsa/">令和7年度中央審査会 年間スケジュール</a></li>
<li><a href="../../category/category/chuoshinsa/2024chuoshinsa/">令和6年度中央審査会スケジュール</a></li>
<li><a href="../../category/category/category/chuoshinsa/2023chuoshinsa/">令和5年度中央審査会スケジュール</a></li>
<li><a href="../../category/category/category/category/chuoshinsa/2022chuoshinsa/">令和4年度中央審査会スケジュール</a></li>
<li><a href="../../category/category/category/category/category/chuoshinsa/2021chuoshinsa/">令和3年度中央審査会スケジュール</a></li>
<li><a href="../../category/chuoshinsa/2020chuoshinsa/">令和2年度中央審査会スケジュール</a></li></ul></section><section class="materials"><h2>中央審査会 各種書類</h2><ul><li><a href="https://www.kyudo.jp/pdf/documents/probation_rules.pdf">審査規程および内規<span class="pdf">PDF</span></a></li>
<li><a href="https://www.kyudo.jp/pdf/documents/probation_fee.pdf">審査料・登録料<span class="pdf">PDF</span></a></li>
<li><a href="https://www.kyudo.jp/pdf/documents/probation_gyosha.pdf">審査における行射の要領<span class="pdf">PDF</span></a></li>
<li><a href="https://www.kyudo.jp/pdf/documents/probation_standard.pdf">審査統一基準<span class="pdf">PDF</span></a></li>
<li><a href="https://www.kyudo.jp/pdf/documents/application_rissha.pdf">中央審査会における立射での受審申請について<span class="pdf">PDF</span></a></li>
<li><a href="https://www.kyudo.jp/pdf/documents/rules_rissha.pdf">立射の作法<span class="pdf">PDF</span></a></li></ul></section><section class="materials"><h2>大会・審査情報コンテンツ</h2><ul><li><a href="../taikai/">全国大会<span class="more">詳しく見る</span></a></li>
<li><a href="./">中央審査会<span class="more">詳しく見る</span></a></li>
<li><a href="../region/">地方審査会<span class="more">詳しく見る</span></a></li>
<li><a href="../association/">連合審査会<span class="more">詳しく見る</span></a></li>
<li><a href="../../map/">全国弓道場マップ</a></li></ul></section><p class="source"><a href="https://www.kyudo.jp/schedule/chuoshinsa/">公式サイトの掲載内容を確認する</a></p></main><footer class="bottom"><span>公益財団法人 全日本弓道連盟</span><div class="links"><a href="../../all-pages.html">全ページ一覧</a><a href="../../info/usearrow.html">矢羽の使用に関する準則ならびに関係資料</a><a href="../../info/guidelines.html">倫理に関するガイドラインと相談窓口</a><a href="../../info/personalinfo.html">個人情報保護方針</a><a href="../../info/link.html">リンク</a></div></footer><script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script>
(function(){{
  var K="../..";
  var reduce=matchMedia("(prefers-reduced-motion: reduce)").matches;
  var M=[["弓道の心",[["弓道の心","/howto/"],["弓道の歴史","/howto/history.html"],["射法について","/howto/syaho.html"],["弓道用語辞典","/howto/terminology.html"]]],
   ["見学・入門",[["弓道を始めたい方","/begin/"],["道具について","/begin/tool.html"],["よくある質問","/begin/faq.html"],["上達への道。","/improve/"],["動画（MOVIE）","/movie/"]]],
   ["大会・審査会情報",[["全国大会（年間スケジュール）","/schedule/taikai/"],["中央審査会（年間スケジュール）","/schedule/chuoshinsa/"],["連合審査会（年間スケジュール）","/schedule/association/"],["地方審査会（年間スケジュール）","/schedule/region/"],["資料・申込書","/documents/"]]],
   ["全国弓道場",[["全国弓道場マップ","/map/"],["中央道場概要と使用日程","/schedule/chuoshinsa/overview.html"]]],
   ["全日本弓道連盟について",[["概要","/aboutus/overview.html"],["中期計画","/aboutus/plan.html"],["加盟団体","/aboutus/org.html"],["職員採用案内","/aboutus/recruit.html"],["ブック（刊行物）","/aboutus/book.html"],["公式グッズ","/aboutus/officialgoods.html"],["弓道ショップ（ONLINE SHOP）","https://www.kyudo-shop.com/"]]]];
  var NAV=["弓道の心","見学・入門","大会・審査会","弓道場","連盟について"];
  var cur$=document.getElementById("cur"), cw=document.getElementById("cw"), nav=document.getElementById("nav"), mb=document.getElementById("mb"), hdr$=document.querySelector("header.site")||document.querySelector("header");
  function href(p){{return /^https?:/.test(p)?p:K+p;}}
  cw.innerHTML=M.map(function(g){{return '<section class="grp"><h3><button type="button">'+g[0]+'</button></h3><ul>'+g[1].map(function(l){{return '<li><a href="'+href(l[1])+'">'+l[0]+'</a></li>';}}).join("")+'</ul></section>';}}).join("");
  nav.innerHTML=NAV.map(function(n){{return '<button type="button">'+n+'</button>';}}).join("");
  var grps=cw.querySelectorAll(".grp"), navB=nav.querySelectorAll("button"), isOpen=false, act=-1, tm;
  var desk=function(){{return matchMedia("(min-width:900px)").matches;}};
  var D=function(x){{return reduce?0:x;}};
  function reveal(){{
    if(!isOpen){{isOpen=true; if(hdr$)hdr$.classList.add("menu-open"); cur$.style.visibility="visible"; gsap.to(cur$,{{clipPath:"inset(0 0 0% 0)",duration:D(.7),ease:"power3.out"}});}}
    gsap.fromTo(cur$.querySelectorAll(".grp.on li"),{{y:14,opacity:0}},{{y:0,opacity:1,duration:D(.5),stagger:.04,ease:"power2.out",overwrite:true}});
  }}
  function show(i){{act=i;grps.forEach(function(s,k){{s.classList.toggle("on",k===i);}});navB.forEach(function(b,k){{b.classList.toggle("on",k===i);}});reveal();}}
  function hide(){{
    if(!isOpen)return; isOpen=false; act=-1; if(hdr$)hdr$.classList.remove("menu-open");
    navB.forEach(function(b){{b.classList.remove("on");}}); grps.forEach(function(s){{s.classList.remove("on");}});
    gsap.to(cur$,{{clipPath:"inset(0 0 100% 0)",duration:D(.5),ease:"power3.in",onComplete:function(){{if(!isOpen)cur$.style.visibility="hidden";}}}});
    document.body.style.overflow=""; mb.textContent="メニュー"; mb.setAttribute("aria-expanded","false");
  }}
  navB.forEach(function(b,k){{
    b.addEventListener("mouseenter",function(){{if(desk()){{clearTimeout(tm);show(k);}}}});
    b.addEventListener("click",function(){{if(desk()){{(isOpen&&act===k)?hide():show(k);}}}});
  }});
  [nav,cur$].forEach(function(el){{
    el.addEventListener("mouseenter",function(){{clearTimeout(tm);}});
    el.addEventListener("mouseleave",function(){{if(desk())tm=setTimeout(hide,280);}});
  }});
  mb.onclick=function(){{
    if(isOpen){{hide();return;}}
    grps.forEach(function(s){{s.classList.remove("on");}}); reveal();
    document.body.style.overflow="hidden"; mb.textContent="閉じる"; mb.setAttribute("aria-expanded","true");
  }};
  grps.forEach(function(s){{s.querySelector("button").addEventListener("click",function(){{
    if(desk())return; var o=s.classList.contains("on"); grps.forEach(function(x){{x.classList.remove("on");}}); if(!o)s.classList.add("on");
  }});}});
}})();
</script>
</body></html>'''

    target = r"site-complete\schedule\chuoshinsa\index.html"
    with open(target, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {target} successfully!")

if __name__ == '__main__':
    update_index()
