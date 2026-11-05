# Auditoría final del portfolio

**Fecha:** 5 de noviembre de 2026 · **Versión auditada:** la publicada en `main` (rondas 1–4 + versión en inglés)
**Alcance:** las 11 páginas (portada y 4 casos en castellano e inglés, más la 404), en móvil, tableta y escritorio.

> Regla de esta ronda: **no cambiar lo que ya había**, solo mejorarlo. No se ha tocado ningún texto
> aprobado ni la dirección visual; todo lo nuevo es aditivo (y está listado en el apartado 4).

---

## Resumen en 30 segundos

| | Antes | Después |
|---|---|---|
| Rendimiento · portada en móvil | 84 | **97** |
| Rendimiento · casos en móvil | 92–93 | **100** |
| Rendimiento · escritorio (todas) | 100 | **100** |
| Accesibilidad (todas) | 96–97 | **100** |
| Buenas prácticas (todas) | 100 | **100** |
| SEO (todas) | 100 | **100** |
| Primer pintado en móvil (portada / casos) | 2,9 s / 2,5 s | **1,2 s / 1,1 s** |
| Elemento principal visible en móvil (LCP) | 3,3 s / 2,7 s | **2,5 s / 1,8 s** |
| Errores de accesibilidad (axe) | 2 tipos, en todas las páginas | **0** |
| Errores de validación HTML | 0 (solo avisos de estilo) | **0** |

Medido con Lighthouse 12 (móvil simulado en 4G lenta y escritorio) sobre las 10 páginas de
contenido, más axe-core y html-validate. En GitHub Pages las cifras reales serán iguales o mejores
(sirve con compresión y CDN).

**Lo más importante que queda en tus manos** (no se puede resolver desde el código):

1. **El CV descargable es una imagen.** Los programas de selección (ATS) y el buscador de Ícaro no
   pueden leerlo. Además no incluye el proyecto de moda ni el teléfono.
2. **El dominio `degallo.github.io` no lleva tu nombre.** Un dominio propio (≈10 €/año) da más
   seriedad. La guía de migración explica cómo hacerlo en 20 minutos sin perder nada.
3. **Tu perfil de GitHub es lo primero que abre un reclutador técnico** y ahora muestra repositorios
   antiguos sin descripción (CC, ALJIBE, MARK-SECT, DISC1, MarkInter) junto a los cuatro proyectos.
4. **Los cuadros de mando de Looker Studio no se pueden ver.** Tu CV y la web dicen que los haces;
   un enlace público es la prueba más convincente que puedes dar.
5. **Falta la fecha de fin del grado y si aceptas otras ciudades o remoto.** Son los dos filtros
   que más usan los reclutadores de prácticas.

El detalle de cada uno está en el apartado 6.

---

## 1. Cómo se ha hecho

- **Lectura completa del código** vigente (también lo hecho en otras sesiones: versión en inglés,
  franja de herramientas, ilustraciones de proyecto, teléfono).
- **Herramientas automáticas:** Lighthouse (rendimiento, accesibilidad, buenas prácticas y SEO),
  axe-core (accesibilidad, con todo el contenido visible) y html-validate (HTML).
- **Revisión visual** con capturas de página completa a 375, 768, 1024, 1440 y 1920 px.
- **Pruebas de uso reales con navegador:** menú móvil, enlaces internos, visor de gráficos,
  copiar email, versión impresa, la web sin JavaScript y la web con una política de seguridad
  estricta.
- **Revisión de contenido** frase a frase desde el punto de vista de un reclutador (castellano e
  inglés) y comprobación de que los repositorios enlazados existen y son públicos.

---

## 2. La web vista por un reclutador

Un reclutador de prácticas dedica entre 30 segundos y 3 minutos. Esto es lo que ve en cada tramo.

### Los primeros 5 segundos (hero)

**Funciona muy bien:**
- Tu nombre enorme, la foto profesional y, encima, la fila de datos: qué estudias, enlaces
  y disponibilidad («a partir de febrero de 2027»).
- «Descargar CV» está en la cabecera y en el hero, a un clic desde cualquier punto.

**Mejorado en esta ronda:**
- Se añade **«Granada»** a la fila de datos. La ubicación es lo segundo que mira un reclutador
  de prácticas, y solo aparecía en el pie.
- A 1024 px (portátiles pequeños y tabletas en horizontal), el pelo del retrato tapaba
  «Disponible para prácticas…». Ahora el retrato se ajusta para no llegar a esa fila.
- La foto se sirve al tamaño exacto de cada pantalla y se pide con prioridad alta. En móvil
  aparece antes.

### Los primeros 30 segundos (Sobre mí y proyectos)

**Funciona muy bien:**
- La frase de Sobre mí dice en una línea quién eres y en qué te especializas.
- Las herramientas, con su nivel honesto («en aprendizaje» en Python).
- Cada proyecto se entiende sin abrirlo, con su pregunta y su resultado en una línea. Eso es
  exactamente lo que busca un reclutador de datos.

**Mejorado en esta ronda:**
- Cada botón «Ver caso» lleva para los lectores de pantalla el nombre de su proyecto. Antes
  había cuatro enlaces idénticos.
- Las ilustraciones (mapas SVG) pesan un 60 % menos sin ningún cambio visible.

### Los primeros 3 minutos (un caso de estudio)

**Funciona muy bien:**
- La estructura: pregunta, métrica (con «qué señala / qué no es»), embudo con el motivo de cada
  descarte, hallazgos, limitaciones y cómo usarlo. Demuestra criterio, que es lo que diferencia
  a un buen candidato de datos.
- La ficha lateral con fuentes, volumen y descargas.

**Mejorado en esta ronda:**
- **Resumen al principio de cada caso** (pregunta, resultado y herramientas, con los mismos textos
  ya aprobados de la portada). Quien llega directo a un caso, por ejemplo desde un enlace en
  LinkedIn, ve la conclusión en 10 segundos. Antes estaba al final.
- **Visor de gráficos:** las páginas del informe se amplían encima de la página sin salir de
  ella. Se cierra con Esc o con un clic fuera. En móvil antes eran ilegibles.
- **La ficha lateral ya no se corta** en portátiles: antes medía más que la pantalla y el
  índice quedaba fuera de vista. Ahora tiene su propio desplazamiento.
- **En móvil, primero el contenido.** La ficha (fuentes, volumen) pasa al final, como anexo,
  y bajo el título aparecen dos accesos rápidos: «Informe PDF» y «Código en GitHub». Antes había
  que bajar casi una pantalla de ficha antes de ver nada del análisis.
- Los botones de descarga indican **el peso del PDF** (por ejemplo, «2,2 MB»).
- Las tablas anchas muestran **una sombra lateral** cuando hay más columnas al deslizar en móvil.
- Un apartado que empieza con un recuadro ya no deja un hueco de más.

### El contacto

**Funciona muy bien:** el email, el teléfono y el CV juntos, con una frase que transmite ganas
de aprender y quedarse.

**Mejorado en esta ronda:**
- Botón **«Copiar email»**. Muchos reclutadores usan correo web, y ahí el enlace `mailto:` no
  abre nada.
- El teléfono ya no se parte en dos líneas («625 79 / 05 41»).
- En el pie de escritorio, el enlace «CV» ya no salta a una segunda línea. En móvil, el email y
  el teléfono van uno debajo del otro.
- Se añade «Volver arriba ↑» en el pie.

### Imprimir o guardar como PDF

Algunos reclutadores imprimen o guardan la página para pasársela a otra persona del equipo.
**Antes salían vacíos** todos los bloques que aparecen al hacer scroll, y también el nombre del
hero. Ahora hay una hoja de impresión con todo visible, sin animaciones ni bloques negros, y con
las URL de los enlaces escritas.

---

## 3. Auditoría técnica

### Rendimiento

| Problema encontrado | Solución |
|---|---|
| Montserrat se pedía a Google Fonts: bloqueaba el primer pintado ~0,9 s en móvil y enviaba la IP de cada visitante a Google | Fuente **autoalojada** en `site/assets/fonts/`: 34 KB con el eje de grosor 400–600, más 3 KB solo para «Ł ł» (antes eran 108 KB entre dos archivos) |
| Las páginas de los informes se servían a 1600 px aunque se vieran a 343 px en móvil | Versiones de **800 y 1200 px**: el navegador elige la que necesita. En móvil pasan de 1,3 MB a 0,5 MB en total |
| Retrato del hero: tamaño declarado distinto del real en móvil | Tamaños corregidos y versión intermedia de 900 px |
| Logos de Inditex, Mango y Tendam a 640 px mostrados a ~150 px | Versiones de 400 px |
| Mapas SVG de 160 KB y 61 KB | Optimizados a 51 KB y 38 KB, sin diferencia visible (comprobado píxel a píxel) |

Lighthouse sigue mostrando algunos avisos que dependen del alojamiento, no de la web: caché de
10 minutos de GitHub Pages, compresión del servidor local de pruebas y minificación de CSS y JS
(la web no tiene paso de compilación a propósito). La guía de migración incluye la configuración
de caché para cuando haya un alojamiento que la permita.

### Accesibilidad

| Problema | Solución |
|---|---|
| El enlace «EN»/«ES» se anunciaba como «English version», sin incluir el texto visible | Ahora «EN · English version» |
| Las palabras gigantes decorativas («proyectos», «Javier Benítez») contaban como texto sin contraste | Pasan a pintarse con CSS: siguen viéndose igual, pero ya no son contenido |
| La última cifra del embudo era blanca sobre gris claro mientras se animaba la barra | Va en oscuro hasta que la barra se rellena |
| Enlaces que abren pestaña nueva sin avisar | Aviso oculto para lectores de pantalla: «(se abre en una pestaña nueva)» |
| Botones de CV sin indicar formato | «(PDF, 473 KB)» para lectores de pantalla |
| Visor de gráficos (nuevo) | Diálogo nativo con foco en «Cerrar», Esc para salir y vuelta del foco al gráfico |

### SEO y compartir en redes

- **`robots.txt` y `sitemap.xml`** con las dos versiones de idioma enlazadas (antes no existían).
- **`hreflang="x-default"`** en todas las páginas: la versión en castellano es la principal.
- **Datos estructurados en cada caso** (`Article` y migas de pan) y la ciudad en el de la portada.
  Es solo la ciudad; la dirección postal sigue sin publicarse.
- **Imagen para compartir en JPG** (1200×630) por caso de estudio. Antes era WebP, que LinkedIn y
  WhatsApp no siempre muestran, y con proporción 16:9, que recortaban.
- Texto alternativo en las imágenes para compartir, icono para iPhone (`apple-touch-icon.png`)
  y favicon con la paleta actual.

### Buenas prácticas y robustez

- **Si `main.js` no llegara a cargar** (red cortada, bloqueador), antes todo el contenido con
  animación de entrada se quedaba invisible. Ahora la página lo detecta y lo muestra.
- **Modo claro forzado** (`color-scheme`): algunos navegadores de móvil (Samsung Internet,
  Chrome con «oscurecer webs») invertían los colores y estropeaban el efecto del nombre sobre el
  retrato.
- `format-detection` desactivado: iOS no convierte cifras en enlaces de teléfono.
- **Política de seguridad (CSP) preparada y probada** para cuando migres a un alojamiento que
  permita cabeceras: no bloquea nada (ver `documentacion/plantillas/_headers`).
- Versión `?v=10` en las URL de CSS y JS para que nadie vea una copia antigua tras publicar.

### Responsive

Probado a 375, 768, 1024, 1440 y 1920 px, en castellano y en inglés: sin scroll horizontal y con
un solo `h1` por página. Lo corregido:

- A 1024 px, el retrato tapaba la disponibilidad.
- En móvil, la disponibilidad salía justificada con huecos enormes. Ahora va alineada a la izquierda.
- En móvil, la columna de texto de la trayectoria era tan estrecha que el justificado abría
  huecos («Gestión   de   campañas   de»). Ahora el logo va encima y el texto ocupa todo el ancho.
- En móvil, el texto centrado del contacto partía palabras con guion («fe-brero»). Ya no.

**Sobre el texto justificado:** es una decisión tuya y se mantiene. En pantallas muy estrechas
siempre quedará algún hueco entre palabras, porque es inherente al justificado. Se ha reducido
al mínimo con guiones automáticos y columnas más anchas.

---

## 4. Lista completa de cambios aplicados

**Archivos nuevos**
- `site/assets/fonts/`: Montserrat autoalojada y su licencia (SIL OFL 1.1).
- `site/assets/img/og/*.jpg`: imagen para compartir cada caso.
- `site/assets/img/proyectos/*/pagina-NN-800.webp` y `-1200.webp`: versiones ligeras.
- `site/assets/img/javier-benitez-recorte-900.webp` y `logos/*-400.webp`.
- `site/apple-touch-icon.png`, `site/robots.txt`, `site/sitemap.xml`.
- `herramientas/`: comprobar la web, cambiar de dominio y preparar imágenes.
- `documentacion/`: esta auditoría, la guía de migración, la de mantenimiento y las plantillas.

**Archivos modificados**
- Las 10 páginas: cabecera (`<head>`) optimizada, resumen en los casos, accesos rápidos en móvil,
  peso de los PDF, «Granada», avisos accesibles, «Volver arriba», teléfono sin cortes.
- `css/styles.css`: fuentes locales y un bloque final «Ronda 5» con todo lo nuevo; no se ha
  borrado ninguna regla anterior.
- `js/main.js`: visor de gráficos, copiar email y señal de que el script ha cargado.
- `404.html`: bilingüe, con enlace a la versión en inglés.
- Iconos SVG de los proyectos: optimizados, idénticos a la vista.

**Archivo eliminado:** `javier-benitez-640.webp`, que ya no se usaba en ninguna página.

---

## 5. Probado y descartado

| Idea | Por qué no |
|---|---|
| Retrato en AVIF | A la misma calidad visual pesa más que el WebP actual (59 KB frente a 54 KB). Con más compresión el pelo y la barba se emborronan |
| Servir Helvetica como fuente web para Windows y Android | Helvetica es de pago (Monotype). Hay clones libres (TeX Gyre Heros, FreeSans), pero o no se pueden descargar desde aquí o tienen licencia GPL. Hoy en Windows se ve Arial, que es casi idéntica. Las opciones están en la guía de mantenimiento |
| Minificar CSS y JS | Supondría añadir un paso de compilación, y la web se mantiene legible a propósito. El ahorro es de unos 5 KB comprimidos |
| Quitar animaciones para ganar puntos de rendimiento | Son parte del diseño que elegiste y no bloquean nada (0 ms de bloqueo) |

---

## 6. Lo que queda en tus manos (por prioridad)

1. **CV con texto seleccionable** (`site/assets/docs/CV_Javier_Benitez_Escobedo.pdf`). Expórtalo
   desde el editor original con «PDF con texto», no como imagen. Añade el proyecto de moda,
   el teléfono y la URL del portfolio, y cambia la frase del perfil por la de la web. Usa el
   mismo nombre de archivo y no tendrás que tocar nada más.
2. **Dominio propio**, por ejemplo `javierbenitez.es`. GitHub redirige automáticamente
   `degallo.github.io` al dominio nuevo, así que los enlaces antiguos siguen funcionando. Pasos
   en `GUIA-MIGRACION.md`, opción A.
3. **Perfil de GitHub:**
   - Fija (pin) los cuatro proyectos.
   - Archiva o haz privados los repositorios antiguos sin descripción.
   - Añade un README a `la-ilusion-del-descuento`.
   - Crea el repositorio de Barcelona.
   - Limpia `PROYECTOROPA` (ver `PENDIENTES.md`).
4. **Enlaces públicos de Looker Studio.** Ya hay un hueco preparado y comentado en cada caso.
5. **Fecha de fin del grado** (por ejemplo, «Finalización prevista: junio de 2027») y **ámbito
   de las prácticas** (Granada, Málaga, remoto…). Ahora solo se ve «Granada».
6. **CV e informes en inglés**, para que la versión inglesa no lleve a documentos en castellano.
7. **Analítica sin cookies** (GoatCounter, gratuita): sabrás si los reclutadores entran y qué
   proyecto miran, y no necesita aviso de cookies.
8. **LinkedIn:** el enlace del portfolio en «Destacados» y en el titular.
9. **Experiencia en El Gallo:** seis años gestionando un negocio son un argumento fuerte. Si tienes
   datos reales (tamaño del equipo, número de proveedores, algo que mediste), una cifra lo haría
   más concreto. No se ha añadido nada porque no está en `contenido/`.
10. **Un quinto proyecto en Python/pandas**, como ya tienes previsto en `PENDIENTES.md`.

---

## 7. Cómo repetir esta auditoría

Desde la raíz del repositorio:

```bash
python3 herramientas/comprobar-web.py
```

Revisa enlaces, imágenes, anclas, metadatos y que no quede ningún `[PENDIENTE]` visible. No
necesita instalar nada.

Para las puntuaciones, abre la web en Chrome y usa DevTools (F12) → pestaña **Lighthouse**,
marcando «Mobile» y luego «Desktop». También puedes usar https://pagespeed.web.dev con la URL
pública: mide la web real de GitHub Pages, con su compresión y su caché.
