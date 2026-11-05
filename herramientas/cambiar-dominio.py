#!/usr/bin/env python3
"""Cambia el dominio público de la web en todos los archivos de site/ (para migrar).

Las rutas internas de la web son relativas y no hay que tocarlas. Lo único que lleva el dominio
escrito son las URL absolutas que leen Google y las redes sociales: canonical, hreflang,
Open Graph (og:url, og:image), datos estructurados (JSON-LD), sitemap.xml y robots.txt.

Uso (desde la raíz del repositorio):
    python3 herramientas/cambiar-dominio.py https://javierbenitez.es/            # simulación: solo cuenta
    python3 herramientas/cambiar-dominio.py https://javierbenitez.es/ --aplicar  # hace el cambio

El dominio actual se detecta solo (canonical de site/index.html).
Después, ejecuta herramientas/comprobar-web.py y revisa el diff con git antes de publicar.
"""
import os
import re
import sys

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site'))
EXTENSIONES = ('.html', '.xml', '.txt', '.webmanifest', '.json')


def dominio_actual():
    html = open(os.path.join(RAIZ, 'index.html'), encoding='utf-8').read()
    m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    if not m:
        sys.exit('No encuentro el canonical en site/index.html')
    url = m.group(1)
    return url if url.endswith('/') else url.rsplit('/', 1)[0] + '/'


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    aplicar = '--aplicar' in sys.argv
    if len(args) != 1 or not re.match(r'^https://[^/]+(/.*)?$', args[0]):
        sys.exit(__doc__)
    nuevo = args[0] if args[0].endswith('/') else args[0] + '/'
    viejo = dominio_actual()
    if nuevo == viejo:
        sys.exit(f'La web ya usa {viejo}')

    total = 0
    for carpeta, _, archivos in os.walk(RAIZ):
        for f in archivos:
            if not f.endswith(EXTENSIONES):
                continue
            ruta = os.path.join(carpeta, f)
            texto = open(ruta, encoding='utf-8').read()
            n = texto.count(viejo)
            if n:
                total += n
                print(f'  {os.path.relpath(ruta, RAIZ):55} {n:3} cambio(s)')
                if aplicar:
                    with open(ruta, 'w', encoding='utf-8') as fh:
                        fh.write(texto.replace(viejo, nuevo))

    print(f'\n{viejo}  →  {nuevo}')
    print(f'{total} apariciones {"cambiadas" if aplicar else "encontradas (simulación: añade --aplicar para cambiarlas)"}.')
    if '/' in nuevo.split('://', 1)[1].rstrip('/'):
        print('\nAVISO: el nuevo dominio incluye una subcarpeta. La página 404.html usa rutas desde la raíz '
              '(«/», «/en/», «/favicon.svg»); cámbialas a mano por la subcarpeta nueva.')


if __name__ == '__main__':
    main()
