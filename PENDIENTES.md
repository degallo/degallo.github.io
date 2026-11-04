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
- [ ] **Moneda del proyecto de Barcelona:** el informe usa "$" porque Inside Airbnb pone ese
      símbolo en la columna `price`, pero en Barcelona los precios suelen venir en euros.
      Comprobarlo antes de publicar cifras; un reclutador de datos lo notaría.
- [x] **Teléfono en la web:** no (por defecto). Tampoco va en el CV descargable.

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
- [ ] Fechas de la formación (año de inicio del grado, años del ciclo superior).
- [x] Reescribir la frase del perfil — aprobada y publicada en "Sobre mí".
- [ ] ¿Versión en inglés? Recomendable a medio plazo (el CV dice inglés profesional).
- [ ] Uso de IA: los proyectos se apoyan en Claude para algunas partes (dashboard, informes).
      Decidir cómo contarlo con naturalidad en "Cómo trabajo" (p. ej. "uso asistentes de IA
      para acelerar el código; el planteamiento, la métrica y las conclusiones son míos").
      Mejor contarlo tú que que lo descubra el reclutador.

## Marcadores [PENDIENTE] visibles en la web

| Página | Marcador | Se resuelve con |
|---|---|---|
| Portada · Trayectoria | `[PENDIENTE: años]` en UGR e IES Ángel Ganivet | Fechas de inicio/fin de cada formación |
| hueco-comercial · ilusion-descuento · alquiler-turistico-barcelona | `[PENDIENTE: enlace público de Looker Studio]` | Enlace de "Insertar" de Looker Studio (el `<iframe>` ya está preparado en un comentario del HTML) |
| alquiler-turistico-barcelona | `[PENDIENTE: confirmar que son euros]` | Confirmar la moneda; si son euros, añadir € a las cifras |
| alquiler-turistico-barcelona | `[PENDIENTE: repositorio público con el SQL]` | Crear el repo y enlazarlo |
| posicionamiento-moda | `[PENDIENTE: repositorio limpio y con README]` | Limpiar/renombrar PROYECTOROPA y enlazarlo |

Notas de la primera versión:

- `la-ilusion-del-descuento` sí se enlaza (ya aparece en el CV), aunque sigue sin README.
- En el embudo de moda, el paso 890 → 873 se ha etiquetado con el criterio "marcas con 5 modelos
  o más por prenda", que es el que figura en el `.md` para las métricas. Comprobar que es el motivo.
- La línea sobre el uso de IA en "Cómo trabajo" **no** se ha publicado: falta el visto bueno de Javi.
- Foto del hero: `site/assets/img/javier-benitez-640.webp` y `-1000.webp`, en B/N, a partir de la
  foto de estudio nueva. `foto-perfil.webp` se conserva pero ya no se usa.

## Después del lanzamiento

- [ ] Dominio propio (opcional, ~10 €/año) o mantener `degallo.github.io`.
- [ ] Analítica respetuosa sin cookies (GoatCounter o similar) para saber si los reclutadores
      entran y qué proyecto miran — muy coherente con un perfil de datos.
- [ ] Poner la URL del portfolio en el CV, en LinkedIn (sección destacados) y en Ícaro.
- [ ] Un quinto proyecto con **Python/pandas** cuando se domine un poco más (ahora todo es SQL),
      idealmente sobre datos de marketing (campañas, encuestas, segmentación de clientes).
