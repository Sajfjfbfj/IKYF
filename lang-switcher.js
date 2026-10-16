/**
 * 全日本弓道連盟 サイト多言語翻訳（日英切替）＆ 自動バージョン更新スクリプト
 * ヘッダーやレイアウトのデザインを一切崩さず、メニュー内の既存「English」リンクと連動
 * 英語翻訳時のテキスト重なり（縦書きタイトル、メニュー内のTour/Introduction、テーブル項目等）を完全防止
 * ブラウザの「戻る」「進む」（bfcache / popstate）時にも確実に英語翻訳を維持
 * スマホPWA・ホーム画面Webアプリの自動更新＆キャッシュクリア機能を統合
 */
(function() {
  // 言語状態の判定（Cookieから取得）
  function getLang() {
    var m = document.cookie.match(/(?:^|;)\s*googtrans=([^;]+)/);
    if (m && m[1].indexOf('/en') !== -1) return 'en';
    return 'ja';
  }

  // 英語モードなら即座に html タグにクラスを付与（FOUC・重なり防止）
  if (getLang() === 'en') {
    document.documentElement.classList.add('lang-en');
  }

  // 1. スタイルの動的注入（Google翻訳の余計な枠を完全排除＆英語翻訳時の重なり解消＆トースト通知）
  var css = `
    .goog-te-banner-frame, iframe.skiptranslate { display: none !important; visibility: hidden !important; height: 0 !important; width: 0 !important; }
    body { top: 0px !important; position: static !important; }
    #goog-gt-tt, .goog-te-balloon-frame { display: none !important; }
    .goog-text-highlight { background-color: transparent !important; box-shadow: none !important; }
    #google_translate_element { display: none !important; }
    .util a.lang-active {
      color: var(--accent, #b79be0) !important;
      font-weight: 600;
    }

    /* ===== 英語翻訳時のレイアウト重なり・崩れ防止スタイル ===== */
    /* トップページタイトル（日本語縦書きから英語横書きへ自然に切り替え、capやseasonsとの重なりを防止） */
    html.lang-en .title, html.translated-ltr .title {
      writing-mode: horizontal-tb !important;
      position: absolute !important;
      top: calc(env(safe-area-inset-top,0px) + 13vh) !important;
      right: 7vw !important;
      left: auto !important;
      max-width: min(86vw, 18em) !important;
      font-size: clamp(24px, 4.2vw, 44px) !important;
      line-height: 1.35 !important;
      letter-spacing: .06em !important;
      text-align: right !important;
    }
    @media (max-width: 768px) {
      html.lang-en .title, html.translated-ltr .title {
        top: calc(env(safe-area-inset-top,0px) + 11vh) !important;
        right: 7vw !important;
        left: 7vw !important;
        max-width: none !important;
        text-align: left !important;
        font-size: clamp(22px, 5.5vw, 30px) !important;
      }
      html.lang-en .cap, html.translated-ltr .cap {
        bottom: calc(env(safe-area-inset-bottom,0px) + 4vh) !important;
        left: 7vw !important;
        right: 7vw !important;
        max-width: none !important;
      }
    }

    /* メニュー内（#cur）の英語翻訳時レイアウト調整（Tour / Introduction等の被りを完全防止） */
    html.lang-en .grp.on, html.translated-ltr .grp.on {
      display: grid !important;
      grid-template-columns: minmax(11em, 1.2fr) 2.8fr !important;
      gap: 3vw !important;
    }
    html.lang-en .grp h3, html.translated-ltr .grp h3 {
      font-size: clamp(20px, 2.2vw, 32px) !important;
      letter-spacing: .04em !important;
      line-height: 1.25 !important;
      overflow-wrap: break-word !important;
      word-break: normal !important;
    }
    html.lang-en .grp ul, html.translated-ltr .grp ul {
      columns: 2 !important;
      column-gap: 3vw !important;
    }
    html.lang-en .grp a, html.translated-ltr .grp a {
      font-size: clamp(14px, 1.3vw, 18px) !important;
      letter-spacing: .04em !important;
      line-height: 1.5 !important;
      word-break: normal !important;
      overflow-wrap: break-word !important;
    }
    @media (max-width: 899px) {
      html.lang-en .grp.on, html.translated-ltr .grp.on {
        display: block !important;
      }
      html.lang-en .grp h3, html.translated-ltr .grp h3 {
        font-size: 16px !important;
        letter-spacing: .04em !important;
      }
      html.lang-en .grp ul, html.translated-ltr .grp ul {
        columns: 1 !important;
      }
    }

    /* ギャラリー見出し（縦書きから横書きへ） */
    html.lang-en .lab, html.translated-ltr .lab {
      writing-mode: horizontal-tb !important;
      font-size: clamp(15px, 1.8vw, 20px) !important;
      letter-spacing: .08em !important;
      line-height: 1.4 !important;
      max-width: 11em !important;
      margin-right: 2vw !important;
      text-align: left !important;
    }

    /* 定義リスト（項目名英語化による被り防止） */
    html.lang-en .spec>div, html.translated-ltr .spec>div {
      grid-template-columns: 14em 1fr !important;
    }
    @media (max-width: 760px) {
      html.lang-en .spec>div, html.translated-ltr .spec>div {
        grid-template-columns: 1fr !important;
        gap: .3em !important;
      }
    }

    /* ナビゲーションメニューの英語長文化対応 */
    html.lang-en .nav, html.translated-ltr .nav {
      gap: 1.2em !important;
      font-size: 13px !important;
    }

    /* 更新通知トーストスタイル */
    #appToast {
      position: fixed;
      bottom: 28px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(20, 18, 28, 0.94);
      color: #f3eef8;
      border: 1px solid rgba(183, 155, 224, 0.45);
      border-radius: 999px;
      padding: 9px 22px;
      font-size: 13px;
      letter-spacing: .08em;
      box-shadow: 0 8px 28px rgba(0, 0, 0, 0.6);
      z-index: 9999;
      opacity: 0;
      transition: opacity 0.35s ease;
      pointer-events: none;
      font-family: "Shippori Mincho", "Yu Mincho", serif;
      white-space: nowrap;
    }
  `;
  var style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  // 2. メニュー内のEnglishリンクを検出してイベントをバインド
  function setupMenuLink() {
    var isEn = (getLang() === 'en');
    var links = document.querySelectorAll('.util a');
    var targetLink = null;

    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      var href = a.getAttribute('href') || '';
      var text = (a.textContent || '').trim().toLowerCase();
      if (href.indexOf('english') !== -1 || text === 'english' || text.indexOf('日本語') !== -1) {
        targetLink = a;
        break;
      }
    }

    if (!targetLink) {
      var util = document.querySelector('.util');
      if (util) {
        targetLink = document.createElement('a');
        targetLink.href = '#';
        util.appendChild(targetLink);
      }
    }

    if (targetLink) {
      targetLink.classList.add('notranslate');
      if (isEn) {
        targetLink.textContent = '日本語 (Japanese)';
        targetLink.classList.add('lang-active');
        targetLink.setAttribute('aria-label', '日本語に戻す');
      } else {
        targetLink.textContent = 'English';
        targetLink.setAttribute('aria-label', 'Translate to English');
      }

      targetLink.onclick = function(e) {
        e.preventDefault();
        var host = location.hostname;
        var parts = host.split('.');
        var isDomain = (parts.length > 2);
        var domainStr = isDomain ? '; domain=.' + parts.slice(-2).join('.') : '';
        var sameSite = '; SameSite=Lax';

        if (getLang() === 'en') {
          // 日本語に戻す: Cookieを消去
          var exp = '; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + sameSite;
          document.cookie = 'googtrans=' + exp;
          document.cookie = 'googtrans=' + exp + '; domain=' + host;
          if (isDomain) document.cookie = 'googtrans=' + exp + domainStr;
          document.cookie = 'googtrans=/ja/ja; path=/;' + sameSite;
        } else {
          // 英語に切り替え: 有効期限1年を設定
          var val = '/ja/en';
          var oneYear = '; expires=' + new Date(Date.now() + 365 * 24 * 60 * 60 * 1000).toUTCString();
          document.cookie = 'googtrans=' + val + '; path=/' + oneYear + sameSite;
          document.cookie = 'googtrans=' + val + '; domain=' + host + '; path=/' + oneYear + sameSite;
          if (isDomain) document.cookie = 'googtrans=' + val + domainStr + '; path=/' + oneYear + sameSite;
        }
        location.reload();
      };
    }
  }

  // 3. 自動更新＆キャッシュクリア機構（PWA / ホーム画面アプリ対応）
  function setupAppUpdater() {
    var util = document.querySelector('.util');
    if (util && !document.getElementById('appUpdateBtn')) {
      var updateBtn = document.createElement('a');
      updateBtn.id = 'appUpdateBtn';
      updateBtn.href = '#';
      updateBtn.className = 'notranslate';
      var isEn = (getLang() === 'en');
      updateBtn.textContent = isEn ? 'Update to Latest' : '最新版に更新';
      updateBtn.onclick = function(e) {
        e.preventDefault();
        checkAppVersion(true);
      };
      util.appendChild(updateBtn);
    }

    function showToast(msg) {
      var toast = document.getElementById('appToast');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'appToast';
        toast.className = 'notranslate';
        document.body.appendChild(toast);
      }
      toast.textContent = msg;
      toast.style.opacity = '1';
      setTimeout(function() {
        toast.style.opacity = '0';
      }, 2600);
    }

    function forceReload() {
      var url = new URL(window.location.href);
      url.searchParams.set('_v', Date.now());
      window.location.replace(url.toString());
    }

    function checkAppVersion(isManual) {
      var fetchUrl = '/version.json?_t=' + Date.now();
      fetch(fetchUrl, { cache: 'no-store' })
        .then(function(res) {
          if (!res.ok) throw new Error('Fetch failed');
          return res.json();
        })
        .then(function(data) {
          if (!data || !data.buildId) return;
          var localId = localStorage.getItem('ikyf_build_id');
          if (!localId) {
            localStorage.setItem('ikyf_build_id', data.buildId);
            if (isManual) {
              showToast(getLang() === 'en' ? 'Already up to date' : '既に最新バージョンです');
            }
          } else if (localId !== data.buildId) {
            localStorage.setItem('ikyf_build_id', data.buildId);
            showToast(getLang() === 'en' ? 'Updating to latest version...' : '最新版に更新しています...');
            setTimeout(forceReload, 600);
          } else if (isManual) {
            showToast(getLang() === 'en' ? 'Reloading...' : '最新版を再読み込みします...');
            setTimeout(forceReload, 500);
          }
        })
        .catch(function() {
          if (isManual) {
            forceReload();
          }
        });
    }

    // 起動時のチェック
    checkAppVersion(false);

    // スマホでバックグラウンドから復帰した時（アプリを再度開いた時）に自動チェック
    document.addEventListener('visibilitychange', function() {
      if (document.visibilityState === 'visible') {
        checkAppVersion(false);
      }
    });

    window.addEventListener('pageshow', function() {
      checkAppVersion(false);
    });
  }

  // 4. Google Translate API のロード
  function loadGoogleTranslate() {
    if (document.getElementById("google_translate_element")) return;

    var div = document.createElement("div");
    div.id = "google_translate_element";
    div.style.display = "none";
    document.body.appendChild(div);

    window.googleTranslateElementInit = function() {
      new google.translate.TranslateElement({
        pageLanguage: 'ja',
        includedLanguages: 'en,ja',
        autoDisplay: false
      }, 'google_translate_element');
    };

    var s = document.createElement("script");
    s.src = "https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit";
    s.async = true;
    document.body.appendChild(s);
  }

  // 5. 英語翻訳時の不要な補足語句 "(Japanese archery)" の自動除去
  function cleanTranslations() {
    function cleanText(text) {
      return text.replace(/\s*[\(（]Japanese archery[\)）]/gi, '');
    }

    function cleanNode(node) {
      if (!node) return;
      if (node.nodeType === Node.TEXT_NODE) {
        if (node.nodeValue && /[\(（]Japanese archery[\)）]/i.test(node.nodeValue)) {
          node.nodeValue = cleanText(node.nodeValue);
        }
      } else if (node.nodeType === Node.ELEMENT_NODE) {
        if (node.tagName !== 'SCRIPT' && node.tagName !== 'STYLE') {
          for (var i = 0; i < node.childNodes.length; i++) {
            cleanNode(node.childNodes[i]);
          }
        }
      }
    }

    cleanNode(document.body);

    if (window.MutationObserver && !window._kyudoObserverInitialized) {
      window._kyudoObserverInitialized = true;
      var observer = new MutationObserver(function(mutations) {
        for (var i = 0; i < mutations.length; i++) {
          var m = mutations[i];
          if (m.type === 'characterData') {
            if (m.target && m.target.nodeValue && /[\(（]Japanese archery[\)）]/i.test(m.target.nodeValue)) {
              m.target.nodeValue = cleanText(m.target.nodeValue);
            }
          } else if (m.type === 'childList') {
            for (var j = 0; j < m.addedNodes.length; j++) {
              cleanNode(m.addedNodes[j]);
            }
          }
        }
      });

      observer.observe(document.body, {
        childList: true,
        subtree: true,
        characterData: true
      });
    }
  }

  // 6. 初期化実行
  function init() {
    setupMenuLink();
    setupAppUpdater();
    if (getLang() === 'en') {
      document.documentElement.classList.add('lang-en');
      loadGoogleTranslate();
      cleanTranslations();
      var count = 0;
      var timer = setInterval(function() {
        cleanTranslations();
        count++;
        if (count > 20) clearInterval(timer);
      }, 500);
    } else {
      document.documentElement.classList.remove('lang-en');
    }
  }

  // 7. ブラウザの「戻る」「進む」（bfcache / popstate）対策
  window.addEventListener('pageshow', function(e) {
    var curLang = getLang();
    if (curLang === 'en') {
      document.documentElement.classList.add('lang-en');
      loadGoogleTranslate();
      cleanTranslations();
    } else {
      document.documentElement.classList.remove('lang-en');
    }

    if (e.persisted) {
      var isEn = (curLang === 'en');
      var hasTranslatedClass = document.documentElement.classList.contains('translated-ltr');
      if ((isEn && !hasTranslatedClass) || (!isEn && hasTranslatedClass)) {
        window.location.reload();
      }
    }
  });

  window.addEventListener('popstate', function() {
    if (getLang() === 'en') {
      document.documentElement.classList.add('lang-en');
      loadGoogleTranslate();
      cleanTranslations();
    }
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
