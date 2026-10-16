/**
 * 全日本弓道連盟 サイト多言語翻訳（日英切替）スクリプト
 * Google Translate Element を活用し、デザインを崩さずワンタップで翻訳・復帰
 */
(function() {
  // 1. スタイルの動的注入（Google翻訳の余計な枠を非表示にし、ダークテーマの切り替えボタンを整形）
  var css = `
    .goog-te-banner-frame, iframe.skiptranslate { display: none !important; }
    body { top: 0px !important; position: static !important; }
    #goog-gt-tt, .goog-te-balloon-frame { display: none !important; }
    .goog-text-highlight { background-color: transparent !important; box-shadow: none !important; }
    #google_translate_element { display: none !important; }

    .header-tools {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }
    .lang-btn {
      font-family: "Shippori Mincho", "Yu Mincho", serif;
      font-size: 13px;
      letter-spacing: .15em;
      padding: .28em .75em;
      border: 1px solid var(--line, rgba(243,238,248,.18));
      border-radius: 999px;
      color: var(--ink, #f3eef8);
      background: rgba(255,255,255,.06);
      transition: all .3s ease;
      cursor: pointer;
      white-space: nowrap;
      text-shadow: none;
      line-height: 1.5;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }
    .lang-btn:hover {
      border-color: var(--accent, #b79be0);
      color: var(--accent, #b79be0);
      background: rgba(183,155,224,.15);
    }
    @media (max-width: 600px) {
      .lang-btn {
        font-size: 11px;
        padding: .2em .6em;
      }
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

  // 3. ヘッダーに切替ボタンを自動挿入
  function injectButton() {
    if (document.getElementById("langToggle")) return;
    var mb = document.getElementById("mb");
    if (!mb) return;

    var btn = document.createElement("button");
    btn.id = "langToggle";
    btn.className = "lang-btn notranslate";
    btn.type = "button";

    var isEn = (getLang() === 'en');
    btn.textContent = isEn ? "JP / 日本語" : "EN / 英語";
    btn.setAttribute("aria-label", isEn ? "日本語に戻す" : "Switch to English");

    btn.onclick = function(e) {
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
        // 念のため /ja/ja もセット
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

    // mb と横並びにするラッパーを作成
    var parent = mb.parentNode;
    var wrapper = document.createElement("div");
    wrapper.className = "header-tools";
    parent.insertBefore(wrapper, mb);
    wrapper.appendChild(btn);
    wrapper.appendChild(mb);
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

  // 5. 初期化実行
  function init() {
    injectButton();
    // 英語が選択されている場合、または翻訳Cookieが存在する場合にGoogle Translateをロード
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
