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
- [ ] ¿Versión en inglés? Recomendable a medio plazo (el CV dice inglés profesional).
- [x] Uso de IA: decidido no mencionarlo en la web.

## Marcadores [PENDIENTE] visibles en la web

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
- Foto del hero: `site/assets/img/javier-benitez-640.webp` y `-1000.webp`, en B/N, a partir de la
  foto de estudio nueva. `foto-perfil.webp` se conserva pero ya no se usa.

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

## Después del lanzamiento

- [ ] Dominio propio (opcional, ~10 €/año) o mantener `degallo.github.io`.
- [ ] Analítica respetuosa sin cookies (GoatCounter o similar) para saber si los reclutadores
      entran y qué proyecto miran — muy coherente con un perfil de datos.
- [ ] Poner la URL del portfolio en el CV, en LinkedIn (sección destacados) y en Ícaro.
- [ ] Un quinto proyecto con **Python/pandas** cuando se domine un poco más (ahora todo es SQL),
      idealmente sobre datos de marketing (campañas, encuestas, segmentación de clientes).
