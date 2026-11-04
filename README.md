# Portfolio — Javier Benítez Escobedo

Portfolio web de análisis de datos orientado a reclutadores. Se publica en GitHub Pages:
**https://degallo.github.io/**

## Cómo está organizado

```
├── CLAUDE.md              ← contexto permanente para Claude Code (léelo primero)
├── PROMPT_INICIAL.md      ← el prompt para arrancar la sesión que construye la web
├── PENDIENTES.md          ← decisiones y material que faltan
├── contenido/
│   ├── perfil.md          ← datos del CV: perfil, experiencia, formación, contacto
│   └── proyectos/         ← un .md por proyecto con todas las cifras verificadas
├── referencias/
│   ├── DISENO.md          ← dirección visual y adaptación de la plantilla de referencia
│   └── capturas/          ← capturas de la plantilla Finox (solo inspiración)
├── site/                  ← LA WEB (lo único que se publica)
│   └── assets/
│       ├── img/           ← foto de perfil e imágenes de cada proyecto (.webp)
│       └── docs/          ← informes PDF de los proyectos
└── .github/workflows/pages.yml  ← publica site/ en GitHub Pages en cada push a main
```

## Cómo empezar

1. Abre Claude Code en la web (claude.ai/code) y elige este repositorio.
2. Copia el bloque de `PROMPT_INICIAL.md` y pégalo como primer mensaje.
3. Revisa `PENDIENTES.md` en paralelo: algunas cosas (CV sin dirección, moneda de Barcelona)
   conviene resolverlas antes de publicar.

## Publicación

GitHub Pages está configurado con "GitHub Actions" como fuente. Cada push a `main` que toque
`site/` vuelve a publicar la web en un par de minutos (pestaña *Actions* para ver el estado).
