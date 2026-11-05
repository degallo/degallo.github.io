# CLAUDE.md — Portfolio de Javier Benítez Escobedo

Este archivo es el contexto permanente del proyecto. Léelo entero antes de tocar nada.
El encargo concreto de la primera sesión está en `PROMPT_INICIAL.md`.

## 1. Qué es esto

Portfolio web personal de **Javier Benítez Escobedo (Javi)**, estudiante de último curso del
Grado en Marketing e Investigación de Mercados (Universidad de Granada) que busca **prácticas
curriculares en análisis de datos** a partir de febrero de 2027 (vía Ícaro, sin fecha de fin).

Todavía no tiene experiencia laboral como analista. Lo que tiene son **cuatro proyectos de
análisis hechos por su cuenta** con datos públicos reales, y eso es lo que el portfolio vende.

## 2. Para quién es (lo más importante)

El lector es un **reclutador, un responsable de RR. HH. o un jefe de equipo de datos/marketing**
que mira el portfolio entre 30 segundos y 3 minutos. **No es un cliente.** Por tanto:

- Nada de "servicios", "precios", "contrátame", "Book a call" ni "consulta gratuita".
- Las llamadas a la acción son: **Ver proyectos · Descargar CV · Escribirme por email · LinkedIn · GitHub**.
- En los primeros 5 segundos tiene que quedar claro: quién es, qué busca (prácticas en análisis
  de datos, a partir de febrero de 2027) y por qué merece la pena seguir leyendo (proyectos con datos reales).
- Cada proyecto se presenta como un **caso de estudio**: pregunta de negocio → datos → método →
  hallazgo → qué haría una empresa con ello → limitaciones. Los reclutadores de datos valoran
  sobre todo el **criterio**: saber qué preguntar, desconfiar de un dato llamativo y decir
  claramente qué no resuelve el análisis. Esa es la ventaja diferencial de Javi; hay que lucirla.

## 3. Reglas de contenido

1. **Todo en español** (una versión en inglés puede venir después; deja el código preparado
   para ello, por ejemplo con los textos agrupados y fáciles de duplicar).
2. **No inventes nada.** Ni cifras, ni experiencia, ni testimonios, ni empresas, ni
   porcentajes tipo "320 % de mejora". Todo dato sale de `contenido/`. Si algo falta, **no lo muestres en la web**:
   deja un comentario HTML `<!-- PENDIENTE: … -->` en su sitio y apúntalo en `PENDIENTES.md`
   (decisión de Javi, nov. 2026: un reclutador no debe ver huecos a medias).
3. Las cifras se copian **exactamente** como están en `contenido/proyectos/*.md` (con formato
   español: punto de miles, coma decimal, `€` detrás con espacio fino o normal).
4. Tono: directo, concreto, sin adjetivos vacíos ("apasionado", "proactivo", "orientado a
   resultados"). Mejor una cifra que un adjetivo.
5. Datos personales: publica **solo** email, LinkedIn y GitHub. **No publiques la dirección
   postal.** El teléfono solo si Javi lo confirma en `PENDIENTES.md`.
6. Sin emojis.

## 4. Stack técnico

- **HTML + CSS + JavaScript sin frameworks ni paso de build.** Se publica tal cual en GitHub Pages.
- La web vive en **`site/`**. El workflow `.github/workflows/pages.yml` publica solo esa carpeta.
  `contenido/` y `referencias/` son material de trabajo y no se publican.
- Rutas **relativas** siempre (`assets/...`, no `/assets/...`), para que funcione igual en local
  y en Pages.
- Estructura sugerida:
  ```
  site/
  ├── index.html                 ← portada (one-page con secciones)
  ├── proyectos/
  │   ├── hueco-comercial.html   ← un caso de estudio por proyecto
  │   ├── ilusion-descuento.html
  │   ├── posicionamiento-moda.html
  │   └── alquiler-turistico-barcelona.html
  ├── css/styles.css
  ├── js/main.js
  ├── assets/ (img/, docs/)      ← ya existe, no cambies los nombres
  ├── 404.html
  └── favicon.svg
  ```
- Fuentes: Google Fonts (máximo 2 familias). Sin jQuery. Animaciones con CSS e
  `IntersectionObserver`; nada de librerías pesadas. Respeta `prefers-reduced-motion`.
- Rendimiento: imágenes `webp` con `width`/`height` y `loading="lazy"` (salvo la del hero).
  Objetivo Lighthouse ≥ 90 en las cuatro categorías.
- Accesibilidad: HTML semántico, un solo `h1` por página, contraste AA, foco visible, `alt`
  descriptivos en todas las imágenes de gráficos (di qué muestra el gráfico, no "gráfico").
- SEO básico: `title` y `meta description` por página, Open Graph (imagen: portada del
  proyecto o la foto), `lang="es"`, datos estructurados `Person` en la portada.
- Responsive de verdad: probar a 375 px, 768 px y 1440 px. Nada de scroll horizontal.

## 5. Dirección de diseño

Lee `referencias/DISENO.md` y mira las capturas de `referencias/capturas/`.
Resumen: estructura y aire de la plantilla **Finox** (minimalista, monocromo, tipografía
enorme, tarjetas redondeadas, etiquetas en píldora, pie oscuro con el nombre gigante),
**con el acento terracota de su CV** para que CV y web parezcan de la misma persona.

**Finox es una plantilla comercial de Webflow: úsala solo como inspiración.** No copies su
HTML, su CSS, sus imágenes ni sus SVG. Escribe todo desde cero.

## 6. Cómo trabajar con Javi

- Habla en español, tono cercano y conciso.
- Prefiere **iterar**: enséñale una primera versión funcional pronto y mejora por rondas.
- Explica brevemente los porqués de las decisiones de diseño y código; está aprendiendo.
- Si algo del contenido no se sostiene o es mejorable para un reclutador, díselo con claridad.
- Haz commits pequeños y con mensajes en español que digan qué cambia.
- Antes de dar algo por terminado: revisa en móvil y escritorio, comprueba que todos los
  enlaces y descargas funcionan y que no queda ningún `[PENDIENTE]` sin listar.
