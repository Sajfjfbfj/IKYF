(() => {
  const scriptUrl = document.currentScript?.src;
  if (!scriptUrl) return;

  const siteRoot = new URL("./", scriptUrl);
  const hrefFor = (path) => new URL(path, siteRoot).href;
  const groups = [
    {
      label: "弓道の心",
      links: [
        ["弓道の心", "howto/index.html"],
        ["弓道の歴史", "howto/history.html"],
        ["射法について", "howto/syaho.html"],
        ["弓道用語辞典", "howto/terminology.html"],
      ],
    },
    {
      label: "見学・入門",
      links: [
        ["弓道を始めたい方", "begin/index.html"],
        ["道具について", "begin/tool.html"],
        ["よくある質問", "begin/faq.html"],
        ["上達への道", "improve/index.html"],
        ["動画（MOVIE）", "movie/index.html"],
      ],
    },
    {
      label: "大会・審査会情報",
      links: [
        ["全国大会", "schedule/taikai/index.html"],
        ["中央審査会", "schedule/chuoshinsa/index.html"],
        ["連合審査会", "schedule/association/index.html"],
        ["地方審査会", "schedule/region/index.html"],
        ["資料・申込書", "documents/index.html"],
      ],
    },
    {
      label: "全国弓道場",
      links: [
        ["全国弓道場マップ", "map/index.html"],
        ["中央道場概要と使用日程", "schedule/chuoshinsa/overview.html"],
      ],
    },
    {
      label: "全日本弓道連盟について",
      links: [
        ["概要", "aboutus/overview.html"],
        ["中期計画", "aboutus/plan.html"],
        ["加盟団体", "aboutus/org.html"],
        ["職員採用案内", "aboutus/recruit.html"],
        ["ブック（刊行物）", "aboutus/book.html"],
        ["公式グッズ", "aboutus/officialgoods.html"],
      ],
    },
  ];
  const utilities = [
    ["連盟からのお知らせ", "https://www.kyudo.jp/notice/"],
    ["お問い合わせ", "https://www.kyudo.jp/info/contact.html"],
    ["English", "https://www.kyudo.jp/info/english.html"],
    ["オンラインショップ", "https://www.kyudo-shop.com/"],
  ];

  const header =
    document.querySelector("header.top") || document.querySelector("body > header");
  if (!header || header.dataset.menuReady === "true") return;

  const brand = header.querySelector("a.brand") || header.querySelector("a[href]");
  if (!brand) return;

  document.body.classList.add("site-menu-enabled");
  header.classList.add("top", "site-menu-header");
  brand.classList.add("brand");

  let nav = header.querySelector("nav");
  if (!nav) {
    for (const child of Array.from(header.children)) {
      if (child !== brand) child.remove();
    }
    nav = document.createElement("nav");
    header.append(nav);
  }
  nav.className = "site-menu-nav";
  nav.setAttribute("aria-label", "メインメニュー");
  nav.replaceChildren();

  const toggle = document.createElement("button");
  toggle.className = "site-menu-toggle";
  toggle.type = "button";
  toggle.textContent = "メニュー";
  toggle.setAttribute("aria-expanded", "false");
  header.append(toggle);

  const panel = document.createElement("div");
  panel.className = "site-menu-panel";
  panel.id = "site-menu-panel";
  panel.setAttribute("aria-label", "サイトメニュー");
  panel.setAttribute("aria-hidden", "true");
  const groupElements = [];

  groups.forEach((group, index) => {
    const navButton = document.createElement("button");
    navButton.type = "button";
    navButton.textContent = group.label;
    navButton.setAttribute("aria-expanded", "false");
    nav.append(navButton);

    const section = document.createElement("section");
    section.className = "site-menu-group";
    const heading = document.createElement("h2");
    const headingButton = document.createElement("button");
    headingButton.className = "site-menu-group-heading";
    headingButton.type = "button";
    headingButton.textContent = group.label;
    headingButton.setAttribute("aria-expanded", "false");
    heading.append(headingButton);

    const list = document.createElement("ul");
    group.links.forEach(([label, path]) => {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = hrefFor(path);
      link.textContent = label;
      item.append(link);
      list.append(item);
    });

    section.append(heading, list);
    panel.append(section);
    groupElements.push({ section, navButton, headingButton, index });
  });

  const utilityList = document.createElement("div");
  utilityList.className = "site-menu-utils";
  utilities.forEach(([label, href]) => {
    const link = document.createElement("a");
    link.href = href;
    link.target = "_blank";
    link.rel = "noopener";
    link.textContent = label;
    utilityList.append(link);
  });
  panel.append(utilityList);
  header.after(panel);

  const isDesktop = () => matchMedia("(min-width: 900px)").matches;
  let isOpen = false;
  let activeIndex = -1;
  let closeTimer;

  function setActive(index) {
    activeIndex = index;
    groupElements.forEach(({ section, navButton, headingButton }, i) => {
      const active = i === index;
      section.classList.toggle("is-active", active);
      section.classList.remove("is-expanded");
      navButton.setAttribute("aria-expanded", String(active));
      headingButton.setAttribute("aria-expanded", "false");
    });
  }

  function openMenu(index = -1) {
    clearTimeout(closeTimer);
    isOpen = true;
    panel.classList.add("is-open");
    panel.setAttribute("aria-hidden", "false");
    toggle.setAttribute("aria-expanded", "true");
    toggle.textContent = "閉じる";
    document.body.style.overflow = isDesktop() ? "" : "hidden";
    if (isDesktop() && index >= 0) setActive(index);
    else if (!isDesktop()) setActive(-1);
  }

  function closeMenu() {
    isOpen = false;
    activeIndex = -1;
    panel.classList.remove("is-open");
    panel.setAttribute("aria-hidden", "true");
    toggle.setAttribute("aria-expanded", "false");
    toggle.textContent = "メニュー";
    document.body.style.overflow = "";
    groupElements.forEach(({ section, navButton, headingButton }) => {
      section.classList.remove("is-active", "is-expanded");
      navButton.setAttribute("aria-expanded", "false");
      headingButton.setAttribute("aria-expanded", "false");
    });
  }

  groupElements.forEach(({ navButton, headingButton, index, section }) => {
    navButton.addEventListener("mouseenter", () => {
      if (isDesktop()) openMenu(index);
    });
    navButton.addEventListener("click", () => {
      if (!isDesktop()) return;
      if (isOpen && activeIndex === index) closeMenu();
      else openMenu(index);
    });
    headingButton.addEventListener("click", () => {
      if (isDesktop()) {
        openMenu(index);
        return;
      }
      const expanded = section.classList.toggle("is-expanded");
      headingButton.setAttribute("aria-expanded", String(expanded));
    });
  });

  toggle.addEventListener("click", () => {
    if (isOpen) closeMenu();
    else openMenu();
  });

  [header, panel].forEach(element => {
    element.addEventListener("mouseenter", () => clearTimeout(closeTimer));
    element.addEventListener("mouseleave", () => {
      if (isDesktop()) closeTimer = setTimeout(closeMenu, 260);
    });
  });

  panel.addEventListener("click", event => {
    if (event.target.closest("a")) closeMenu();
  });
  document.addEventListener("click", event => {
    if (isOpen && !header.contains(event.target) && !panel.contains(event.target)) {
      closeMenu();
    }
  });
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && isOpen) closeMenu();
  });
  window.addEventListener("resize", () => {
    if (isOpen) closeMenu();
  });

  header.dataset.menuReady = "true";
  const main = document.querySelector("main");
  if (main && !main.classList.contains("wrap")) {
    main.classList.add("site-menu-sitemap");
  }
})();
