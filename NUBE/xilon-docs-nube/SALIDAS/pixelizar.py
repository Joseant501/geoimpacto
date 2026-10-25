#!/usr/bin/env python3
"""
pixelizar.py - Convierte imágenes o carpetas de fotogramas a pixel art ESTABLE para animación.

Dependencias: Pillow + numpy.

Por qué es estable entre fotogramas:
  - La paleta es FIJA (la misma para todos los fotogramas, nada de paleta adaptativa).
  - El dithering es ORDENADO (Bayer), anclado a la rejilla de píxeles: no hay difusión de error,
    así que un píxel que no cambia en la fuente no cambia en la salida.
  - La reducción es por promedio de área (BOX), determinista.

Uso rápido:
  python pixelizar.py foto.jpg                         -> foto_pixel.png (verde, 160 px, 1920x1080)
  python pixelizar.py carpeta_frames -o salida --paleta color --dither 4
  python pixelizar.py foto.jpg --guardar-indice        -> además guarda foto_idx.png (160x90 indexado)
  python pixelizar.py foto_idx.png --remapear color    -> cambia la paleta de un indexado SIN regenerar
"""
import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image

# --- Paletas fijas -----------------------------------------------------------------------------
# Verde fósforo: 4 tonos de #001a08 a #00FF66 (interpolación lineal).
PALETA_VERDE = ["#001a08", "#00661f", "#00b347", "#00ff66"]
# Color retro de 8 tonos (propia del canal; incluye el ámbar #FFB000 del HUD).
PALETA_COLOR = ["#0b0b0f", "#1f2a44", "#5b8fb9", "#2e6b3a",
                "#a8432a", "#d9a066", "#ffb000", "#ece6d3"]
PALETAS = {"verde": PALETA_VERDE, "color": PALETA_COLOR}
EXTENSIONES = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp"}


def hex_a_rgb(lista):
    return np.array([[int(h[i:i + 2], 16) for i in (1, 3, 5)] for h in lista], dtype=np.float32)


def leer_paleta(nombre_o_lista):
    """'verde', 'color' o una lista '#rrggbb,#rrggbb,...' (4-8 colores)."""
    if nombre_o_lista in PALETAS:
        cols = PALETAS[nombre_o_lista]
    else:
        cols = [c.strip() for c in nombre_o_lista.split(",") if c.strip()]
    if not 2 <= len(cols) <= 16:
        sys.exit(f"Paleta con {len(cols)} colores: usa entre 4 y 8 (máx. 16).")
    return hex_a_rgb(cols)


def bayer(n):
    """Matriz de Bayer n x n (n = 2, 4 u 8) normalizada a [-0.5, 0.5)."""
    m = np.array([[0, 2], [3, 1]], dtype=np.float32)
    while m.shape[0] < n:
        m = np.block([[4 * m, 4 * m + 2], [4 * m + 3, 4 * m + 1]])
    return (m + 0.5) / (n * n) - 0.5


def recortar_16_9(img):
    """Recorte centrado a 16:9 (para mantener la proporción del vídeo)."""
    w, h = img.size
    objetivo = 16 / 9
    if abs(w / h - objetivo) < 1e-3:
        return img
    if w / h > objetivo:
        nw = round(h * objetivo)
        x = (w - nw) // 2
        return img.crop((x, 0, x + nw, h))
    nh = round(w / objetivo)
    y = (h - nh) // 2
    return img.crop((0, y, w, y + nh))


def luminancia(rgb):
    return rgb @ np.array([0.299, 0.587, 0.114], dtype=np.float32)


def cuantizar(rgb, paleta, dither, fuerza):
    """Devuelve una matriz de índices (h, w) en la paleta fija.

    - Paleta monocroma (todos los tonos del mismo matiz, p. ej. verde): se cuantiza por luminancia
      a niveles, que es lo más estable y no mete ruido de color.
    - Paleta de color: el color más cercano (distancia RGB ponderada) tras sumar el umbral de Bayer.
    """
    h, w, _ = rgb.shape
    if dither:
        mat = bayer(dither)
        umbral = np.tile(mat, (h // dither + 1, w // dither + 1))[:h, :w]
    else:
        umbral = np.zeros((h, w), dtype=np.float32)

    lum_pal = luminancia(paleta)
    orden = np.argsort(lum_pal)
    # Monocroma = todos los tonos con el mismo matiz (proporción entre canales casi constante).
    croma = paleta / np.maximum(paleta.max(axis=1, keepdims=True), 1)
    es_mono = np.ptp(croma[1:], axis=0).max() < 0.15

    if es_mono:
        n = len(paleta)
        t = luminancia(rgb) / 255.0 * (n - 1)              # rango completo -> n niveles
        nivel = np.clip(np.floor(t + 0.5 + umbral * fuerza), 0, n - 1).astype(np.int64)
        return orden[nivel]

    # Paleta de color: el paso del umbral es aproximadamente la distancia media entre colores.
    paso = 255.0 / max(len(paleta) - 1, 1) * 1.5
    rgb_d = rgb + (umbral * fuerza * paso)[..., None]
    # Distancia "redmean" (aproximación perceptual barata): evita que los verdes de hierba
    # acaben en azul, cosa que pasa con pesos de luminancia porque el azul pesa muy poco.
    dif = rgb_d[:, :, None, :] - paleta[None, None, :, :]
    rmed = (rgb_d[:, :, None, 0] + paleta[None, None, :, 0]) / 2
    dist = ((2 + rmed / 256) * dif[..., 0] ** 2 + 4 * dif[..., 1] ** 2
            + (2 + (255 - rmed) / 256) * dif[..., 2] ** 2)
    return np.argmin(dist, axis=-1)


def a_indexada(indices, paleta):
    img = Image.fromarray(indices.astype(np.uint8), mode="P")
    pal = paleta.astype(np.uint8).flatten().tolist()
    img.putpalette(pal + [0, 0, 0] * (256 - len(paleta)))
    return img


def pixelizar(img, ancho, paleta, dither, fuerza):
    img = recortar_16_9(img.convert("RGB"))
    alto = round(ancho * 9 / 16)
    peq = img.resize((ancho, alto), Image.BOX)             # promedio de área: determinista
    rgb = np.asarray(peq, dtype=np.float32)
    return a_indexada(cuantizar(rgb, paleta, dither, fuerza), paleta)


def remapear(img_idx, paleta_nueva):
    """Cambia la paleta de una imagen YA indexada sin recalcular nada.
    Si el número de colores coincide, índice -> índice (por orden de luminancia, para que
    lo oscuro siga siendo oscuro). Si no coincide, se reparte por rango de luminancia."""
    if img_idx.mode != "P":
        sys.exit("--remapear necesita una imagen indexada (modo P), p. ej. la *_idx.png que genera --guardar-indice.")
    idx = np.asarray(img_idx).astype(np.int64)
    usados = int(idx.max()) + 1
    pal_vieja = np.array(img_idx.getpalette()[:usados * 3], dtype=np.float32).reshape(-1, 3)
    rango_viejo = np.argsort(np.argsort(luminancia(pal_vieja)))      # rango de cada índice viejo
    orden_nuevo = np.argsort(luminancia(paleta_nueva))
    n_v, n_n = len(pal_vieja), len(paleta_nueva)
    rango_nuevo = np.round(rango_viejo * (n_n - 1) / max(n_v - 1, 1)).astype(np.int64)
    tabla = orden_nuevo[rango_nuevo]
    return a_indexada(tabla[idx], paleta_nueva)


def escalar(img_idx, salida):
    w, h = salida
    return img_idx.resize((w, h), Image.NEAREST).convert("RGB")


def parse_tam(s):
    try:
        w, h = s.lower().split("x")
        return int(w), int(h)
    except ValueError:
        raise argparse.ArgumentTypeError("Formato: ANCHOxALTO, p. ej. 1920x1080")


def main():
    ap = argparse.ArgumentParser(description="Pixel art estable para animación (paleta fija + Bayer).")
    ap.add_argument("entrada", help="imagen o carpeta de fotogramas")
    ap.add_argument("-o", "--salida-dir", help="carpeta de salida (por defecto, junto a la entrada)")
    ap.add_argument("--ancho", type=int, default=160, help="ancho en píxeles de arte (def. 160; alto = 16:9)")
    ap.add_argument("--salida", type=parse_tam, default=(1920, 1080), help="tamaño final (def. 1920x1080)")
    ap.add_argument("--paleta", default="verde", help="verde | color | lista '#rrggbb,...' (4-8 colores)")
    ap.add_argument("--dither", type=int, choices=[0, 2, 4, 8], default=4, help="Bayer n x n; 0 = sin dithering (def. 4)")
    ap.add_argument("--fuerza", type=float, default=None, help="intensidad del dithering 0-1.5 (def. 1.0 en verde, 0.6 en color)")
    ap.add_argument("--guardar-indice", action="store_true", help="guarda también *_idx.png (pequeño, indexado) para remapear después")
    ap.add_argument("--remapear", metavar="PALETA", help="NO regenera: toma *_idx.png y le aplica otra paleta")
    ap.add_argument("--sufijo", default=None, help="sufijo del archivo de salida (def. _pixel o _remap)")
    a = ap.parse_args()

    ent = Path(a.entrada)
    archivos = sorted(p for p in ent.iterdir() if p.suffix.lower() in EXTENSIONES) if ent.is_dir() else [ent]
    if not archivos:
        sys.exit("No hay imágenes en la entrada.")
    out_dir = Path(a.salida_dir) if a.salida_dir else (ent if ent.is_dir() else ent.parent)
    out_dir.mkdir(parents=True, exist_ok=True)

    for p in archivos:
        img = Image.open(p)
        if a.remapear:
            idx = remapear(img, leer_paleta(a.remapear))
            suf = a.sufijo or "_remap"
        else:
            fuerza = a.fuerza if a.fuerza is not None else (1.0 if a.paleta == "verde" else 0.6)
            idx = pixelizar(img, a.ancho, leer_paleta(a.paleta), a.dither, fuerza)
            suf = a.sufijo or "_pixel"
            if a.guardar_indice:
                idx.save(out_dir / f"{p.stem}_idx.png")
        escalar(idx, a.salida).save(out_dir / f"{p.stem}{suf}.png")
        print(f"OK  {p.name} -> {p.stem}{suf}.png")


if __name__ == "__main__":
    main()
