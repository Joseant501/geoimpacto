# Xilon — Dossier de lanzamiento y diseño HUD (24/10/2026)
Origen: conversación con Gemini pegada por Jose + decisiones de Jose el 24/10/2026.

## Decisiones cerradas por Jose
- Diseño: **HUD retro estilo terminal CRT (Nostromo / 1979)**. FIJADO.
- Clips de stock (Pictory/Getty): **filtro de película vintage, NO monocromo** (se conserva el color).
- **Easter eggs: no, de momento** (derechos).
- Idiomas: guiones 1 y 2 ya escritos en inglés y español (inglés = maestro). Dos pistas de audio en el mismo vídeo.

## Estrategia de lanzamiento (cascada, 5-7 días)
- Día 1: Vídeo 1 (el de mayor gancho: dinero/papel, impuestos o enclaves) + tráiler de canal.
- Día 3: Vídeo 2. Día 5 o 7: Vídeo 3. Nada de estrenos simultáneos.
- Tráiler manifiesto (60 s) = vídeo fijado de bienvenida para no suscriptores, no sale como vídeo libre en el feed.
- Banner y estética coherentes con la identidad analógica desde el primer segundo.

## Identidad visual del HUD
- Fondo `#000000` o gris carbón. Texto/líneas verde fósforo `#00FF66`/`#22FF44`. Alertas/paradojas en ámbar `#FFB000`.
- Tipografía `VT323` (matriz de puntos / terminal UNIX), todo en MAYÚSCULAS.
- Capa CRT en DaVinci: scanlines finas, phosphor glow suave, curvatura sutil de tubo (lens distortion) en bordes.
- Plantilla macro reutilizable en DaVinci: fondo = consola; ventana central = stock de Pictory con filtro vintage a color; Xilon en croma superpuesto.

## ⚠️ Conflicto a resolver con la regla "rótulos sin texto, solo cifras" (dos pistas de audio)
Los logs del HUD de la conversación ("SYSTEM_LOG: HUMANO_GASTA_EN_NAVE_MILITAR // LOGICA = CERO") son TEXTO en un idioma: con dos pistas de audio, el rótulo solo vale para una. Para que el mismo vídeo sirva en inglés y español:
- En el HUD usar **códigos, números, símbolos y barras** (ej. `REG-0412`, `ΔT 1716H`, `$ 0.041`, `▮▮▮▯▯`), nunca frases.
- Las frases de log, si se quieren, van en el audio de Xilon, no en pantalla.
- Cifras en formato inglés (4.1 ¢ · 1,716 h).

## Sonido (diseñar en Cubase)
Pitidos de tracker, zumbido de tubo CRT, tecleo mecánico analógico, estática de señal entrando, "tres notas" cuando Xilon piensa, blips de interfaz, golpes de dato. Biblioteca: G:\CLAUDE_EDITS\SOUNDS (comprobar contenido actual; la librería cambia).
