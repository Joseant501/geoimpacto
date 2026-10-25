# TAREAS PARA SESIONES EN LA NUBE — Xilon's Earth Docs
Repositorio de SOLO TEXTO (sin claves, sin vídeo). Lee primero `contexto\` (voz de Xilon, reglas del canal, dossier del HUD) y los guiones en `VIDEOS\001 Human Frontiers` y `VIDEOS\002 Human Pets`.
Guardar cada resultado en `SALIDAS\` con el nombre que se indica y hacer commit. NO publicar nada, NO tocar cuentas, NO inventar datos.

## Reglas comunes
- Idioma maestro: INGLÉS; el español se adapta después sin perfección.
- Un solo vídeo con DOS pistas de audio (EN + ES): **en pantalla nunca texto, solo cifras/códigos/símbolos** (formato inglés: 4.1 ¢, 1,716 h).
- Xilon habla con frases cortas, sin contracciones, "Query?" y "Signal continues." (ver `contexto\XILON_VOZ_Y_HABLA.md`).
- Datos solo con fuente y FECHA verificables; lo no verificable se marca "SIN VERIFICAR".
- Diseño: HUD retro CRT estilo Nostromo 1979 (verde #00FF66, ámbar #FFB000), stock con filtro vintage a color. Sin easter eggs.

## TAREA 1 — Verificar datos (la más importante)
Para cada cifra, afirmación o dato de los guiones 001 y 002: buscar fuente primaria, anotar URL, fecha del dato, valor exacto y si el guion lo dice bien (CORRECTO / REDONDEO ACEPTABLE / ERROR / SIN VERIFICAR). Proponer la frase corregida cuando falle. Salida: `SALIDAS\DATOS_VERIFICADOS_001.md` y `_002.md` (tabla: frase del guion | dato | fuente+URL | fecha | veredicto | corrección). Marcar al principio las 5 cifras más arriesgadas.

## TAREA 2 — Consultas de stock para Pictory (una por escena)
Dividir `NARRACION_EN.txt` de cada vídeo en escenas por frases. Para cada escena: 2 consultas LITERALES en inglés (lugar + acción, la escena muestra exactamente lo que dice la frase) y duración sugerida. Reglas: imagen real, cámara documental, sin gráficos/animaciones/texto, sin personas posando a cámara, sin repetir clips, planos de 1-2 s en los primeros 30 s y de 3-5 s después, variar encuadre. Marcar escenas sin stock posible ("SIN CLIP") y proponer plan B. Salida: `SALIDAS\QUERIES_PICTORY_001.md` y `_002.md`.

## TAREA 3 — Hoja de efectos de sonido y música por escena
Por escena de cada vídeo: SFX concretos (estática de señal, zumbido CRT, tecleo mecánico, tracker/radar, blips de interfaz, impacto grave de dato, motivo de tres notas cuando Xilon piensa, whoosh de reacción pop-in/pop-out), con momento exacto (palabra o pausa) y justificación visual; y la música: pieza, tono (intriga documental/futurista analógico, NO intensa), energía 1-5. Reglas: graves primero, agudos ≤5 %, nunca el mismo SFX seguido, ningún SFX sin justificación visual, beeps ≤10 %. Salida: `SALIDAS\CUES_SONIDO_001.md` y `_002.md` + una lista consolidada de efectos a buscar.

## TAREA 4 — Adaptación EN↔ES con presupuesto de palabras
Comparar `NARRACION_EN.txt` y `NARRACION_ES.txt`: palabras por párrafo, relación de duración estimada (EN ≈ 0,375 s/palabra; ES va ~10 % más corta), detectar párrafos donde el ES no cabe en el hueco del EN o se queda corto y proponer recortes/relleno SIN tocar datos. Revisar también que cada cifra aparezca igual en ambos idiomas y que el estilo de Xilon se conserve en español. Salida: `SALIDAS\ADAPTACION_001.md` y `_002.md`.

## TAREA 6 — Pixelizador (script de Python, probado con las imágenes de `muestras\`)
Escribir `SALIDAS\pixelizar.py` (solo Pillow + numpy, sin dependencias raras) que convierta una imagen o una carpeta de fotogramas a pixel art de forma ESTABLE para animación: 1) reducir a un ancho configurable (por defecto 160 px de ancho, mantener proporción 16:9); 2) cuantizar a una paleta FIJA de 4-8 colores (la misma para todos los fotogramas, nada de paleta adaptativa por imagen), con dithering ordenado (Bayer) opcional; 3) reescalar con vecino más cercano al tamaño de salida (por defecto 1920×1080); 4) modo `--paleta verde` (4 tonos de verde fósforo desde #001a08 hasta #00FF66) y modo `--paleta color` (paleta de 8 colores retro); 5) opción para mapear una imagen ya indexada a otra paleta SIN regenerar. Probarlo con las 4 imágenes de `muestras\`, guardar los resultados en `SALIDAS\pixel_pruebas\` en ambos modos y escribir `SALIDAS\PIXEL_NOTAS.md` con qué parámetros se ven mejor (y qué falla: texto, caras, degradados).

## TAREA 7 — Búsqueda de LoRA de pixel art (solo informe, NO descargar nada)
Buscar en Civitai (y otras fuentes fiables) LoRA de pixel art para **SDXL** y para **Flux** compatibles con ComfyUI. Para cada candidato: nombre, URL, modelo base, autor, descargas/valoración, y SU LICENCIA y si permite uso comercial/venta de imágenes generadas (copiar el texto de la licencia). Descartar los que no permitan uso comercial. Salida: `SALIDAS\LORAS_PIXEL.md` con el top 5 y una recomendación.

## TAREA 5 — Paquete de publicación
Para cada vídeo: 10 títulos candidatos (patrones de alta demanda, sin clickbait falso), descripción provisional (con créditos de fuentes), 15 etiquetas, 3 conceptos de miniatura (descripción + prompt para Nano Banana Pro, sin texto en la imagen salvo 3-4 palabras para añadir después) y 3 ideas de capítulos. Salida: `SALIDAS\PUBLICACION_001.md` y `_002.md`.
