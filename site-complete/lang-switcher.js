/**
 * 全日本弓道連盟 サイト多言語翻訳（日英切替）スクリプト
 * ヘッダーやレイアウトのデザインを一切崩さず、メニュー内の既存「English」リンクと連動
 */
(function() {
  // 1. スタイルの動的注入（Google翻訳の余計な枠を完全排除）
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
  `;
  var style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  // 2. 言語状態の判定（Cookieから取得）
  function getLang() {
    var m = document.cookie.match(/(?:^|;)\s*googtrans=([^;]+)/);
    if (m && m[1].indexOf('/en') !== -1) return 'en';
    return 'ja';
  }

  // 3. メニュー内のEnglishリンクを検出してイベントをバインド
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

        if (getLang() === 'en') {
          // 日本語に戻す: Cookieを消去
          var exp = '; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
          document.cookie = 'googtrans=' + exp;
          document.cookie = 'googtrans=' + exp + '; domain=' + host;
          if (isDomain) document.cookie = 'googtrans=' + exp + domainStr;
          document.cookie = 'googtrans=/ja/ja; path=/;';
        } else {
          // 英語に切り替え
          var val = '/ja/en';
          document.cookie = 'googtrans=' + val + '; path=/;';
          document.cookie = 'googtrans=' + val + '; domain=' + host + '; path=/;';
          if (isDomain) document.cookie = 'googtrans=' + val + domainStr + '; path=/;';
        }
        location.reload();
      };
    }
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

  function init() {
    setupMenuLink();
    if (getLang() === 'en') {
      loadGoogleTranslate();
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
