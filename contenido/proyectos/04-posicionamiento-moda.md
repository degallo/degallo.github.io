# ¿Compiten de verdad en precio las grandes cadenas de moda en España?

- **slug:** `posicionamiento-moda`
- **Subtítulo:** Posicionamiento de precio de 16 cadenas a partir de su catálogo online.
- **Etiqueta:** Pricing · Moda · Catálogos online
- **Fecha:** octubre 2026 (datos recogidos el 10/10/2026)
- **Fuentes:** catálogo online de cada marca en España (sección mujer), 10/10/2026. Precio de catálogo y precio rebajado.
- **Herramientas:** SQL (SQLite: 7 scripts, de creación de tabla a solapamiento) · Python (unificación de los catálogos en bruto, `construir_bd.py`) · cuartiles con NTILE(4)
- **Volumen:** 1.697 modelos de 16 cadenas → 890 prendas básicas (873 en las métricas)
- **Repositorio:** https://github.com/degallo/PROYECTOROPA [PENDIENTE: renombrar, añadir README y limpiar; ver PENDIENTES.md]
- **Informe PDF:** `site/assets/docs/posicionamiento-precio-moda.pdf` (18 páginas)
- **No está en el CV actual.** [PENDIENTE: añadirlo al CV]

## Imágenes disponibles (`site/assets/img/proyectos/posicionamiento-moda/`)

| Archivo | Qué muestra |
|---|---|
| `pagina-01.webp` | Portada: escalera de precio mediano del vaquero básico por marca (Inditex en azul, Tendam en naranja) |
| `pagina-02.webp` | Resumen: ×2 · 97 % · 78 % |
| `pagina-04.webp` | Rango de precios por cadena (camiseta y vaquero) |
| `pagina-06.webp` | Los choques frontales de precio (solapamiento por tramos) |
| `pagina-13.webp` | Cómo posicionar una marca: los cuatro tramos |
| `pagina-16.webp` | Conclusión: qué podría hacer una marca y una agencia |

Imagen de tarjeta recomendada: `pagina-01.webp` (la escalera).

## La pregunta

¿Dónde se posiciona en precio cada gran cadena de moda en España y con quién se solapa? ¿Escalona Inditex sus marcas sin pisarse, y dónde chocan con sus rivales?
Para un equipo de marketing o una agencia que tiene que fijar el precio de entrada de una marca y decidir contra quién compararse.

## Qué se compara

- Camiseta de manga larga y vaquero largo, sección mujer. Cada modelo cuenta una vez (las variantes de color no son filas nuevas).
- Prenda básica: camiseta lisa o de canalé, sin estampado; vaquero de cualquier corte, sin rotos, tachas ni estampados.
- Métricas sobre precio de catálogo; marcas con 5 modelos o más por prenda.
- Marcas: Inditex (Lefties, Zara, Massimo Dutti) · Tendam (Springfield, Cortefiel, Pedro del Hierro; Women'secret fuera) · Mango · H&M · Primark · premium española (Desigual, Adolfo Domínguez, Bimba y Lola, Scalpers, El Ganso, Silbon).

## Cifras clave

- **×2:** cada escalón de Inditex cuesta aproximadamente el doble (×1,7 a ×2,0). Tendam repite el patrón un peldaño más arriba.
- **97 %** de solapamiento entre Lefties y Primark en vaqueros: el choque de la gama baja.
- **78 %** entre Mango y Zara en vaqueros: la gama media es un choque a tres con H&M (87 % con Zara).
- Mediana del vaquero básico: Primark 18,00 € · Lefties 19,99 € · Mango 29,99 € · H&M 34,99 € · Zara 35,95 € · Springfield 35,99 € · Massimo Dutti 59,95 € · Cortefiel 59,99 € … hasta Adolfo Domínguez 130,00 €.

## Hallazgos

- **Escalera de Inditex:** Lefties → Zara ×2,0 en camiseta (15,95/7,99), ×1,8 en vaquero (35,95/19,99); Zara → Massimo Dutti ×1,9 y ×1,7. Tendam: Springfield → Cortefiel ×1,7; Cortefiel → Pedro del Hierro ×2,0.
- **Cinco choques frontales**, y en la gama baja sigue habiendo solo uno (Lefties–Primark).
- **H&M rodea a Zara en camisetas** y choca de frente en vaqueros. **El espejismo de la media:** H&M parece más cara que Zara por la media (vaquero 36,38 € vs. 34,41 €) pero no por la mediana (34,99 € vs. 35,95 €): su cola cara sube la media.
- **Cortefiel coincide con Massimo Dutti** a precio de catálogo (91 % en vaqueros) pero con la rebaja se separa (56 %).
- **Por encima de 60 €**, dos niveles: Scalpers en torno a 60–80 €; Desigual, Pedro del Hierro y Adolfo Domínguez en 90–135 €. Ancla de control: 0 % de solapamiento entre este tramo y Primark o Lefties (el método separa bien).
- **Psicología de precio:** en 10 de 20 combinaciones marca-prenda, 3 precios o menos cubren todo el catálogo de básicas. El ,95 es de Zara y Massimo Dutti; el ,99, de H&M, Lefties, Mango, Cortefiel y Springfield.
- **El hueco:** entre Zara y Massimo Dutti (camiseta 17,95–29,95 €, vaquero 39,95–49,95 €) es la zona menos ocupada.
- **Robustez:** al añadir 11 marcas al análisis original, cinco conclusiones se mantienen y dos cambian ("solo dos choques" → cinco; "Massimo Dutti aislado" → Cortefiel coincide con él). Un choque solo se da por bueno si aguanta al cambiar el ancho de tramo y con el precio rebajado: 4 de los 11 solapamientos por encima del 50 % caían 20 puntos o más.

## Cómo posicionar una marca (los cuatro tramos)

1. **Gama baja:** vaquero 18,00–19,99 €, camiseta 7,00–7,99 € → referencia Lefties y Primark.
2. **Gama media:** vaquero 29,99–35,95 €, camiseta 14,99–15,95 € → compararse con Zara, H&M y Mango a la vez.
3. **Gama media-alta:** vaquero 59,95 €, camiseta 29,95 € → Massimo Dutti y Cortefiel (mirar su precio rebajado).
4. **Zona a investigar:** camiseta 17,95–29,95 €, vaquero 39,95–49,95 € → validar demanda antes de decidir.

## Limitaciones

Posicionamiento, no estrategia · foto de un solo día (Springfield tenía el 90 % rebajado y Cortefiel el 41 %) · muestras pequeñas en premium · básicas clasificadas por palabras clave · Shein fuera (protección anti-bot) y Women'secret fuera (sin vaqueros) · cuartiles aproximados con NTILE(4).

## Conclusión

Un mapa del precio de catálogo de 16 cadenas, comprobado con dos métricas, dos anchos de tramo y el precio rebajado, que dice en qué tramo está cada una y con quién comparte precios. No mide ventas ni demanda: es el punto de partida para preguntarlas.
