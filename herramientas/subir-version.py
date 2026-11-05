#!/usr/bin/env python3
"""Sube la versión de CSS y JS (?v=10 → ?v=11) en todas las páginas de site/.

Para qué sirve: los navegadores guardan styles.css y main.js en caché. Si cambias alguno de los
dos y no cambias la versión, un reclutador que ya hubiera entrado podría ver la web con el CSS
viejo. Ejecútalo cada vez que toques css/styles.css o js/main.js, antes de publicar.

Uso (desde la raíz del repositorio):
    python3 herramientas/subir-version.py
"""
import glob
import os
import re

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site'))
PATRON = re.compile(r'((?:styles\.css|main\.js)\?v=)(\d+)')


def main():
    paginas = glob.glob(os.path.join(RAIZ, '**', '*.html'), recursive=True)
    versiones = set()
    for ruta in paginas:
        with open(ruta, encoding='utf-8') as fh:
            versiones.update(int(m.group(2)) for m in PATRON.finditer(fh.read()))
    if not versiones:
        raise SystemExit('No encuentro ninguna versión ?v=N en las páginas.')
    nueva = max(versiones) + 1
    cambiadas = 0
    for ruta in paginas:
        with open(ruta, encoding='utf-8') as fh:
            texto = fh.read()
        nuevo = PATRON.sub(lambda m: f'{m.group(1)}{nueva}', texto)
        if nuevo != texto:
            with open(ruta, 'w', encoding='utf-8') as fh:
                fh.write(nuevo)
            cambiadas += 1
    print(f'Versión {max(versiones)} → {nueva} en {cambiadas} páginas.')


if __name__ == '__main__':
    main()
