#!/usr/bin/env python3
"""Comprueba la web antes de publicar. Solo usa la biblioteca estándar de Python (no hay que instalar nada).

Uso (desde la raíz del repositorio):
    python3 herramientas/comprobar-web.py

Revisa en todas las páginas de site/:
  - que existan todos los archivos enlazados (páginas, imágenes, srcset, CSS, JS, PDF, fuentes);
  - que las anclas (#seccion) apunten a un id que existe;
  - un solo <h1>, <title>, meta description y canonical por página;
  - que todas las imágenes tengan texto alternativo (alt);
  - que no quede ningún «[PENDIENTE» visible (en comentarios HTML sí puede estar);
  - que las URL absolutas del propio dominio (canonical, hreflang, og:image, sitemap) existan en local.
Termina con código 1 si encuentra errores, para poder usarlo en una automatización.
"""
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
RAIZ = os.path.normpath(RAIZ)


class Pagina(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.imgs_sin_alt = set(), [], 0
        self.h1, self.title, self.desc, self.canonical = 0, False, False, None
        self.texto, self._ignorar = [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag in ('script', 'style'):
            self._ignorar += 1
        if tag == 'h1':
            self.h1 += 1
        if tag == 'title':
            self.title = True
        if tag == 'meta' and a.get('name') == 'description' and a.get('content'):
            self.desc = True
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a.get('href')
        if tag == 'img' and 'alt' not in a:
            self.imgs_sin_alt += 1
        for attr in ('href', 'src'):
            if a.get(attr):
                self.refs.append((tag, attr, a[attr]))
        for attr in ('srcset', 'imagesrcset'):
            if a.get(attr):
                for parte in a[attr].split(','):
                    url = parte.strip().split(' ')[0]
                    if url:
                        self.refs.append((tag, attr, url))
        if tag == 'meta' and a.get('property', '').startswith('og:image') and a.get('content', '').startswith('http'):
            self.refs.append((tag, 'content', a['content']))

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self._ignorar -= 1

    def handle_data(self, data):
        if not self._ignorar:
            self.texto.append(data)


def paginas():
    for carpeta, _, archivos in os.walk(RAIZ):
        for f in archivos:
            if f.endswith('.html'):
                yield os.path.join(carpeta, f)


def analizar(ruta):
    p = Pagina()
    with open(ruta, encoding='utf-8') as fh:
        p.feed(fh.read())
    return p


def base_del_sitio():
    """El dominio público sale del canonical de la portada (p. ej. https://degallo.github.io/)."""
    canon = analizar(os.path.join(RAIZ, 'index.html')).canonical or ''
    return canon if canon.endswith('/') else canon.rsplit('/', 1)[0] + '/'


def a_archivo_local(url, pagina, base):
    """Convierte un enlace en la ruta del archivo dentro de site/ (o None si es externo)."""
    if url.startswith(base):
        ruta = url[len(base):]
        destino = os.path.join(RAIZ, ruta)
    elif re.match(r'^[a-z]+:', url) or url.startswith('//'):
        return None                       # externo, mailto:, tel:
    elif url.startswith('/'):
        destino = os.path.join(RAIZ, url.lstrip('/'))
    else:
        destino = os.path.join(os.path.dirname(pagina), url)
    partes = urlsplit(destino)
    destino = unquote(partes.path)
    if destino.endswith('/') or os.path.isdir(destino):
        destino = os.path.join(destino, 'index.html')
    return os.path.normpath(destino), partes.fragment


def main():
    base = base_del_sitio()
    errores, avisos = [], []
    cache = {}

    def ids_de(ruta):
        if ruta not in cache:
            cache[ruta] = analizar(ruta).ids
        return cache[ruta]

    todas = sorted(paginas())
    for ruta in todas:
        rel = os.path.relpath(ruta, RAIZ)
        p = analizar(ruta)
        cache[ruta] = p.ids
        if p.h1 != 1:
            errores.append(f'{rel}: tiene {p.h1} <h1> (debe haber uno)')
        if not p.title:
            errores.append(f'{rel}: falta <title>')
        if not p.desc and not rel.startswith('404'):
            errores.append(f'{rel}: falta meta description')
        if p.imgs_sin_alt:
            errores.append(f'{rel}: {p.imgs_sin_alt} imagen(es) sin alt')
        if '[PENDIENTE' in ''.join(p.texto):
            errores.append(f'{rel}: hay un [PENDIENTE] visible (debe ir como comentario HTML)')
        for tag, attr, url in p.refs:
            if url.startswith('#'):
                if url != '#' and url[1:] not in p.ids:
                    errores.append(f'{rel}: el ancla {url} no existe en la página')
                continue
            res = a_archivo_local(url, ruta, base)
            if res is None:
                continue
            destino, frag = res                       # (la 404 usa rutas desde la raíz «/» a propósito)
            if not os.path.exists(destino):
                errores.append(f'{rel}: <{tag} {attr}> apunta a «{url}», que no existe')
            elif frag and destino.endswith('.html') and frag not in ids_de(destino):
                errores.append(f'{rel}: «{url}» apunta a un ancla que no existe')

    # Mapa del sitio
    sitemap = os.path.join(RAIZ, 'sitemap.xml')
    if os.path.exists(sitemap):
        for url in re.findall(r'(?:<loc>|href=")([^<"]+)', open(sitemap, encoding='utf-8').read()):
            res = a_archivo_local(url, sitemap, base)
            if res and not os.path.exists(res[0]):
                errores.append(f'sitemap.xml: «{url}» no corresponde a ningún archivo')
    else:
        avisos.append('No hay sitemap.xml')

    print(f'Dominio detectado: {base}')
    print(f'Páginas revisadas: {len(todas)}')
    for a in avisos:
        print('  aviso:', a)
    if errores:
        print(f'\n{len(errores)} error(es):')
        for e in errores:
            print('  ✗', e)
        sys.exit(1)
    print('Todo correcto: enlaces, imágenes, anclas y metadatos en orden.')


if __name__ == '__main__':
    main()
