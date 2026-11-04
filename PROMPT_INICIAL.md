# Prompt para la sesión de Claude Code (copiar y pegar)

> Abre una sesión de Claude Code en la web sobre el repositorio `degallo/degallo.github.io`
> y pega todo el bloque de abajo como primer mensaje.

---

Vas a construir mi portfolio web de analista de datos. Todo el contexto está en este repositorio; antes de escribir una sola línea de código, lee en este orden:

1. `CLAUDE.md` — quién soy, para quién es la web, reglas de contenido, stack y forma de trabajar.
2. `contenido/perfil.md` — mis datos, formación, experiencia, habilidades y enlaces.
3. `contenido/proyectos/*.md` — los cuatro proyectos, con todas las cifras ya verificadas.
4. `referencias/DISENO.md` y las imágenes de `referencias/capturas/` — la dirección visual.
5. `PENDIENTES.md` — lo que todavía no está decidido o falta.

**Objetivo:** una web estática (HTML, CSS y JS sin frameworks) dentro de `site/`, que se publica sola en GitHub Pages con el workflow que ya existe. Está pensada para **reclutadores**, no para clientes: tiene que dejar claro en 5 segundos que soy estudiante de último curso de Marketing e Investigación de Mercados (UGR), que busco **prácticas curriculares en análisis de datos para febrero–junio de 2027**, y que tengo cuatro proyectos propios con datos públicos reales que lo demuestran.

**Qué quiero en la portada (`site/index.html`), en este orden:**

1. **Cabecera fija** minimalista: mi nombre a la izquierda; Sobre mí · Proyectos · Trayectoria · Contacto; a la derecha un enlace subrayado "Descargar CV ↗".
2. **Hero** al estilo Finox: un titular enorme (propón 2–3 opciones, por ejemplo "Hola." o "Datos con criterio de negocio"), una línea que diga qué hago y qué busco, una etiqueta tipo píldora "Disponible para prácticas · feb–jun 2027", mi foto en blanco y negro (`site/assets/img/foto-perfil.webp`) y "Bajar ↓".
3. **Sobre mí** con tarjetas: un texto corto, 2–3 tarjetas con cifras **reales** sacadas de los proyectos (por ejemplo "11.237 gasolineras auditadas", "277 municipios medidos uno a uno", "15.293 anuncios depurados") y las herramientas (SQL/SQLite, Looker Studio, Excel/Sheets, Python y pandas en aprendizaje, Git/GitHub).
4. **Proyectos**: los cuatro como tarjetas grandes con imagen, título, la pregunta de negocio en una línea, el hallazgo principal en una línea, etiquetas de herramientas y fuentes, y enlace al caso de estudio. Orden: El hueco comercial, La ilusión del descuento, Alquiler turístico en Barcelona, Posicionamiento de precio en moda.
5. **Cómo trabajo**: 3–4 principios que se repiten en mis proyectos (pregunta de negocio primero; cada filtro con su motivo; confirmar un hallazgo con métricas independientes; decir en voz alta lo que el análisis no resuelve). Usa frases y ejemplos de los propios proyectos.
6. **Trayectoria**: lista al estilo "Explore My Design Journey" de Finox con formación y experiencia (fila: lugar y fechas · descripción · etiquetas). Incluye la experiencia no relacionada con datos tal cual está en el perfil; es útil.
7. **Bloque CTA** oscuro: "¿Buscas a alguien para prácticas en análisis de datos?" + email + Descargar CV.
8. **Pie oscuro** con mi nombre gigante de fondo, email, LinkedIn y GitHub.

**Páginas de caso de estudio** (`site/proyectos/<slug>.html`, una por proyecto, misma plantilla): portada con título y subtítulo; ficha (fecha, fuentes, herramientas, volumen de datos, enlace al repositorio si existe y al informe PDF); la pregunta; la métrica (con su "qué señala / qué no es"); el embudo de filtrado; los hallazgos con las cifras clave destacadas; las imágenes de `site/assets/img/proyectos/<slug>/` con pies de foto; limitaciones; "cómo usarlo"; conclusión; y navegación al proyecto anterior/siguiente. Si el proyecto tiene marcador de dashboard de Looker Studio en el `.md`, deja preparado un bloque para incrustarlo.

**Cómo quiero que trabajemos:**

- Primero, en un mensaje corto: dime qué has entendido, propón la paleta, las fuentes y 2–3 opciones de titular del hero, y señala cualquier cosa del contenido que te parezca floja para un reclutador. Espera mi respuesta.
- Después, construye una **primera versión completa y funcional** (portada + los cuatro casos), haz commit y push a `main` y dime la URL de GitHub Pages para verla.
- Luego iteramos por rondas cortas. Commits pequeños con mensajes en español.
- No inventes ningún dato. Lo que falte, `[PENDIENTE: …]` visible y apuntado en `PENDIENTES.md`.
- No copies código, imágenes ni SVG de la plantilla Finox: es solo referencia visual.
- Antes de cada entrega revisa: móvil (375 px) y escritorio, enlaces y descargas, contraste, `alt` de las imágenes, y que no hay errores en la consola.
