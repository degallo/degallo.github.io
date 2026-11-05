# Guía de migración del portfolio

Todo lo necesario para llevar la web a otro dominio o a otro alojamiento sin perder nada.
Está escrita para hacerla tú mismo, paso a paso. Si algo falla, el apartado 9 explica cómo
volver atrás.

---

## 1. Lo que hay que saber antes de empezar

**La web es estática:** solo HTML, CSS, JavaScript, imágenes y PDF. No tiene base de datos, ni
servidor propio, ni paso de compilación. Migrarla consiste en **copiar la carpeta `site/`** a
otro sitio y apuntar el dominio.

**Qué depende del dominio** (y lo cambia solo `herramientas/cambiar-dominio.py`):

| Dónde | Para qué |
|---|---|
| `<link rel="canonical">` y `hreflang` en cada página | Le dicen a Google cuál es la dirección buena y cuál es la versión en el otro idioma |
| `og:url`, `og:image` | La vista previa al compartir en LinkedIn, WhatsApp o correo |
| Datos estructurados (`application/ld+json`) | La ficha de «persona» y de cada caso para buscadores |
| `sitemap.xml` y `robots.txt` | El mapa del sitio para Google |

**Lo que no depende del dominio:** todos los enlaces internos, imágenes, CSS, JS y PDF usan
rutas **relativas** (`assets/...`, `../css/...`), así que funcionan igual en cualquier dominio
y en cualquier subcarpeta. La única excepción es `site/404.html`, que usa rutas desde la raíz
(`/`) porque GitHub Pages la sirve en cualquier ruta inexistente.

**Inventario** (unos 11 MB y 125 archivos):

```
site/
├── index.html, en/index.html          ← portada en castellano e inglés
├── proyectos/*.html, en/proyectos/*   ← los cuatro casos de estudio (ES y EN)
├── 404.html                           ← página de error (bilingüe)
├── css/styles.css · js/main.js        ← un solo CSS y un solo JS
├── assets/fonts/                      ← Montserrat autoalojada (licencia OFL incluida)
├── assets/img/                        ← retrato, logos, ilustraciones, páginas de los informes, og/
├── assets/docs/                       ← CV e informes en PDF
├── favicon.svg · apple-touch-icon.png
└── robots.txt · sitemap.xml
```

**Terceros:** ninguno. La web no carga nada de otros servidores: ni fuentes de Google, ni
analítica, ni librerías. Puedes migrarla a cualquier sitio sin dar de alta servicios externos.

---

## 2. Antes de migrar: copia de seguridad

1. Marca la versión actual con una etiqueta, para poder volver a ella con un comando:

   ```bash
   git tag -a v1.0 -m "Portfolio publicado en degallo.github.io"
   ```

   ```bash
   git push origin v1.0
   ```

2. Opcional: en GitHub, **Code → Download ZIP** y guárdalo fuera del ordenador (Drive, USB).

---

## 3. ¿Qué opción elijo?

| Opción | Para qué | Coste | Dificultad |
|---|---|---|---|
| **A. GitHub Pages + dominio propio** | Lo recomendado: no cambia nada salvo la dirección | Solo el dominio (~10 €/año) | Baja |
| **B. Netlify** | Si quieres formularios, vistas previas por rama o cabeceras de seguridad | Gratis | Baja |
| **C. Cloudflare Pages** | La más rápida en toda Europa; cabeceras y analítica sin cookies incluidas | Gratis | Baja |
| **D. Vercel** | Parecida a Netlify | Gratis (uso personal) | Baja |
| **E. Hosting tradicional** (Hostinger, IONOS, SiteGround…) | Si ya pagas uno o quieres correo con tu dominio en el mismo sitio | 2–8 €/mes | Media |
| **F. Pasarla a un CMS** (WordPress, Webflow, Framer…) | Solo si quieres editarla sin código | Variable | Alta: no es una migración, es rehacerla |

Mi recomendación: **A**. Es la que menos cambia: sigues publicando con un `git push` y GitHub
redirige automáticamente `degallo.github.io` al dominio nuevo.

---

## 4. Opción A — Dominio propio en GitHub Pages (recomendada)

**Tiempo:** unos 20 minutos, más hasta 24 h de espera a que el DNS y el certificado se activen.

1. **Compra el dominio** en cualquier registrador: Namecheap, Porkbun, Dinahosting, IONOS,
   Cloudflare Registrar… Ideas: `javierbenitez.es`, `javierbenitezescobedo.com`.
2. **Verifica el dominio en GitHub** para que nadie pueda usarlo en su cuenta: en GitHub, tu foto →
   **Settings → Pages → Add a domain**. Te pedirá crear un registro **TXT** en el DNS; créalo en
   el panel del registrador y pulsa **Verify**.
3. **Crea los registros DNS** en el registrador:

   | Tipo | Nombre | Valor |
   |---|---|---|
   | A | `@` | `185.199.108.153` |
   | A | `@` | `185.199.109.153` |
   | A | `@` | `185.199.110.153` |
   | A | `@` | `185.199.111.153` |
   | AAAA | `@` | `2606:50c0:8000::153` |
   | AAAA | `@` | `2606:50c0:8001::153` |
   | AAAA | `@` | `2606:50c0:8002::153` |
   | AAAA | `@` | `2606:50c0:8003::153` |
   | CNAME | `www` | `degallo.github.io` |

   Comprueba que estas IP siguen siendo las vigentes en la documentación oficial:
   https://docs.github.com/es/pages/configuring-a-custom-domain-for-your-github-pages-site
4. **Configura el dominio en el repositorio:** `degallo/degallo.github.io` → **Settings → Pages →
   Custom domain** → escribe `javierbenitez.es` → **Save**. Como la web se publica con GitHub
   Actions, **no hace falta** crear un archivo `CNAME` (con Actions, GitHub lo ignora).
5. Cuando GitHub muestre el dominio como válido (puede tardar), marca **Enforce HTTPS**.
6. **Cambia el dominio en la web** y comprueba que todo sigue en orden:

   ```bash
   python3 herramientas/cambiar-dominio.py https://javierbenitez.es/
   ```

   ```bash
   python3 herramientas/cambiar-dominio.py https://javierbenitez.es/ --aplicar
   ```

   ```bash
   python3 herramientas/comprobar-web.py
   ```

   El primero solo simula y te dice cuántos cambios hará; el segundo los aplica.
7. Publica con commit y push a `main`. Al terminar, `https://degallo.github.io/` redirigirá solo
   a `https://javierbenitez.es/`.
8. Sigue con el apartado 7 (después de migrar).

---

## 5. Opciones B, C y D — Netlify, Cloudflare Pages o Vercel

Las tres funcionan igual: conectas el repositorio de GitHub y cada `git push` publica la web.
**No hay comando de compilación** y la carpeta que se publica es **`site`**.

### B. Netlify

1. https://app.netlify.com → **Add new site → Import an existing project → GitHub** → elige
   `degallo.github.io`.
2. **Build command:** vacío · **Publish directory:** `site` → **Deploy**.
3. Copia `documentacion/plantillas/netlify.toml` a la raíz del repositorio y
   `documentacion/plantillas/_headers` dentro de `site/`. Dan caché eficiente y cabeceras de
   seguridad, ya probadas con la web.
4. **Domain management → Add a domain** y sigue sus instrucciones de DNS.
5. Cambia el dominio en la web con `cambiar-dominio.py` (paso 6 de la opción A).

Alternativa sin GitHub: https://app.netlify.com/drop y arrastra la carpeta `site/`. Solo para
probar: cada cambio habría que volver a arrastrarlo.

### C. Cloudflare Pages

1. https://dash.cloudflare.com → **Workers & Pages → Create → Pages → Connect to Git** → elige
   el repositorio.
2. **Framework preset:** None · **Build command:** vacío · **Build output directory:** `site`.
3. Copia `documentacion/plantillas/_headers` dentro de `site/`.
4. **Custom domains → Set up a domain.** Si el dominio está en Cloudflare, se configura solo.
5. Opcional: **Web Analytics** de Cloudflare, sin cookies y gratis.
6. Cambia el dominio en la web con `cambiar-dominio.py`.

### D. Vercel

1. https://vercel.com/new → importa el repositorio.
2. **Framework Preset:** Other · **Output Directory:** `site` · **Build Command:** vacío.
3. Copia `documentacion/plantillas/vercel.json` a la raíz del repositorio.
4. **Settings → Domains** y añade el tuyo.
5. Cambia el dominio en la web con `cambiar-dominio.py`.

**Si dejas GitHub Pages por una de estas,** desactívalo en **Settings → Pages** o convierte
`degallo.github.io` en una redirección (apartado 8) para no tener dos copias publicadas.

---

## 6. Opción E — Hosting tradicional (cPanel, Plesk o panel propio)

1. Cambia primero el dominio en la web, en tu ordenador:

   ```bash
   python3 herramientas/cambiar-dominio.py https://javierbenitez.es/ --aplicar
   ```

   ```bash
   python3 herramientas/comprobar-web.py
   ```

2. En el panel del hosting, activa el **certificado SSL gratuito** (Let's Encrypt).
3. Sube el **contenido** de `site/` (no la carpeta, sino lo que hay dentro) a `public_html/`,
   con el **Administrador de archivos** del panel o con FileZilla (FTP/SFTP).
4. Sube también `documentacion/plantillas/.htaccess` a `public_html/`. Fuerza HTTPS, activa la
   página 404, la compresión y la caché.
5. Abre la web y prueba: portada, un caso, la versión en inglés, descargar el CV y una dirección
   inventada (debe salir la 404).

**Inconveniente:** cada cambio hay que volver a subirlo a mano. Algunos paneles (Hostinger,
cPanel con «Git Version Control») pueden publicar desde GitHub automáticamente.

**En una subcarpeta** (`javierbenitez.es/portfolio/`): pasa la dirección completa a
`cambiar-dominio.py` (`https://javierbenitez.es/portfolio/`) y cambia a mano las rutas que
empiezan por `/` en `site/404.html` (`/`, `/#proyectos`, `/en/`, `/favicon.svg`,
`/apple-touch-icon.png`) por `/portfolio/...`. El script te avisa.

**Nginx (VPS propio):** tienes un bloque de configuración equivalente en
`documentacion/plantillas/nginx.conf`.

---

## 7. Después de migrar (para cualquier opción)

- [ ] `python3 herramientas/comprobar-web.py` sin errores.
- [ ] La web abre con **https** y el candado, en móvil y ordenador.
- [ ] **Google Search Console** (https://search.google.com/search-console): añade el dominio,
      verifícalo con el registro TXT que te pida y envía `https://tu-dominio/sitemap.xml`.
- [ ] **Vista previa en LinkedIn:** pega la URL en https://www.linkedin.com/post-inspector/
      para que lea la imagen y el título nuevos (LinkedIn guarda la antigua unos días).
- [ ] **Actualiza la dirección en:**
  - el CV (y vuelve a subir el PDF);
  - LinkedIn (sección «Contacto» y «Destacados»);
  - tu perfil de GitHub (campo «Website» y README de `degallo/degallo`);
  - Ícaro;
  - la firma del correo.
- [ ] Si usabas analítica, cambia el dominio también allí.

---

## 8. Si dejas GitHub Pages: redirigir `degallo.github.io`

Con la **opción A** no hace falta: GitHub redirige solo.

Si te vas a otro alojamiento (opciones B a E) y quieres que los enlaces antiguos sigan
funcionando, deja en este repositorio una web mínima que redirija. Sustituye el contenido de
`site/` por estos dos archivos (cambia el dominio):

**`site/index.html`**

```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Javier Benítez Escobedo · El portfolio se ha mudado</title>
  <link rel="canonical" href="https://javierbenitez.es/">
  <meta http-equiv="refresh" content="0; url=https://javierbenitez.es/">
  <meta name="robots" content="noindex">
</head>
<body>
  <p>El portfolio está ahora en <a href="https://javierbenitez.es/">javierbenitez.es</a>.</p>
</body>
</html>
```

**`site/404.html`**: igual, pero conservando la ruta (por ejemplo, `/proyectos/hueco-comercial.html`):

```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Redirigiendo…</title>
  <meta name="robots" content="noindex">
  <script>location.replace('https://javierbenitez.es' + location.pathname + location.hash);</script>
</head>
<body>
  <p>El portfolio está ahora en <a href="https://javierbenitez.es/">javierbenitez.es</a>.</p>
</body>
</html>
```

---

## 9. Volver atrás si algo sale mal

- **Deshacer el cambio de dominio en los archivos:**

  ```bash
  python3 herramientas/cambiar-dominio.py https://degallo.github.io/ --aplicar
  ```

- **Volver a la versión de la copia de seguridad:** `git checkout v1.0 -- site` y después commit
  y push.
- **Quitar el dominio en GitHub:** Settings → Pages → Custom domain → **Remove**. La web vuelve
  a `degallo.github.io` en unos minutos.

---

## 10. Plantillas incluidas (`documentacion/plantillas/`)

| Archivo | Para | Dónde va al migrar |
|---|---|---|
| `_headers` | Netlify y Cloudflare Pages: caché y seguridad (CSP probada con esta web) | Dentro de `site/` |
| `netlify.toml` | Netlify: carpeta que se publica | Raíz del repositorio |
| `vercel.json` | Vercel: carpeta que se publica, caché y seguridad | Raíz del repositorio |
| `.htaccess` | Apache (hosting tradicional): HTTPS, 404, compresión, caché | Junto al contenido de `site/` |
| `nginx.conf` | Nginx (VPS): bloque `server` equivalente | Configuración del servidor |
| `CNAME.ejemplo` | Solo si alguna vez publicas desde una rama en vez de con Actions | `site/CNAME` (sin `.ejemplo`) |

**Sobre la política de seguridad (CSP) de `_headers`:** permite el pequeño `<script>` de una
línea que hay en el `<head>` de cada página gracias a su huella (`sha256-…`). Si algún día
cambias ese script, hay que recalcular la huella: si no, el navegador lo bloquea. No es grave
(la web sigue funcionando), pero las animaciones de entrada pueden dar un pequeño parpadeo.
Cómo recalcularla: `MANTENIMIENTO.md`, apartado «Cabeceras de seguridad». También
permite incrustar Looker Studio (`frame-src`) para cuando publiques los dashboards. Si añades
analítica (GoatCounter, Plausible…), añade su dominio a `script-src` y `connect-src`.
