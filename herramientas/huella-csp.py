#!/usr/bin/env python3
"""Calcula la huella (sha256) de los <script> incrustados en las páginas, para la política de
seguridad (Content-Security-Policy) de documentacion/plantillas/_headers.

Solo hace falta si cambias el <script> de una línea que hay en el <head> de cada página
y publicas en un alojamiento que use esas cabeceras (Netlify, Cloudflare Pages…).

Uso (desde la raíz del repositorio):
    python3 herramientas/huella-csp.py
Copia el resultado en la línea Content-Security-Policy, dentro de script-src.
"""
import base64
import glob
import hashlib
import os
import re

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site'))

huellas = {}
for ruta in glob.glob(os.path.join(RAIZ, '**', '*.html'), recursive=True):
    with open(ruta, encoding='utf-8') as fh:
        for m in re.finditer(r'<script>(.*?)</script>', fh.read(), flags=re.S):
            h = "'sha256-" + base64.b64encode(hashlib.sha256(m.group(1).encode('utf-8')).digest()).decode() + "'"
            huellas.setdefault(h, []).append(os.path.relpath(ruta, RAIZ))

for h, paginas in huellas.items():
    print(f'{h}   ({len(paginas)} páginas)')
if len(huellas) > 1:
    print('\nAviso: no todas las páginas tienen el mismo script; añade todas las huellas a script-src.')
