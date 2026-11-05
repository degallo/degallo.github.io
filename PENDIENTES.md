# Pendientes y decisiones

Lista viva. Javi marca lo que vaya resolviendo; Claude Code añade aquí cualquier `[PENDIENTE]`
que deje en la web.

## Antes de publicar la web (bloqueantes)

- [x] **CV para la web sin dirección postal ni teléfono** — hecho (provisional) en
      `site/assets/docs/CV_Javier_Benitez_Escobedo.pdf`: es el CV actual con las filas de teléfono
      y dirección eliminadas. Sustituirlo por la versión definitiva cuando exista.
- [ ] **CV definitivo:** el PDF actual es una imagen (no tiene capa de texto), así que los
      sistemas de selección (ATS, Ícaro) no pueden leerlo. Exportarlo con texto seleccionable.
      Aprovechar para cambiar la frase del perfil por la nueva (ya está en la web):
      "En las prácticas quiero trabajar con datos internos de una empresa, pasar de SQL a
      Python/pandas en un caso real y aprender cómo se usa un cuadro de mando en un equipo."
      Y poner la URL del portfolio.
- [ ] **Añadir al CV el proyecto de moda** (16 cadenas, octubre 2026). Ahora mismo la web
      tendría cuatro proyectos y el CV tres.
- [x] **Moneda del proyecto de Barcelona:** confirmado por Javi, son dólares. La web usa "$".
- [x] **Teléfono en la web:** sí, 625 79 05 41 (Javi lo confirmó el 4-nov-2026). Está en Contacto y en el pie. **Falta añadirlo al CV descargable** (`CV_Javier_Benitez_Escobedo.pdf` no lo lleva todavía).

## Repositorios de los proyectos (los va a abrir el reclutador)

- [ ] **PROYECTOROPA:** quitar `CLAUDE.md` e `INSTRUCCIONES_AMPLIACION.md` del repo público
      (contienen notas internas y datos personales y dicen que el análisis lo hace la IA, lo
      cual resta credibilidad). Renombrar el repo (p. ej. `posicionamiento-precio-moda`) y
      añadir un README como el de `huecocomercial`.
- [ ] **la-ilusion-del-descuento:** no tiene README. Añadir uno (pregunta, métrica, embudo,
      resultado, limitaciones, cómo reproducirlo).
- [ ] **huecocomercial:** el README dice "de 277 a 114 candidatos" en un título y 113 en la
      tabla y el informe; unificar en 113. La sección "Estructura del repositorio" menciona
      `sql/`, `resumen-ejecutivo.pdf` y `dashboard/` que no existen.
- [ ] **Barcelona:** crear repositorio público con el SQL y un README.
- [ ] Fijar (pin) los cuatro repos en el perfil de GitHub y actualizar el README de perfil
      (`degallo/degallo`) con enlace al portfolio.

## Contenido que falta o hay que decidir

- [ ] **Dashboards de Looker Studio:** el CV dice que hay cuadros de mando; si existen enlaces
      públicos, son lo más valioso que se puede enseñar. Añadirlos a cada `contenido/proyectos/*.md`.
- [ ] **Cursos y certificaciones** que no están en el CV (p. ej. el curso de análisis de datos
      de IBM, si lo está haciendo o lo ha terminado). Merecen una línea en "Trayectoria".
- [ ] ¿Mencionar el objetivo del Máster en Big Data y Business Analytics (ESIC)? Puede reforzar
      el mensaje de "voy en serio con los datos".
- [ ] Ámbito de las prácticas: Granada / Málaga / remoto / cualquier sitio.
- [ ] Fechas de la formación (año de inicio del grado, años del ciclo superior). Aplazado por
      decisión de Javi: de momento la web muestra solo la duración, sin marcador.
- [x] Reescribir la frase del perfil — aprobada y publicada en "Sobre mí".
- [x] **Versión en inglés:** portada y las 4 páginas de caso en `site/en/` (selector ES/EN en cada página, hreflang en ambos idiomas). **Falta:** informes PDF y CV en inglés (los botones indican "(ES)"). En inglés no se muestran los marcadores de dashboard ni de repositorio pendientes; siguen en la versión en castellano.
- [x] Uso de IA: decidido no mencionarlo en la web.

## Marcadores pendientes (desde nov. 2026, ocultos como comentario HTML; ya no se ven en la web)

| Página | Marcador | Se resuelve con |
|---|---|---|
| hueco-comercial · ilusion-descuento · alquiler-turistico-barcelona | `[PENDIENTE: enlace público de Looker Studio]` | Enlace de "Insertar" de Looker Studio (el `<iframe>` ya está preparado en un comentario del HTML) |
| alquiler-turistico-barcelona | `[PENDIENTE: repositorio público con el SQL]` | Crear el repo y enlazarlo |
| posicionamiento-moda | `[PENDIENTE: repositorio limpio y con README]` | Limpiar/renombrar PROYECTOROPA y enlazarlo |

Notas de la primera versión:

- `la-ilusion-del-descuento` sí se enlaza (ya aparece en el CV), aunque sigue sin README.
- En el embudo de moda, el paso 890 → 873 se ha etiquetado con el criterio "marcas con 5 modelos
  o más por prenda", que es el que figura en el `.md` para las métricas. Comprobar que es el motivo.
- Uso de IA: decidido **no** mencionarlo en la web.
- Foto del hero: recorte en B/N `javier-benitez-recorte-700/900/1200.webp`. `javier-benitez-1000.webp`
  se usa en los datos estructurados de la portada. `foto-perfil.webp` se conserva pero ya no se usa.

## Ronda 2 (rediseño)

- [x] Hero con el nombre completo; "Sobre mí" abre con la frase de estudiante de la UGR.
- [x] Eliminada la sección "Cómo trabajo".
- [x] Trayectoria con logos (UGR, IES Ángel Ganivet, Cafetería Bar El Gallo, MODE Foundation),
      en gris y a color al pasar el ratón.
- [x] Nueva llamada a la acción orientada a aprender y quedarse.

## Ronda 3

- [x] Disponibilidad: "a partir de febrero de 2027", sin fecha de fin (decisión de Javi).
- [x] Texto justificado en toda la web, con guiones automáticos.
- [x] Bloques más separados: bandas gris/blanco alternas y cabecera numerada (01–04) en cada bloque.

## Ronda 5 · Auditoría final (5-nov-2026)

Detalle completo en `documentacion/AUDITORIA.md`. Hecho:

- [x] Montserrat autoalojada (fuera Google Fonts), imágenes a medida (800/1200 px), SVG optimizados.
- [x] Resumen (pregunta, resultado, herramientas) al principio de cada caso, ES y EN.
- [x] Visor de gráficos, botón «Copiar email», hoja de impresión, «Volver arriba».
- [x] robots.txt, sitemap.xml bilingüe, datos estructurados por caso, imagen para redes en JPG.
- [x] Accesibilidad 100 en todas las páginas; rendimiento móvil 97–100.
- [x] Guía de migración, guía de mantenimiento, plantillas de alojamiento y herramientas.

Nuevo por decidir o hacer (además de lo ya listado arriba):

- [ ] **Perfil de GitHub:** archivar o hacer privados los repositorios antiguos sin descripción
      (CC, ALJIBE, MARK-SECT, DISC1, MarkInter): es lo primero que ve quien pulsa «GitHub».
- [ ] **Fecha de fin del grado** (p. ej. «Finalización prevista: junio de 2027»): es un filtro
      habitual de los reclutadores de prácticas.
- [ ] **¿Helvetica también en Windows/Android?** Hoy se ve Arial; opciones en
      `documentacion/MANTENIMIENTO.md` (licencia o clon libre TeX Gyre Heros).
- [ ] Tras cambiar de dominio (si se hace): Google Search Console + sitemap y LinkedIn Post Inspector.

## Después del lanzamiento

- [ ] Dominio propio (opcional, ~10 €/año) o mantener `degallo.github.io`.
- [ ] Analítica respetuosa sin cookies (GoatCounter o similar) para saber si los reclutadores
      entran y qué proyecto miran — muy coherente con un perfil de datos.
- [ ] Poner la URL del portfolio en el CV, en LinkedIn (sección destacados) y en Ícaro.
- [ ] Un quinto proyecto con **Python/pandas** cuando se domine un poco más (ahora todo es SQL),
      idealmente sobre datos de marketing (campañas, encuestas, segmentación de clientes).


## Ocultos en la web hasta tenerlos (nov. 2026)

Están como comentario HTML en su página; al tener el dato, descomentar y rellenar.

- [ ] Enlaces públicos de Looker Studio: hueco comercial, ilusión del descuento y alquiler turístico (bloque "Dashboard interactivo").
- [ ] Repositorio público con el SQL del alquiler turístico en Barcelona (fila "Código" de la ficha).
- [ ] Repositorio limpio y con README del posicionamiento de moda (fila "Código" de la ficha).
