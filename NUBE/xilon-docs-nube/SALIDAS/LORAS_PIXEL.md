# LORAS_PIXEL · LoRA de pixel art para SDXL y Flux (TAREA 7)
25/10/2026 · **Solo informe. No se ha descargado nada.**

## ⚠️ Límite de esta búsqueda (leer primero)
- Desde esta sesión **no se puede abrir Civitai** (la red lo bloquea) y solo había buscador web. Lo que se sabe de cada modelo viene de resultados de búsqueda, de espejos (CivArchive, PromptLayer, comfy.icu) y de fichas de Hugging Face.
- **No se han podido leer las casillas de permisos de Civitai** ("Sell images they generate", "Use without crediting", "Run on services"…) de ningún modelo. Cuando un dato no está confirmado en la fuente original, pone **SIN VERIFICAR**.
- Las cifras de descargas son de espejos o capturas antiguas, y pueden no coincidir con las actuales.
- **Antes de usar cualquiera:** abrir su página (Civitai o Hugging Face), mirar el bloque de licencia y las casillas, hacer captura con fecha y guardarla en `00_DOCS`.

## Cómo afecta la licencia del modelo base

| Base | Licencia | ¿Imágenes generadas para uso comercial? | Texto clave (copiado de la fuente) |
|---|---|---|---|
| **SDXL 1.0** | CreativeML **Open RAIL++-M** (24/11/2022) | **Sí**, con las restricciones de uso de la licencia (nada ilegal, dañino, etc.) | Cláusula de "Output" de la familia CreativeML Open RAIL: *"Licensor claims no rights in the Output You generate using the Model. You are accountable for the Output you generate and its subsequent uses. No use of the output can contravene any provision as stated in the License."* Fuente: licencia de Stable Diffusion (https://huggingface.co/spaces/CompVis/stable-diffusion-license) · copia de Open RAIL++-M: https://open.windriver.com/info/uni-license-list/licenses/bigscience-open-rail-m2.html |
| **FLUX.1 [dev]** | FLUX [dev] **Non-Commercial License v2.0** (actualizada el 25/11/2025) | **Las imágenes, sí; el modelo, no.** El texto v2.0 permite usar las imágenes "para cualquier fin, incluido el comercial", pero el modelo solo puede usarse con fines no comerciales. BFL vende una licencia comercial *self-hosted* (desde junio de 2025, según una guía de terceros: SIN VERIFICAR en BFL). | *"You may use Output for any purpose (including for commercial purposes), except as expressly prohibited herein."* Prohibido usar las imágenes para entrenar o destilar un modelo que compita con FLUX [dev]. Fuente: https://bfl.ai/legal/non-commercial-license-terms · ficha: https://huggingface.co/black-forest-labs/FLUX.1-dev |
| **FLUX.1 [schnell]** | Apache 2.0 | Sí, sin restricciones relevantes | No se ha encontrado **ningún LoRA de pixel art para schnell** con licencia clara |

**Lectura para el canal:** el canal está monetizado, así que es uso comercial. **SDXL es la vía limpia.** Con Flux dev, las imágenes se pueden usar comercialmente según el texto v2.0, pero *ejecutar* el modelo dentro de una actividad comercial es una zona gris; el propio foro de Hugging Face tiene un hilo sobre esa ambigüedad (https://huggingface.co/black-forest-labs/FLUX.1-dev/discussions/136). Esto no es asesoramiento legal.

## Top 5 (provisional, a falta de ver las casillas de Civitai)

| # | Nombre | URL | Base | Autor | Descargas / valoración | Licencia (según la fuente) | ¿Uso comercial de imágenes? |
|---|---|---|---|---|---|---|---|
| 1 | **PixelArtRedmond** (versión SDXL) | https://civitai.com/models/144684/pixelartredmond-pixel-art-loras | SDXL 1.0 (la página de Civitai tiene ahora también una versión Qwen-Image) | artificialguybr | No consta (SIN VERIFICAR) | CreativeML OpenRAIL-M según PromptLayer (https://www.promptlayer.com/models/pixelartredmond). Ojo: este autor usa otras licencias en otros modelos ("bespoke-lora-trained-license"). | Probable **sí** por la licencia, pero las casillas de Civitai están SIN VERIFICAR |
| 2 | **pixel-art-sdxl-dora-v0-9** | https://huggingface.co/thliang01/pixel-art-sdxl-dora-v0-9 | SDXL (es un DoRA, variante de LoRA) | thliang01 | No consta | **openrail++** (etiqueta de la ficha HF) | **Sí**, según Open RAIL++-M. Comprobar que la versión de ComfyUI de Jose carga DoRA |
| 3 | **Flux 2D Game Assets LoRA** | https://huggingface.co/gokaygokay/Flux-2D-Game-Assets-LoRA | FLUX.1 [dev] | gokaygokay | ~880-895 descargas en CivArchive; 1,8 K ejecuciones en Replicate | Apache-2.0 según PromptLayer (https://www.promptlayer.com/models/flux-2d-game-assets-lora). **Pero la base es dev:** el LoRA no puede "relicenciar" el modelo base. | Imágenes: sí según la v2.0 de FLUX dev; modelo: no comercial. Orientado a *assets* de juego (palabra activadora "GRPZA"), no a planos de documental |
| 4 | **Retro Pixel Flux LoRA** | https://huggingface.co/prithivMLmods/Retro-Pixel-Flux-LoRA | FLUX.1 [dev] | prithivMLmods | 492 descargas en el último mes (ficha HF) | CreativeML OpenRAIL-M según PromptLayer (https://www.promptlayer.com/models/retro-pixel-flux-lora); la base dev es no comercial | Como el anterior. El autor avisa: "not the final version and may contain artifacts" |
| 5 | **Pixel Art Illustrations FLUX** | https://civitai.com/models/683579/pixel-art-illustrations-flux | FLUX.1 [dev] | No consta en las fuentes | 908 descargas (espejo CivArchive, v1.2) | FLUX.1 [dev] Non-Commercial License (listado en Civitai) | Imágenes: sí según la v2.0; casillas de Civitai SIN VERIFICAR. Su autor dice que va mejor en **paisajes**, que es lo que necesita el canal |

## Descartados

| Nombre | URL | Motivo |
|---|---|---|
| Pixel Art XL (SDXL) | https://civitai.com/models/120096/pixel-art-xl · HF: https://huggingface.co/nerijs/pixel-art-xl | **Probablemente prohíbe vender imágenes en Civitai.** Un blog japonés que copia sus casillas (https://note.com/taziku/n/ne0ddd358f547) lo marca como NO permitido, aunque en HF figure como creativeml-openrail-m. Es el más descargado (~107 K en CivArchive), pero hay conflicto entre plataformas: **descartado** salvo que Jose vea en Civitai la casilla "Sell images" marcada |
| Pixel-Art-Kontext-Dev | https://civitai.com/models/1756882/pixel-art-kontext-dev | El creador **prohíbe expresamente el uso comercial** |
| Modern pixel art (FLUX) | https://civitai.com/models/783743/modern-pixel-art | FLUX dev NC; no se encontró autor, descargas ni casillas. No se puede valorar |
| RD Pixel Art Lora (FLUX) | https://civitai.com/models/646820/rd-pixel-art-lora | FLUX dev NC; sin datos de casillas ni de autor |
| Pixel game assets [FLUX] by Dever | https://civitai.com/models/945266/pixel-game-assets-flux-by-dever | FLUX dev NC; enfocado a *assets* de juego; sin datos |
| pixelartdotfluxlora | https://huggingface.co/deAPI-ai/pixelartdotfluxlora | FLUX dev NC; es una copia de un modelo de Civitai (la autoría original no está clara) |

## Recomendación
1. **Primera opción: no depender de un LoRA.** Generar con SDXL base (Open RAIL++-M, uso comercial claro) o usar stock real, y pasarlo por **`pixelizar.py`** (TAREA 6). La paleta fija y el Bayer dan un pixel art **estable entre fotogramas**, que es justo lo que un LoRA no garantiza en animación (cada fotograma "inventa" píxeles distintos y parpadea). Además no hay ninguna licencia de terceros que vigilar.
2. **Si se quiere un LoRA para fotogramas fijos o miniaturas:** **#2 pixel-art-sdxl-dora** (licencia openrail++ visible en la ficha) o **#1 PixelArtRedmond SDXL**, después de confirmar en su página la licencia y la casilla "Sell images they generate", con captura y fecha.
3. **Flux:** solo si Jose acepta la zona gris de usar FLUX dev en un canal monetizado, o compra la licencia comercial de BFL. En ese caso, **#5 Pixel Art Illustrations FLUX** encaja mejor con paisajes de documental que los LoRA de *assets* de juego.
4. **En todos los casos:** pasar la salida del LoRA por `pixelizar.py` con la paleta del canal, para que todo el vídeo comparta la misma paleta y rejilla.

## Fuentes consultadas (25/10/2026)
- Licencia FLUX [dev] v2.0: https://bfl.ai/legal/non-commercial-license-terms
- Ficha FLUX.1-dev: https://huggingface.co/black-forest-labs/FLUX.1-dev
- Artículo de Civitai "Can I Use FLUX for Commercial Use?": https://civitai.com/articles/6625/can-i-use-flux-for-commercial-use
- Guía de licencias FLUX (terceros): https://artificialguy.com/blog/flux-licensing-commercial-use/
- Open RAIL++-M (copia): https://open.windriver.com/info/uni-license-list/licenses/bigscience-open-rail-m2.html
- Espejos y fichas: https://civarchive.com/models/120096 · https://comfy.icu/models/683579/Pixel-Art-Illustrations-FLUX · https://www.promptlayer.com/models/pixel-art-xl
