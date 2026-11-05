/* Portfolio · Javier Benítez Escobedo
   JS mínimo: menú móvil, cabecera al hacer scroll, apariciones con
   IntersectionObserver y sección activa en la navegación.
   La web funciona igual sin JS (todo el contenido está en el HTML). */

(function () {
  'use strict';

  // Señal para el <script> del <head>: si main.js no llegara a ejecutarse, allí se
  // retira la clase .js y todo el contenido queda visible sin animaciones.
  window.__jbReady = true;

  // Textos de la interfaz, en los dos idiomas.
  var UI = {
    es: { menu: 'Menú', close: 'Cerrar', viewer: 'Gráfico ampliado', full: 'Abrir a tamaño completo',
          copy: 'Copiar email', copied: 'Email copiado', copyFail: 'Cópialo a mano:' },
    en: { menu: 'Menu', close: 'Close', viewer: 'Enlarged chart', full: 'Open full size',
          copy: 'Copy email', copied: 'Email copied', copyFail: 'Copy it manually:' }
  };
  var lang = (document.documentElement.lang || 'es').slice(0, 2);
  var t = UI[lang] || UI.es;

  var root = document.documentElement;
  root.classList.add('js');

  // ---- Portada: el nombre entra letra a letra ----
  // Cada letra es un <span class="ch"> con su índice (--i) para escalonar la
  // animación en CSS. El h1 conserva su texto en aria-label y las letras se
  // ocultan a lectores de pantalla. Con movimiento reducido no se divide nada.
  var heroName = document.querySelector('.hero__name');
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (heroName && !reduceMotion) {
    var n = 0;
    heroName.setAttribute('aria-label', Array.prototype.map.call(heroName.children, function (l) {
      return l.textContent.trim();
    }).join(' '));
    Array.prototype.forEach.call(heroName.children, function (line) {
      var words = line.textContent.trim().split(/\s+/);
      line.textContent = '';
      line.setAttribute('aria-hidden', 'true');
      words.forEach(function (word, wi) {
        var w = document.createElement('span');
        w.className = 'w';
        Array.prototype.forEach.call(word, function (chr) {
          var c = document.createElement('span');
          c.className = 'ch';
          c.textContent = chr;
          c.style.setProperty('--i', n++);
          w.appendChild(c);
        });
        line.appendChild(w);
        if (wi < words.length - 1) line.appendChild(document.createTextNode(' '));
      });
    });
    heroName.classList.add('is-split');
  }

  // ---- Cabecera: borde al hacer scroll ----
  var header = document.querySelector('.site-header');
  function onScroll() {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 8);
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // ---- Menú móvil ----
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('nav');
  function setMenu(open) {
    if (!toggle || !nav) return;
    nav.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.textContent = open ? t.close : t.menu;
  }
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      setMenu(toggle.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setMenu(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setMenu(false);
    });
  }

  // ---- Año del pie ----
  var year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();

  // ---- Visor de gráficos (casos de estudio) ----
  // Sin JS, el enlace abre la imagen grande como siempre. Con JS, se abre encima de
  // la página en un <dialog>: Esc o clic fuera para cerrar, y el foco vuelve al gráfico.
  var figLinks = document.querySelectorAll('.figure a[href$=".webp"]');
  if (figLinks.length && typeof HTMLDialogElement === 'function') {
    var dlg, lbImg, lbCap, lbOpen, lastLink = null;
    // El visor se construye la primera vez que se abre (así no hay nada vacío en la página)
    var buildViewer = function () {
      dlg = document.createElement('dialog');
      dlg.className = 'lightbox';
      dlg.setAttribute('aria-label', t.viewer);
      dlg.innerHTML =
        '<div class="lightbox__bar">' +
          '<a class="btn btn--sm lightbox__open" target="_blank" rel="noopener"></a>' +
          '<button type="button" class="btn btn--sm lightbox__close" autofocus></button>' +   // al abrir, el foco va a «Cerrar»
        '</div>' +
        '<figure class="lightbox__fig"><img alt=""><figcaption class="lightbox__cap"></figcaption></figure>';
      document.body.appendChild(dlg);
      lbImg = dlg.querySelector('img');
      lbCap = dlg.querySelector('figcaption');
      lbOpen = dlg.querySelector('.lightbox__open');
      var lbClose = dlg.querySelector('.lightbox__close');
      lbOpen.textContent = t.full;
      lbClose.textContent = t.close;
      lbClose.addEventListener('click', function () { dlg.close(); });
      dlg.addEventListener('click', function (e) {
        if (e.target === dlg || e.target.classList.contains('lightbox__fig')) dlg.close();
      });
      dlg.addEventListener('close', function () {
        lbImg.removeAttribute('src');
        if (lastLink) lastLink.focus();
      });
    };
    Array.prototype.forEach.call(figLinks, function (a) {
      a.addEventListener('click', function (e) {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return; // abrir en pestaña nueva sigue funcionando
        e.preventDefault();
        if (!dlg) buildViewer();
        lastLink = a;
        var thumb = a.querySelector('img');
        var fc = a.closest('figure') && a.closest('figure').querySelector('figcaption');
        lbImg.src = a.href;
        lbImg.alt = thumb ? thumb.alt : '';
        lbCap.innerHTML = fc ? fc.innerHTML : '';
        lbOpen.href = a.href;
        dlg.showModal();
      });
    });
  }

  // ---- Copiar el email (bloque de contacto) ----
  var mail = document.querySelector('.cta__actions a[href^="mailto:"]');
  if (mail && navigator.clipboard && window.isSecureContext) {
    var address = mail.getAttribute('href').replace('mailto:', '');
    var row = document.createElement('div');
    row.className = 'copy-email-row';
    row.innerHTML = '<button type="button" class="copy-email"></button><span class="copy-email__status" role="status" aria-live="polite"></span>';
    var copyBtn = row.querySelector('button');
    var copyStatus = row.querySelector('span');
    copyBtn.textContent = t.copy;
    mail.parentNode.insertAdjacentElement('afterend', row);
    var copyTimer;
    copyBtn.addEventListener('click', function () {
      navigator.clipboard.writeText(address).then(function () {
        copyStatus.textContent = t.copied;
      }, function () {
        copyStatus.textContent = t.copyFail + ' ' + address;
      });
      clearTimeout(copyTimer);
      copyTimer = setTimeout(function () { copyStatus.textContent = ''; }, 3000);
    });
  }

  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('is-in'); });
    return;
  }

  // ---- Apariciones suaves ----
  var revealer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-in');
        revealer.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  document.querySelectorAll('.reveal, .funnel').forEach(function (el) { revealer.observe(el); });

  // ---- Sección activa en la navegación (portada y ficha de cada caso) ----
  var links = Array.prototype.slice.call(document.querySelectorAll('[data-spy] a[href*="#"]'));
  var targets = links
    .map(function (a) { return document.getElementById(a.getAttribute('href').split('#')[1]); })
    .filter(Boolean);
  // El hero no está en el menú: al volver arriba se limpia el resaltado.
  var top = document.getElementById('inicio');
  if (top && targets.length) targets.push(top);
  if (targets.length) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        links.forEach(function (a) {
          var on = a.getAttribute('href').split('#')[1] === entry.target.id;
          if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    targets.forEach(function (el) { spy.observe(el); });
  }
})();
