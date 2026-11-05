# Guía de mantenimiento

Cómo cambiar cosas en la web sin romper nada: dónde está cada texto, cómo sustituir el CV, cómo
añadir un dashboard o un proyecto nuevo y qué comprobar antes de publicar.

---

## 1. Ver la web en tu ordenador

Desde la raíz del repositorio:

```bash
python3 -m http.server 8000 --directory site
```

Abre http://localhost:8000. Para parar el servidor, pulsa Ctrl+C en la terminal.

Abrir `index.html` con doble clic casi funciona, pero algunos navegadores bloquean la fuente
local y el visor de gráficos cuando la web se abre como archivo. Usa el servidor.

---

## 2. Dónde está cada cosa

| Quiero cambiar… | Archivo |
|---|---|
| Textos de la portada en castellano | `site/index.html` |
| Textos de la portada en inglés | `site/en/index.html` |
| Un caso de estudio | `site/proyectos/<proyecto>.html` y su gemelo `site/en/proyectos/<proyecto>.html` |
| Colores, tamaños, espacios | `site/css/styles.css` (los colores están al principio, en `:root`) |
| Menú móvil, visor de gráficos, copiar email, animaciones | `site/js/main.js` |
| Textos de los botones que crea el JavaScript («Copiar email», «Cerrar»…) | `site/js/main.js`, objeto `UI` al principio |
| CV e informes | `site/assets/docs/` |
| Imágenes | `site/assets/img/` |
| Página de error | `site/404.html` (lleva su propio CSS dentro) |
| Datos verificados de los proyectos | `contenido/proyectos/*.md` (no se publica) |

**Regla de oro:** casi todo existe dos veces (castellano e inglés). Si cambias un texto en una
página, cambia también su gemela.

**Reglas de contenido** (resumen de `CLAUDE.md`):
- No inventes cifras. Todo sale de `contenido/`.
- Si algo falta, **no se muestra**: se deja como comentario `<!-- PENDIENTE: … -->` y se apunta en
  `PENDIENTES.md`.
- Las cifras van en formato español en la versión en castellano (`11.237`, `34,5 mil M €`) e
  inglés en la versión inglesa (`11,237`).
- El texto va justificado. Los títulos, etiquetas y botones, no.

---

## 3. Tareas frecuentes

### Sustituir el CV

1. Exporta el PDF **con texto seleccionable** (no como imagen) y llámalo exactamente
   `CV_Javier_Benitez_Escobedo.pdf`.
2. Sustituye el archivo en `site/assets/docs/`.
3. Opcional: los enlaces al CV dicen su peso a los lectores de pantalla («PDF, 473 KB»). Si el
   nuevo pesa muy distinto, busca `473 KB` en las páginas y cámbialo.

Si algún día tienes el CV en inglés, guárdalo como `CV_Javier_Benitez_Escobedo_EN.pdf` y cambia
los enlaces de `site/en/` para que apunten a él.

### Activar un dashboard de Looker Studio

1. En Looker Studio: **Compartir → Insertar informe → Habilitar inserción**. Copia la URL que
   empieza por `https://lookerstudio.google.com/embed/reporting/…`.
2. Comprueba que el informe es público: **Compartir → Cualquier persona con el enlace puede ver**.
3. En la página del caso en castellano, busca el comentario `Dashboard de Looker Studio: oculto…`,
   quita las marcas de comentario (`<!--` y `-->`) y pon tu URL en `src="…"`.
4. La página en inglés no tiene ese comentario: copia el mismo bloque ya activado en el mismo
   sitio (al final de «Findings», antes de «Limitations») y traduce el título («Interactive
   dashboard») y el `title` del `<iframe>`.
5. Borra la línea correspondiente de `PENDIENTES.md`.

### Enlazar un repositorio nuevo (Barcelona o moda)

En la página del caso en castellano, la ficha tiene un aviso `<!-- Código: oculto hasta… -->`.
Sustitúyelo por una fila como esta (cambia la dirección y el detalle):

```html
<div><dt>Código</dt><dd><a href="https://github.com/degallo/NOMBRE" target="_blank" rel="noopener">github.com/degallo/NOMBRE ↗<span class="visually-hidden"> (se abre en una pestaña nueva)</span></a></dd></div>
```

Copia también el botón «Ver el SQL en GitHub» de `hueco-comercial.html` en dos sitios:
- en la ficha (`ficha__actions`);
- en los accesos rápidos de móvil (`case-hero__actions`, el botón «Código en GitHub»).

En la versión inglesa no hay aviso: añade la fila detrás de «Volume», con `Code` y
`(opens in a new tab)`, y los dos botones copiados de `en/proyectos/hueco-comercial.html`.

### Cambiar el CSS o el JavaScript

Después de editar `styles.css` o `main.js`, ejecuta:

```bash
python3 herramientas/subir-version.py
```

Cambia `?v=10` por `?v=11` en todas las páginas, para que ningún navegador muestre la versión
guardada en caché.

### Añadir un proyecto nuevo

1. **Contenido:** crea `contenido/proyectos/05-<nombre>.md` con las cifras verificadas (copia la
   estructura de los otros).
2. **Imágenes:** exporta las páginas del informe a WebP de 1600×900 como
   `site/assets/img/proyectos/<carpeta>/pagina-NN.webp`. Después:

   ```bash
   python3 herramientas/preparar-imagenes.py site/assets/img/proyectos/<carpeta> <slug>
   ```

   Crea las versiones de 800 y 1200 px y la imagen para redes. Necesita Pillow:
   `python3 -m pip install pillow`.
3. **PDF:** el informe va en `site/assets/docs/`.
4. **Página del caso:** duplica `site/proyectos/hueco-comercial.html` como `<slug>.html` y
   cambia, de arriba abajo:
   - el `<head>`: título, descripción, `canonical`, `hreflang` (los tres), `og:*` y los datos
     estructurados (`application/ld+json`);
   - la cabecera: el enlace «EN» a la versión inglesa;
   - el hero: etiqueta, `h1`, subtítulo, accesos rápidos y portada;
   - la ficha, el índice, el resumen y el cuerpo;
   - la navegación «Anterior / Siguiente» al final.
5. **Versión inglesa:** igual, en `site/en/proyectos/<slug>.html` (duplica la inglesa de otro caso).
6. **Portada:** copia un bloque `<article class="project">` en `site/index.html` y en
   `site/en/index.html`. Si usas una ilustración propia, va en `assets/img/proyectos/iconos/`.
7. **Navegación:** actualiza «Anterior / Siguiente» del caso que quede antes y del que quede
   después, para que el nuevo entre en el ciclo.
8. **Mapa del sitio:** añade las dos URL nuevas en `site/sitemap.xml`, copiando un bloque `<url>`.
9. Comprueba y publica (apartado 4).

### Añadir analítica sin cookies (GoatCounter)

1. Crea una cuenta gratuita en https://www.goatcounter.com (por ejemplo, `javibenitez`).
2. Pega esto justo antes de `</body>` en las 10 páginas, cambiando `javibenitez` por tu nombre
   de cuenta:

   ```html
   <script data-goatcounter="https://javibenitez.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
   ```

No usa cookies, así que no necesitas aviso de cookies. Si usas las cabeceras de seguridad de
`documentacion/plantillas/_headers`, añade `https://gc.zgo.at` a `script-src` y
`https://javibenitez.goatcounter.com` a `connect-src` e `img-src`.

### Que se vea Helvetica también en Windows y Android

Hoy la web pide «Helvetica Neue / Helvetica / Arial»: en Mac e iPhone se ve Helvetica, y en
Windows y Android, Arial, que es casi igual. Helvetica no se puede servir como fuente web sin
licencia. Hay dos opciones:

1. **Licencia de Helvetica Now** para web (Monotype, de pago).
2. **Un clon libre: TeX Gyre Heros** (licencia GUST, gratuita).
   1. Descárgalo de https://www.ctan.org/pkg/tex-gyre-heros.
   2. Convierte `texgyreheros-regular.otf` a WOFF2 (por ejemplo, con https://transfonter.org) y
      guárdalo en `site/assets/fonts/`.
   3. Añade esto al principio de `styles.css`:

      ```css
      @font-face {
        font-family: "Helvetica Web";
        /* Primero la Helvetica del sistema (Mac, iPhone); si no existe, el clon */
        src: local("Helvetica Neue"), local("HelveticaNeue"), local("Helvetica"),
             url("../assets/fonts/texgyreheros-regular.woff2") format("woff2");
        font-weight: 400 600; font-display: swap;
      }
      ```

   4. Cambia `--font-display` en `:root` por
      `"Helvetica Web", "Helvetica Neue", Helvetica, Arial, sans-serif`.
   5. Sube la versión con `python3 herramientas/subir-version.py`.

### Cabeceras de seguridad: recalcular la huella

Solo si publicas en Netlify o Cloudflare Pages con `_headers` y cambias el `<script>` de una
línea del `<head>`:

```bash
python3 herramientas/huella-csp.py
```

Copia la huella que imprime en `script-src` del archivo `_headers`.

---

## 4. Antes de publicar

- [ ] Comprueba la web:

  ```bash
  python3 herramientas/comprobar-web.py
  ```

  Tiene que terminar en «Todo correcto».
- [ ] Mírala en local en móvil (DevTools → icono de móvil, 375 px) y en escritorio.
- [ ] Si tocaste CSS o JS, sube la versión:

  ```bash
  python3 herramientas/subir-version.py
  ```

- [ ] Si cambiaste textos, cambia también la versión en el otro idioma.
- [ ] Nada a medias a la vista: lo que falte, como `<!-- PENDIENTE: … -->` y en `PENDIENTES.md`.

## 5. Publicar

Haz commit y push a `main`. GitHub Actions publica `site/` en un par de minutos (pestaña
**Actions** del repositorio). Si no ves el cambio, recarga sin caché: Ctrl+F5 en Windows,
Cmd+Shift+R en Mac.

---

## 6. Problemas frecuentes

| Síntoma | Causa probable | Solución |
|---|---|---|
| He cambiado el CSS y no se ve | Caché del navegador | `herramientas/subir-version.py` y publicar; Ctrl+F5 |
| Una imagen no aparece | Ruta mal escrita o con mayúsculas distintas (GitHub Pages distingue `Foto.webp` de `foto.webp`) | `herramientas/comprobar-web.py` te dice cuál |
| El visor de gráficos no se abre | El enlace no termina en `.webp` o no está dentro de `<figure class="figure">` | Copia la estructura de otra figura |
| LinkedIn muestra una vista previa antigua | LinkedIn guarda la imagen unos días | https://www.linkedin.com/post-inspector/ y pulsa «Inspect» |
| La web sale en blanco en algunas secciones | Error de JavaScript que impide revelar el contenido | Abre la consola (F12) y mira el error; mientras tanto, la web se muestra completa si `main.js` no carga |
| El texto justificado deja huecos en móvil | Es inherente al justificado en columnas estrechas | Se mitiga con frases sin palabras muy largas; los guiones ya están activados |
