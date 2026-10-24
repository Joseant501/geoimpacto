# REGLAS DEL CANAL — XILON'S EARTH DOCS
Versión 1 · 24/10/2026 (ventana ESTRATEGA, decisiones de Jose).
Documento nuevo. NO sustituye a nada: la voz y el habla de Xilon viven en `XILON_VOZ.md` (raíz del canal, biblia validada con el 001), que manda en todo lo que sea de habla.
Leer este archivo + `XILON_VOZ.md` + `00_DOCS/README_ESTRUCTURA.md` al empezar cualquier ventana del canal.

---

## 1. Qué es el canal
- Documentales y curiosidades humanas contados por Xilon, una criatura alienígena original que estudia a los sapiens. Tono documental con humor tierno.
- Xilon AMA a los humanos: le confunden, pero le fascinan. Asombro y empatía, nunca burla ni superioridad.
- Un solo canal, idioma maestro INGLÉS, con pistas de audio en INGLÉS y ESPAÑOL (función de YouTube de audio en varios idiomas). Un único vídeo para los dos idiomas.
- Separado de Backroom Economy, que es un canal serio. No se mezclan.

## 2. El hueco del canal (datos vidIQ, 23/10/2026)
- No existe ningún DOCUMENTAL contado por un alien. Sí existe un género de FICCIÓN enorme (historias HFY: alienígenas que observan a la humanidad), con vídeos de 100.000 a 1,4 M de vistas en canales pequeños.
- Xilon da a ese público lo mismo pero con datos reales y verificados.

## 3. Cómo se eligen los temas
1. El tema tiene que tener demanda PROBADA: antes de escribir, buscar un viral pasado sobre el asunto (vidIQ).
2. El viral solo prueba la demanda. NUNCA se copia su estructura, su ángulo ni su empaque. El ángulo es siempre el de Xilon.
3. Curiosidades humanas y rarezas del planeta. Sin política de partido. La crítica, si la hay, cae en el sistema, nunca en la gente.
4. Temas en cola:
   - 001 Human Frontiers (fronteras y enclaves): en producción. Demanda: "7 Borders That Make Absolutely No Sense" (326.000 vistas en 1 semana, 20x); en español, "Argentina: 25 Secretos Geográficos…" (1,2 M).
   - Mascotas: psicología de mascotas con 237.000-670.000 vistas; "Your Dog Doesn't Think You're Human", 628.000.
   - Costumbres del mundo por países: 400.000-720.000 vistas ("How Moms Punish Kids in Different Countries", "Never Use These Gestures…").
   - Más adelante: dinero fiat e impuestos (tiran a economía y política; no para el arranque).
   - Aparcado: café (la demanda va sobre todo al ángulo de salud).

## 4. Lanzamiento en cascada
- Nada de estrenos simultáneos.
- Día 1: vídeo 1 (el de más gancho: enclaves y fronteras). Día 3: vídeo 2. Día 5 o 7: vídeo 3.
- Objetivo: que quien llegue con el primero tenga algo más que ver y aprovechar las pantallas finales.
- Antes del día 1 hay que tener los tres vídeos terminados.

## 5. Portada del canal
- Banner y portada coherentes con la estética desde el primer día.
- Tráiler de canal de unos 60 s solo para no suscriptores: PENDIENTE comprobar en Studio que la función sigue disponible. Prioridad baja frente al vídeo 1.

## 6. Identidad visual
- Infografía estilo consola de ciencia ficción clásica (tubo CRT, años 70-80): verde fósforo (#00FF66 / #22FF44) sobre negro o gris carbón muy profundo; ámbar (#FFB000) para alertas y paradojas graves.
- Tipografía de terminal o matriz de puntos (VT323 o monoespaciada), en MAYÚSCULAS.
- Capa CRT en DaVinci: líneas de escaneo finas, resplandor suave del verde y curvatura sutil del tubo en los bordes.
- El METRAJE va EN COLOR, con filtro analógico. El verde monocromo es solo para gráficos, datos y registros.
- Plantilla fija reutilizable en DaVinci: la consola como marco y la ventana central con el metraje procesado.

## 7. Metraje
- Getty / Pictory como base, presentado como "imágenes de vigilancia" captadas por los sensores de la nave de Xilon.
- Cero mapas genéricos sin tratar.
- Clips de Xilon: Veo / ComfyUI, con croma verde #09A847 (ver README_ESTRUCTURA y BIBLIOTECA_REACCIONES).

## 8. Lore y guiños: universo PROPIO
- Prohibido: siluetas, wireframes o mapas de calor de criaturas de otras franquicias, y nombres o códigos de otras franquicias (planetas, empresas, naves). Son propiedad de otros aunque se transformen.
- Sí: homenaje de género sin nombres (estética de consola, sonidos de rastreador, zumbido de tubo, teclado mecánico) y lore propio de Xilon: su planeta (Oolen-7), su nave, sus códigos de registro y sus escalas.
- Registros de la nave con chistes, SIEMPRE con la voz de Xilon (tierna, no fría ni militar). Ejemplo: `SAPIENS GASTA EN NAVE DE GUERRA // XILON TRISTE // NIVEL ABSURDO: 8`.
- Diseño de sonido hecho por Jose en Cubase.

## 9. Producción
- Xilon a cámara: intro, 2 reacciones y cierre. El resto, voz en off.
- Episodios de 8-10 minutos.
- Pídele permiso a Jose antes de instalar, modificar o sobrescribir nada. Copia de seguridad antes de tocar.
- Todo lo pesado va en GPU (RTX 3090): h264_nvenc para codificar y -hwaccel cuda para decodificar; CPU solo si falla la GPU.
- Registrar horas y gasto de cada paso en `00_DOCS/HORAS.md`.
- Decisiones en tipo test numerado. Avisar en tandas cortas, nada de procesos largos en silencio.
- Al cerrar cada sesión: `RESUMEN_SESION_<fecha>_<VENTANA>_XILON.md` con el mensaje para la siguiente ventana.

## 10. PENDIENTE DE DECIDIR (Jose)
1. CONFLICTO: `XILON_VOZ.md` dice "en pantalla solo números, no hay tarjetas de texto" (para que el mismo vídeo sirva a las dos pistas de audio), pero los registros de la nave (punto 8) son texto. Opciones:
   A) Registros solo en inglés (el idioma maestro; el español lo entiende por contexto).
   B) Registros solo con números y símbolos (NIVEL ABSURDO: 8 → ⚠ 8/10).
   C) Sin registros de texto; solo números, como dice la biblia.
2. Tráiler de canal: comprobar si existe la función.
3. Licencia de Getty vía Pictory para montar en DaVinci: Jose lo da por bueno (otro canal suyo está monetizado así).
