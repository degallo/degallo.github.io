# Portfolio — Javier Benítez Escobedo

Portfolio web de análisis de datos orientado a reclutadores, en castellano e inglés.
Se publica en GitHub Pages: **https://degallo.github.io/**

## Cómo está organizado

```
├── CLAUDE.md              ← contexto permanente para Claude Code (léelo primero)
├── PENDIENTES.md          ← decisiones y material que faltan
├── PROMPT_INICIAL.md      ← el encargo de la primera sesión (histórico)
├── documentacion/
│   ├── AUDITORIA.md       ← análisis completo de la web (reclutador + técnico), antes/después
│   ├── GUIA-MIGRACION.md  ← cómo llevar la web a otro dominio o alojamiento
│   ├── MANTENIMIENTO.md   ← cómo cambiar textos, el CV, añadir un dashboard o un proyecto
│   └── plantillas/        ← configuración lista para Netlify, Cloudflare, Vercel, Apache, Nginx
├── herramientas/          ← scripts de Python (sin dependencias, salvo el de imágenes)
├── contenido/
│   ├── perfil.md          ← datos del CV: perfil, experiencia, formación, contacto
│   └── proyectos/         ← un .md por proyecto con todas las cifras verificadas
├── referencias/
│   ├── DISENO.md          ← dirección visual (la vigente está al principio)
│   └── capturas/          ← capturas de la plantilla Finox (solo inspiración)
├── site/                  ← LA WEB (lo único que se publica)
│   ├── index.html · proyectos/      ← castellano
│   ├── en/                          ← inglés
│   ├── css/ · js/
│   └── assets/ (fonts/, img/, docs/)
└── .github/workflows/pages.yml  ← publica site/ en GitHub Pages en cada push a main
```

## Ver la web en local

```bash
python3 -m http.server 8000 --directory site
```

Y abre http://localhost:8000.

## Herramientas

| Comando | Para qué |
|---|---|
| `python3 herramientas/comprobar-web.py` | Antes de publicar: enlaces, imágenes, anclas, metadatos y que no quede ningún `[PENDIENTE]` visible |
| `python3 herramientas/subir-version.py` | Después de tocar el CSS o el JS: evita que los navegadores muestren la versión en caché |
| `python3 herramientas/preparar-imagenes.py <carpeta> <slug>` | Proyecto nuevo: versiones de 800/1200 px e imagen para redes (necesita Pillow) |
| `python3 herramientas/cambiar-dominio.py <url> [--aplicar]` | Migrar a otro dominio: cambia todas las URL absolutas de una vez |
| `python3 herramientas/huella-csp.py` | Recalcula la huella del script para la política de seguridad de `_headers` |

## Publicación

GitHub Pages está configurado con "GitHub Actions" como fuente. Cada push a `main` que toque
`site/` vuelve a publicar la web en un par de minutos (pestaña *Actions* para ver el estado).
