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

## TAREA 5 — Paquete de publicación
Para cada vídeo: 10 títulos candidatos (patrones de alta demanda, sin clickbait falso), descripción provisional (con créditos de fuentes), 15 etiquetas, 3 conceptos de miniatura (descripción + prompt para Nano Banana Pro, sin texto en la imagen salvo 3-4 palabras para añadir después) y 3 ideas de capítulos. Salida: `SALIDAS\PUBLICACION_001.md` y `_002.md`.
