# Rentabilidad del alquiler turístico legal en Barcelona

- **slug:** `alquiler-turistico-barcelona`
- **Subtítulo:** Quedan 29 meses de licencia HUTB. ¿En qué barrios renta de verdad un piso turístico legal, y en cuáles solo lo parecía?
- **Etiqueta:** Análisis de mercado · Inside Airbnb
- **Fecha:** agosto 2026 (snapshot del 25 de junio de 2026)
- **Fuentes:** Inside Airbnb, snapshot de Barcelona del 25/06/2026 (15.293 anuncios) · Cartografía de barrios y distritos: Ajuntament de Barcelona vía bcn-geodata
- **Herramientas:** SQL (SQLite) · Looker Studio · mapas coropléticos
- **Volumen:** 15.293 anuncios → 6.520 pisos HUTB comparables · 48 barrios
- **Repositorio:** [PENDIENTE: no existe repositorio público; ver PENDIENTES.md]
- **Informe PDF:** `site/assets/docs/alquiler-turistico-barcelona.pdf` (19 diapositivas, convertido desde el .pptx original)
- **Dashboard interactivo:** [PENDIENTE: enlace público de Looker Studio, si existe]

## Imágenes disponibles (`site/assets/img/proyectos/alquiler-turistico-bcn/`)

| Archivo | Qué muestra |
|---|---|
| `pagina-01.webp` | Portada |
| `pagina-02.webp` | La pregunta de negocio y las cifras clave (15.293 · 6.520 · 57 % · 242 M) |
| `pagina-07.webp` | Mapa de ingreso anual por piso HUTB por barrio + top 10 |
| `pagina-08.webp` | Embudo de 15.293 anuncios a 6.520 pisos comparables |
| `pagina-13.webp` | Dispersión por barrio con las dos métricas: "la métrica creaba la incompatibilidad" |
| `pagina-19.webp` | Conclusión: "El mapa del negocio cambia al cambiar la forma de medirlo" |

Imagen de tarjeta recomendada: `pagina-07.webp` (el mapa).

## Aviso sobre la moneda

El informe usa "$" porque Inside Airbnb formatea la columna `price` con el símbolo $, pero
en Barcelona los precios están en la moneda local. [PENDIENTE: Javi debe confirmarlo; si son
euros, en la web usar €.] Mientras tanto, en la web escribir las cifras sin símbolo de moneda
ambiguo o con "€" solo si Javi lo confirma.

## La pregunta de negocio

¿Dónde concentrar las licencias que quedan antes de noviembre de 2028?
El 24 de noviembre de 2028 se extinguen todas las licencias HUTB de Barcelona (el Plan Especial no las renueva y el Tribunal Constitucional avaló la medida). Una gestora de alquiler turístico tiene que decidir hoy en qué pisos invierte reforma, captación y equipo, y de cuáles salir antes.

## Cifras clave

- **15.293** anuncios activos en Barcelona
- **6.520** pisos HUTB con dato usable
- **57 %** del universo se descarta por precio, licencia o tipo de alojamiento
- **242 M** de ingreso anual estimado del mercado HUTB legal

## El mercado hoy

De 13.355 anuncios con precio, solo el **48,7 %** tiene licencia HUTB (7.195 anuncios, los que desaparecen en 2028). El **25,4 %** ya está en alquiler de temporada, una figura que 2028 no toca. El 19,9 % no declara información (no necesariamente irregular).

## La métrica y su ajuste

**Ingreso anual estimado = precio por noche × (365 − noches disponibles)**
- **Señala:** el techo de ingreso bruto si cada noche bloqueada fuese una noche vendida.
- **No es:** beneficio (no descuenta gestión, limpieza, comisiones ni impuestos) ni ocupación real.
- **Caso real:** un ático en Sarrià a 451 la noche, 31 noches disponibles, 0 reseñas en 12 meses, última reseña abril de 2024 → 150.634 al año según la fórmula. Ese piso, él solo, colocaba a Sarrià como el barrio más rentable.

**Ajuste:** se sustituye el calendario por la estimación de ocupación basada en el ritmo de reseñas (Inside Airbnb).
- 395 pisos HUTB (6,0 %) tienen el calendario cerrado más de 200 noches y casi ninguna reseña; 129, ninguna en 12 meses. Aportan 29,5 M al año con la fórmula del panel (12,1 % del mercado) y 1,3 M con el modelo de reseñas.
- Correlación entre las dos estimaciones de noches ocupadas: **0,15**.
- En total casi coinciden (244,0 M vs. 241,5 M, un 1 %), pero barrio a barrio no: correlación de rangos **0,31**.

## El embudo

De 15.293 anuncios → 13.355 con precio → 7.195 con licencia HUTB → 6.548 vivienda entera → **6.520** en barrios con 5 pisos HUTB o más. Los 13 barrios descartados suman 28 anuncios.

## Top 10 barrios (ingreso anual por piso, corregido · nº de pisos)

1. Diagonal Mar 47.739 · 73
2. Sant Martí de Provençals 45.970 · 11
3. la Dreta de l'Eixample 45.505 · 1.081
4. el Fort Pienc 45.311 · 238
5. l'Antiga Esquerra 44.671 · 378
6. la Sagrada Família 43.350 · 559
7. el Camp d'en Grassot 42.777 · 123
8. la Vila Olímpica 41.672 · 65
9. la Vila de Gràcia 39.744 · 461
10. el Parc i la Llacuna 39.699 · 85

Mediana de los 48 barrios: 31.967. Entre el primero y el último, 23 veces de diferencia.

## Hallazgos: tres grupos, tres mecanismos

- **Motor del Eixample** (confirmado por las dos métricas): 5 barrios contiguos (Dreta de l'Eixample, Fort Pienc, Antiga Esquerra, Sagrada Família, Camp d'en Grassot) con 2.379 pisos HUTB y una media de 44.700 al año por piso; ninguno baja de 42.700.
- **Nichos al alza:** barrios que el panel infravaloraba (Diagonal Mar, Sant Martí de Provençals, Hostafrancs, el Camp de l'Arpa, la Salut). Suben entre 8 y 26 puestos al corregir. Diagonal Mar, con 73 pisos, es el más sólido y el primero de la ciudad.
- **Trampas del calendario:** los que más caen al corregir (el Besòs i el Maresme, Sarrià, el Clot, les Corts, la Verneda). Sarrià pasa de 67.870 a 26.100 por piso; sin el ático, 51.317.
- **La métrica creaba la incompatibilidad, no el mercado:** con el modelo de reseñas, la correlación entre número de pisos e ingreso por piso pasa de 0,16 a 0,48.
- **Triangulación:** un particular con un solo piso ingresa 47.021 al año; una cartera de más de 20 pisos, 31.077 (un 34 % menos por unidad). El precio por noche es plano (285–298); lo que cae es la ocupación, las reseñas y el sello superhost (del 55 % al 15 %).
- **Por distrito:** Eixample concentra 3.073 de los 6.520 pisos (47 %) y el ingreso por piso más alto (41.600). Ciutat Vella rinde menos de lo supuesto (31.116). Les Corts es donde más se desvía el calendario (41.073 vs. 26.460).

## Limitaciones

1. Es ingreso bruto, no beneficio.
2. El modelo de reseñas topa la ocupación en el 70 % del año: subestima a los mejores.
3. Es una foto de junio de 2026, no una serie.
4. Las medias de barrios pequeños siguen siendo frágiles (Sarrià y la Verneda: 6 pisos).
5. Es inteligencia de mercado, no sustituye los datos internos de una cartera.

## Cómo usarlo: tres decisiones con criterio de parada

1. **Concentrar la retención en el corredor del Eixample** (2.379 pisos). Parada: si el ingreso por piso del bloque cae por debajo de 40.000 en el siguiente snapshot, revisar la tesis.
2. **Sondear los nichos antes de que suban de precio** (Diagonal Mar, el Camp de l'Arpa). Parada: no comprometer capital en barrios de menos de 50 pisos sin confirmar con datos propios.
3. **Sacar del plan los barrios que solo lo parecían.** Parada: reincorporar solo si un histórico de reservas propio contradice la señal de reseñas.

## Conclusión

**"El mapa del negocio cambia al cambiar la forma de medirlo."** Los 242 M del mercado HUTB legal son los mismos con una métrica y con otra; lo que cambia es a qué barrio se atribuyen. Fiable porque dos estimaciones con fuentes de error distintas coinciden en el agregado y los desacuerdos caen donde eran previsibles: en los barrios de pocos pisos.
