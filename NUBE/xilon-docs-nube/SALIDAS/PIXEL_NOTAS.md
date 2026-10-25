# PIXEL_NOTAS · pixelizar.py (TAREA 6)
25/10/2026

## ⚠️ Aviso importante: no se ha probado con las imágenes de `muestras\`
La carpeta `muestras\` **no está en el repositorio** ni se ha subido a la sesión. Por eso las pruebas se hicieron con **4 imágenes sintéticas**, generadas a propósito para forzar los casos difíciles. Están en `pixel_pruebas/fuentes_sinteticas/`, junto al script que las genera (`generar_muestras.py`):

| Muestra | Para qué sirve |
|---|---|
| `01_degradado.png` | Degradado de cielo + sol + montañas (prueba los **degradados**) |
| `02_texto.png` | Texto grande, cifras y texto pequeño (prueba el **texto**) |
| `03_cara.png` | Cara ilustrada con piel, ojos y sombra suave (prueba las **caras**) |
| `04_foto_textura.png` | Textura con ruido y manchas tipo foto de paisaje (prueba la **foto real**) |

**Pendiente:** subir las 4 imágenes de `muestras\` a `NUBE/xilon-docs-nube/muestras/` y ejecutar:
```
python pixelizar.py muestras -o SALIDAS/pixel_pruebas --paleta verde --sufijo _verde --guardar-indice
python pixelizar.py muestras -o SALIDAS/pixel_pruebas --paleta color --sufijo _color
```

## Cómo funciona (y por qué es estable en animación)
1. **Recorte centrado a 16:9** y reducción por **promedio de área** (BOX) al ancho elegido. Por defecto, 160 × 90.
2. **Paleta fija** (la misma en todos los fotogramas):
   - `--paleta verde`: 4 tonos `#001a08 · #00661f · #00b347 · #00ff66`. Se cuantiza por **luminancia**, así que no mete ruido de color.
   - `--paleta color`: 8 tonos retro propios, con el ámbar del HUD: `#0b0b0f #1f2a44 #5b8fb9 #2e6b3a #a8432a #d9a066 #ffb000 #ece6d3`. Usa el color más cercano con distancia perceptual ("redmean").
   - `--paleta "#rrggbb,..."`: paleta propia de 4-8 colores.
3. **Dithering Bayer ordenado** (`--dither 2|4|8`, o `0` para quitarlo). Va anclado a la rejilla, sin difusión de error: un píxel que no cambia en la fuente no cambia en la salida.
4. **Reescalado por vecino más cercano** a `--salida` (por defecto 1920×1080).
5. **`--guardar-indice`** guarda la versión pequeña indexada (`*_idx.png`, 160×90). **`--remapear PALETA`** le cambia la paleta **sin regenerar** nada: se ordena por luminancia, para que lo oscuro siga siendo oscuro. También funciona entre paletas de distinto tamaño (4 → 8).

**Prueba de estabilidad:** 24 fotogramas con una bola que se mueve sobre un fondo fijo → **0,0 %** de píxeles cambiados en la zona estática entre fotogramas, en los dos modos.

## Resultados en `pixel_pruebas/`
- `*_verde.png` y `*_color.png`: las 4 muestras en los dos modos (1920×1080).
- `*_idx.png`: índices de 160×90 (modo verde).
- `01_degradado_idx_remap_a_color.png`: el índice verde remapeado a color sin regenerar.
- `02_texto_color_320.png`: el texto con `--ancho 320`, para comparar.

## Parámetros que mejor se ven

| Uso | Recomendado | Por qué |
|---|---|---|
| HUD / "imagen de vigilancia" verde | `--paleta verde --ancho 160 --dither 4` (fuerza 1.0, por defecto) | Los degradados quedan suaves con Bayer 4 y la silueta se lee bien. Es el look CRT del canal. |
| Stock a color con estética retro | `--paleta color --ancho 160 --dither 4 --fuerza 0.6` (por defecto en color) | Con fuerza 1.0 aparece una "trama" de puntos claros sobre la piel y el cielo; con 0.6 queda limpio sin perder el degradado. |
| Planos con texto o cifras importantes | `--ancho 320` | A 160 px el texto grande se lee, pero el pequeño se rompe. |
| Planos muy planos (cielo liso, ilustración) | `--dither 0` o `--dither 2` | Sin dithering quedan franjas limpias de color (look más "16 bits"). |
| Ruido / foto con mucho grano | `--fuerza 0.5` y un desenfoque suave antes (en DaVinci) | Si no, el grano se convierte en "polvo" de colores sueltos. |

## Qué falla (y cómo esquivarlo)
- **Texto:** el texto pequeño (<~40 px de alto en 1080p) es ilegible a 160 px. El grande sí aguanta. Como en pantalla solo van cifras, conviene ponerlas **después** del pixelizado, como capa HUD nítida, y no pixelizarlas.
- **Caras:** a 160 px, una cara que ocupa 1/3 de la altura se queda en ojos + boca; la nariz y los rasgos suaves desaparecen, sobre todo con fuerza 0.5. Para planos de cara: `--ancho 240-320`, o encuadrar más cerca. En verde, la piel y el fondo pueden caer en el mismo tono si tienen luminancia parecida.
- **Degradados:** sin dithering salen bandas muy marcadas (en verde, el cielo queda en 2-3 franjas). Con Bayer 4 están bien. Con Bayer 8 la trama se nota más (patrón de "rejilla") en planos fijos grandes.
- **Paleta color y naturaleza:** con solo 8 tonos, los verdes medios de hierba y los azules grises se mezclan con tramas. Si un vídeo es casi todo paisaje, compensa una paleta propia con un verde medio, por ejemplo cambiando `#1f2a44` por `#6a9a4a` en `--paleta "..."`.
- **Grano y ruido de la fuente:** el ruido de vídeo de stock genera píxeles sueltos que cambian entre fotogramas. **No es inestabilidad del script:** es que la fuente cambia. Hay que reducir el ruido antes (DaVinci → Noise Reduction temporal).
- **Recorte 16:9:** las fuentes verticales u otras proporciones se recortan al centro. Si importa el encuadre, hay que reencuadrar antes.

## Rendimiento
Medido en esta sesión: 24 fotogramas 1080p en unos 2 s (≈ 0,08 s por fotograma; casi todo es leer y escribir PNG de 1080p). Una carpeta de 1.000 fotogramas tardaría unos 1,5 min en CPU. No necesita GPU.
