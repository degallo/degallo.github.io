# El hueco comercial

- **slug:** `hueco-comercial`
- **Subtítulo:** Dónde hay renta disponible que el comercio local no está aprovechando. Los 277 municipios de Granada y Málaga, medidos uno a uno.
- **Etiqueta:** Análisis territorial · Granada y Málaga
- **Fecha:** agosto 2026
- **Fuentes:** INE — Atlas de Distribución de Renta de los Hogares, Padrón municipal, Directorio Central de Empresas (DIRCE), Encuesta de Presupuestos Familiares 2023 · Instituto Geográfico Nacional (geometría municipal, vía es-atlas) · Delimitación del Área Metropolitana de Granada: POTAUG (2013)
- **Herramientas:** SQL (SQLite, DB Browser) · Looker Studio · mapa coroplético
- **Volumen:** 277 municipios · 34,5 mil M € de renta anual
- **Repositorio:** https://github.com/degallo/huecocomercial (279 líneas de SQL en `consultas.sql`)
- **Informe PDF:** `site/assets/docs/el-hueco-comercial.pdf` (16 páginas)
- **Dashboard interactivo:** [PENDIENTE: enlace público de Looker Studio, si existe]

## Imágenes disponibles (`site/assets/img/proyectos/hueco-comercial/`)

| Archivo | Qué muestra |
|---|---|
| `pagina-01.webp` | Portada: título y silueta de las dos provincias coloreada por municipio |
| `pagina-02.webp` | La pregunta y las cuatro cifras clave (277 · 113 · 103 · 34,5 mil M €) |
| `pagina-04.webp` | Mapa coroplético: renta disponible por comercio en los 277 municipios |
| `pagina-05.webp` | Embudo de filtrado de 277 a 113 municipios candidatos |
| `pagina-10.webp` | Urbanización de lujo: fichas de Benahavís, Casares y Ojén ("Alto ratio, mecanismo distinto") |
| `pagina-11.webp` | Gráfico de burbujas: los tres grupos ocupan zonas que no se solapan |
| `pagina-16.webp` | Conclusión: dos candidatos verificados, no intuidos |

Imagen de tarjeta recomendada: `pagina-04.webp` (el mapa).

## La pregunta

¿Dónde hay dinero que el comercio local no está recogiendo?
En cada municipio vive una cantidad de renta anual. Repartida entre los comercios abiertos da los euros disponibles por negocio. Cuando esa cifra se dispara, o hay poca oferta para el dinero que hay, o ese dinero se está gastando en otro sitio. Para quien decide dónde abrir un negocio o una franquicia.

## Cifras clave

- **277** municipios en el estudio
- **113** candidatos con dato utilizable
- **103** sin cifra por secreto estadístico
- **34,5 mil M €** de renta anual en las dos provincias

## La métrica

**Renta disponible por negocio = (renta por persona × población) ÷ comercios**

- **Qué señala:** poca oferta para el dinero disponible, o dinero que se marcha a gastar fuera. Un ratio alto es una señal de que hay sitio.
- **Qué no es:** no es facturación ni demanda insatisfecha. No todo ese dinero se gasta en comercio local, y el indicador no dice qué ramas faltan.
- **Ejemplo real:** Molvízar (Granada, INE 18133) — renta por persona 10.188 €, población 2.752, renta total 28,0 M €, 32 comercios → **876.168 € por comercio**, el ratio más alto de las dos provincias.

## El embudo: de 277 a 113

| Paso | Municipios | Descarte |
|---|---|---|
| Municipios de Granada y Málaga | 277 | — |
| Con cifra de comercio publicada | 174 | −103 por secreto estadístico |
| Con al menos 30 comercios | 148 | −26 con muestra demasiado pequeña |
| Fuera del cinturón de Granada | 115 | −33 por efecto dormitorio |
| Excluidas las dos capitales | 113 | −2 (Granada y Málaga) |

Los 113 restantes son los únicos donde el ratio se puede leer como señal de mercado y no como artefacto del dato.

## Hallazgos: tres grupos, mismo ratio alto, mecanismos distintos

**Núcleo fuerte** (confirmado por tres métricas): mercado grande, ratio alto y menos comercio del que les correspondería.
- **Rincón de la Victoria** (Málaga): 754.946 € por comercio · ajustada 349.540 € · 51.300 hab. · 1.061 comercios · 20,7 por 1.000 hab. · renta total 801,0 M € · percentiles: ratio P99, escasez P80, volumen P94
- **Antequera** (Málaga): 594.516 € · ajustada 275.261 € · 41.178 hab. · 875 comercios · 21,2 por 1.000 hab. · 520,2 M € · ratio P92, escasez P75, volumen P91
- Entre los municipios de más de 25.000 habitantes, son los de menor densidad de comercio (20,7 y 21,2 por 1.000 hab., frente a 23–32 en el resto).

**Oportunidad de pueblo** (escala de pueblo): el ratio se dispara porque casi no hay tiendas; cabe un negocio, no una cadena. Los cuatro de Granada, entre 2.100 y 7.400 habitantes.
- Molvízar 876.168 € · Valle del Zalabí 690.541 € · Albuñol 666.623 € · Gualchos 587.522 €

**Urbanización de lujo** (mecanismo distinto): renta muy alta y poco comercio, pero porque sus residentes compran en Marbella, a quince minutos. No es una fuga de gasto recuperable.
- Benahavís 715.807 € · Casares 685.568 € · Ojén 598.911 €

Candidato no confirmable: **Guaro** (Málaga), 2.307 habitantes y 24,9 M € de renta, pero el INE oculta su número de comercios.

**Ajuste del gasto:** según la EPF del INE (2023), el 46,3 % del gasto medio va a alimentación, vestido, mobiliario, transporte y restauración. Aplicado como factor constante cambia la escala, no el orden.

**Separación de grupos:** por renta (los pueblos por debajo de 11.500 € por habitante), por volumen (el núcleo arranca en 520 M € de renta total; el lujo no pasa de 132 M €) y por provincia (los cuatro pueblos son de Granada; núcleo y lujo, de Málaga).

**Granada vs. Málaga:** Granada 174 municipios, 930.181 hab., 11,82 mil M €, 21.990 comercios, mediana 485.931 €/comercio, 73 sin cifra (42 %). Málaga 103 municipios, 1.751.600 hab., 22,66 mil M €, 44.527 comercios, mediana 456.133 €, 30 sin cifra (29 %).

## Limitaciones (dichas en voz alta)

1. 103 municipios no se pueden puntuar por secreto estadístico, justo los más pequeños. La lista dice dónde está el mejor hueco entre los que se pueden medir.
2. El grupo de lujo no se separa por renta (Benahavís 14.248 €/hab. vs. Rincón 15.614 €): lo que los separa es el mecanismo y la geografía, un juicio de contexto.
3. Falta lo que decide el negocio: qué ramas faltan, cuánto cuesta un local, cómo se mueve la gente entre municipios.

## Cómo usarlo

Un ratio alto señala dónde mirar, no qué abrir.
- Rincón de la Victoria y Antequera: bajar al detalle por rama de actividad.
- Los cuatro pueblos de Granada: comprobar desplazamientos a la cabecera comarcal antes de decidir.

## Conclusión

Rincón de la Victoria y Antequera son los únicos, de 277 municipios, donde el mercado es grande, la renta es alta y el comercio es insuficiente a la vez, confirmado por tres medidas independientes.
**"277 municipios medidos. Dos confirmados tres veces. Cero basados en intuición."**
