# Plantillas de alojamiento

Configuración lista para usar si la web se muda de GitHub Pages. Ninguna hace falta mientras siga
en GitHub Pages. Cómo usar cada una: `documentacion/GUIA-MIGRACION.md`, apartado 10.

| Archivo | Alojamiento | Dónde copiarlo |
|---|---|---|
| `_headers` | Netlify, Cloudflare Pages | Dentro de `site/` |
| `netlify.toml` | Netlify | Raíz del repositorio |
| `vercel.json` | Vercel | Raíz del repositorio |
| `.htaccess` | Apache (cPanel, Plesk, la mayoría de hostings) | Junto al contenido de `site/` |
| `nginx.conf` | Nginx (VPS) | Configuración del servidor |
| `CNAME.ejemplo` | GitHub Pages publicando desde una rama (no con Actions) | `site/CNAME` |
