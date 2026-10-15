// Header navigation: Services dropdown (desktop) and full-screen menu (mobile).
(function () {
  var trigger = document.querySelector('.nav-trigger');
  var toggle = document.querySelector('.menu-toggle');
  var menu = document.getElementById('mobile-menu');
  var hoverTimer;

  function setMega(open) {
    if (trigger) trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  if (trigger) {
    var item = trigger.parentElement;
    var hoverOpenedAt = 0;
    trigger.addEventListener('click', function () {
      // A click right after hover-opening should not immediately close it again
      if (Date.now() - hoverOpenedAt < 600) return;
      setMega(trigger.getAttribute('aria-expanded') !== 'true');
    });
    // Open on hover for mouse users, with a short delay on leave so it doesn't flicker
    item.addEventListener('mouseenter', function () {
      if (!window.matchMedia('(hover: hover)').matches) return;
      clearTimeout(hoverTimer);
      if (trigger.getAttribute('aria-expanded') !== 'true') { hoverOpenedAt = Date.now(); setMega(true); }
    });
    item.addEventListener('mouseleave', function () {
      if (window.matchMedia('(hover: hover)').matches) { hoverTimer = setTimeout(function () { setMega(false); }, 160); }
    });
    item.addEventListener('focusout', function (e) {
      if (!item.contains(e.relatedTarget)) setMega(false);
    });
  }

  function setMenu(open) {
    if (!toggle || !menu) return;
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    menu.hidden = !open;
    document.body.classList.toggle('menu-open', open);
  }

  if (toggle) {
    toggle.addEventListener('click', function () {
      setMenu(toggle.getAttribute('aria-expanded') !== 'true');
    });
    // Close after following an in-page link such as /#services
    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) setMenu(false);
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 960) setMenu(false);
    });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (trigger && trigger.getAttribute('aria-expanded') === 'true') { setMega(false); trigger.focus(); }
    if (toggle && toggle.getAttribute('aria-expanded') === 'true') { setMenu(false); toggle.focus(); }
  });

  document.addEventListener('click', function (e) {
    if (trigger && !trigger.parentElement.contains(e.target)) setMega(false);
  });
})();

// Subtle motion: content eases in as it scrolls into view, the header gains a
// shadow once the page scrolls, and the hero dot field drifts slightly.
// Everything is skipped when the visitor prefers reduced motion.
(function () {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var header = document.querySelector('.site-header');
  var hero = document.querySelector('.hero');
  var ticking = false;

  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle('scrolled', y > 8);
    if (hero && y < hero.offsetHeight) hero.style.setProperty('--drift', (y * 0.18).toFixed(1) + 'px');
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  if (!('IntersectionObserver' in window)) return;

  // Section text and cards below the hero. Grids reveal card by card.
  var selector = [
    'main section:not(.hero) > .wrap > :not(.grid):not(.steps):not(.about-split):not(.contact-grid):not(.checks):not(.faq)',
    'main section:not(.hero) .about-split > div > *',
    'main section:not(.hero) .grid > *',
    'main section:not(.hero) .steps > *',
    'main section:not(.hero) .stats > *',
    'main section:not(.hero) .checks > li',
    'main section:not(.hero) .faq > details'
  ].join(',');
  var items = Array.prototype.filter.call(document.querySelectorAll(selector), function (el) {
    // Only hide what starts below the fold, so nothing visible on load ever blinks
    return el.getBoundingClientRect().top > window.innerHeight * 0.92;
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('in');
      io.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -8% 0px' });

  items.forEach(function (el) {
    // Stagger siblings in a row of cards or a list
    var parent = el.parentElement;
    var isGroup = parent.matches('.grid, .steps, .stats, .checks, .faq');
    if (isGroup) {
      var i = Array.prototype.indexOf.call(parent.children, el);
      el.style.setProperty('--delay', ((i % 3) * 90) + 'ms');
    }
    el.classList.add('reveal');
    io.observe(el);
  });
})();
