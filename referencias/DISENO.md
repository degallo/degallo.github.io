# Dirección de diseño

> **Actualización (ronda 2, noviembre 2026) — manda sobre lo de abajo.**
> Javi pidió una portada más profesional y menos "storytelling", con estas referencias:
> portfolios de *daniel stoopendaal* y *Alex Graham* (nombre gigante en Helvetica cruzando un
> retrato en blanco y negro sobre fondo gris, navegación mínima en píldora).
> - **Paleta:** monocroma (gris claro `#F1F1EF`, blanco, tinta `#111`). El terracota `#A4472B`
>   queda solo como acento mínimo (puntos de etiqueta, hover).
> - **Tipografía:** principal **Helvetica** (titulares y nombre); secundaria y terciaria
>   **Montserrat** (texto y etiquetas en mayúsculas espaciadas). Sin otras familias.
> - **Hero:** el nombre completo en grande con `mix-blend-mode: difference` sobre el retrato
>   recortado (`javier-benitez-recorte-*.webp`).
> - **Contenido:** sin la sección "Cómo trabajo" ni titulares eslogan. Trayectoria en dos
>   columnas (Formación / Experiencia) con los logos de cada institución en `assets/img/logos/`.

## Referencia: plantilla Finox (Webflow)

Capturas en `referencias/capturas/`:

| Captura | Sección | Qué tomar |
|---|---|---|
| `finox-01.png` | Hero | Titular gigante ("Hello") en tipografía grotesca fina, subtítulo con raya ("— It's Finox…"), retrato en blanco y negro recortado a la derecha, "Scroll down ↓", año en vertical en el lateral |
| `finox-02.png` | About me | Texto a la izquierda; columna de tarjetas blancas redondeadas con una cifra enorme y un icono en círculo; fotos en B/N; puntos con icono y texto corto |
| `finox-03.png` | Portfolio | Tarjetas grandes con imagen a sangre, esquinas redondeadas, título "Nombre — descripción" debajo, carrusel horizontal |
| `finox-04.png` | Experiences | Etiqueta "● Experiences", titular grande, filas separadas por líneas finas: lugar + fechas · descripción · etiquetas en píldora gris |
| `finox-05.png` | CTA | Bloque oscuro a todo ancho con imagen desaturada de fondo, titular centrado y enlace subrayado con flecha ↗ |
| `finox-06.png` | Footer | Fondo negro, navegación, contacto centrado en grande, redes a los lados y el nombre gigante semitransparente cortado por abajo |

**Rasgos que definen el estilo:** casi monocromo (grises sobre #F3F3F3, negro #0F1112),
tipografía Inter Display con interletraje negativo en titulares, mucho espacio en blanco,
radios de 12–24 px, enlaces subrayados con flecha ↗ en lugar de botones, etiquetas de
sección con un punto "● Sección", animaciones suaves de aparición al hacer scroll.

**Licencia:** Finox es una plantilla comercial. Se usa solo como inspiración visual. No se
copia su código, sus imágenes ni sus iconos.

## Adaptación para un reclutador (no para un cliente)

| En Finox | En el portfolio |
|---|---|
| "Book A Call ↗" | "Descargar CV ↗" (cabecera) y "Escríbeme ↗" (CTA) |
| "320 % Average increase in client engagement" | Cifras reales de los proyectos: "11.237 gasolineras auditadas", "277 municipios medidos", "15.293 anuncios depurados", "1.697 prendas comparadas" |
| Services / Pricing | Se elimina. En su lugar: "Cómo trabajo" (método) y "Herramientas" |
| Blog | Se elimina (o más adelante, "Notas" con aprendizajes) |
| "Exclusive Winter Deal… Free Consultation" | "¿Buscas a alguien para prácticas en análisis de datos? Disponible feb–jun 2027" |
| Experiences (empresas de diseño) | Trayectoria: formación + experiencia real |
| Portfolio con mockups bonitos | Tarjetas con la imagen real de cada informe (mapa, gráfico principal) + pregunta y hallazgo en una línea |

## Identidad propia: puente con el CV

El CV de Javi ya tiene una identidad clara; la web debe parecer de la misma persona:

| Token | Valor (muestreado del CV) | Uso |
|---|---|---|
| Acento | `#A4472B` (terracota) | Etiquetas de sección, subrayados, cifras clave, estados hover. Úsalo con moderación |
| Fondo cálido | `#F6F1E6` (crema) | Alternativa al gris de Finox para el fondo general o para bloques |
| Tinta | `#191918` | Texto y bloques oscuros (CTA, pie) |

Además, los informes de los proyectos usan una paleta parecida (crema, granate/terracota,
azul grisáceo), así que las imágenes encajarán con el fondo cálido.

**Tipografía:** el CV usa una grotesca geométrica en mayúsculas espaciadas (tipo Montserrat)
para titulares. Propuesta: **Inter** o **Inter Tight** (titulares grandes, interletraje negativo, como Finox)
+ la misma familia para el texto. Opcional: mayúsculas espaciadas pequeñas para etiquetas de
sección, como el CV ("PERFIL", "PROYECTOS DE DATOS"). Claude Code puede proponer otra pareja,
pero máximo dos familias.

**Modo oscuro:** opcional. Si se implementa, que respete `prefers-color-scheme` y que las
imágenes de los informes (fondo crema) se vean dentro de una tarjeta, no flotando sobre negro.

## Detalles que suman con reclutadores

- Píldora de estado en el hero: "● Disponible para prácticas · feb–jun 2027".
- En cada tarjeta de proyecto: herramientas y fuentes como etiquetas (SQL, Looker Studio, INE, MITECO…).
- En cada caso de estudio, una ficha lateral fija (sticky) con fecha, datos, herramientas y enlaces.
- Botón de descarga del informe PDF y enlace al repositorio con el SQL.
- El texto tiene que poder escanearse: titulares que ya cuentan la conclusión (como hacen los propios informes).
