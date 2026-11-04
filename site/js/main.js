/* Portfolio · Javier Benítez Escobedo
   JS mínimo: menú móvil, cabecera al hacer scroll, apariciones con
   IntersectionObserver y sección activa en la navegación.
   La web funciona igual sin JS (todo el contenido está en el HTML). */

(function () {
  'use strict';

  // Textos de la interfaz agrupados aquí para una futura versión en inglés.
  var UI = {
    es: { menu: 'Menú', close: 'Cerrar' },
    en: { menu: 'Menu', close: 'Close' }
  };
  var lang = (document.documentElement.lang || 'es').slice(0, 2);
  var t = UI[lang] || UI.es;

  var root = document.documentElement;
  root.classList.add('js');

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
