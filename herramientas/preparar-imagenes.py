#!/usr/bin/env python3
"""Prepara las imágenes de un proyecto nuevo (o de uno existente si cambias sus páginas).

Necesita Pillow:  python3 -m pip install pillow

Uso (desde la raíz del repositorio):
    python3 herramientas/preparar-imagenes.py site/assets/img/proyectos/<carpeta> <slug-de-la-pagina>

Ejemplo:
    python3 herramientas/preparar-imagenes.py site/assets/img/proyectos/hueco-comercial hueco-comercial

Qué hace con cada «pagina-NN.webp» de la carpeta (exportadas a 1600×900 desde el informe):
  - crea «pagina-NN-800.webp» y «pagina-NN-1200.webp» (el navegador elige la que necesita);
  - crea la imagen para compartir en redes «site/assets/img/og/<slug>.jpg» (1200×630) a partir
    de «pagina-01.webp» (LinkedIn y WhatsApp no siempre muestran WebP).
No modifica ni borra los originales.

Si partes de PNG o JPG, conviértelos antes a WebP de 1600×900, por ejemplo con:
    python3 -c "from PIL import Image; Image.open('pagina-01.png').convert('RGB').resize((1600,900)).save('pagina-01.webp', quality=82, method=6)"
"""
import os
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit('Falta Pillow. Instálalo con:  python3 -m pip install pillow')

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    carpeta, slug = sys.argv[1], sys.argv[2]
    originales = sorted(f for f in os.listdir(carpeta)
                        if f.startswith('pagina-') and f.endswith('.webp') and f.count('-') == 1)
    if not originales:
        sys.exit(f'No hay archivos pagina-NN.webp en {carpeta}')
    for f in originales:
        im = Image.open(os.path.join(carpeta, f))
        if im.size != (1600, 900):
            print(f'  aviso: {f} mide {im.size[0]}×{im.size[1]}; se esperaba 1600×900')
        for ancho in (800, 1200):
            alto = round(im.height * ancho / im.width)
            destino = os.path.join(carpeta, f.replace('.webp', f'-{ancho}.webp'))
            im.resize((ancho, alto), Image.LANCZOS).save(destino, 'WEBP', quality=82, method=6)
        print(f'  {f}: creadas las versiones de 800 y 1200 px')

    portada = os.path.join(carpeta, 'pagina-01.webp')
    if os.path.exists(portada):
        im = Image.open(portada).convert('RGB')
        alto = round(im.width / 1.905)                       # proporción 1200×630
        arriba = max(0, (im.height - alto) // 2)
        og = im.crop((0, arriba, im.width, arriba + alto)).resize((1200, 630), Image.LANCZOS)
        destino = os.path.join(RAIZ, 'site', 'assets', 'img', 'og', f'{slug}.jpg')
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        og.save(destino, 'JPEG', quality=84, optimize=True, progressive=True)
        print(f'  imagen para redes: {os.path.relpath(destino, RAIZ)}')


if __name__ == '__main__':
    main()
