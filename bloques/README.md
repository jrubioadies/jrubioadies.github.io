# Bloques de bolsillo

El clásico de piezas que caen, para jugar en el navegador y pensado para el móvil.

**Juega aquí:** https://jrubioadies.github.io/bloques/

## Qué tiene

- Pozo de 10×20 con las siete piezas de siempre, reparto por bolsas de siete (nunca faltan las alargadas mucho tiempo) y vista de las tres siguientes.
- Pieza fantasma, pieza guardada, caída suave y caída de golpe.
- Giro estándar con patadas de pared y medio segundo de margen al tocar suelo.
- Puntuación por líneas (de 1 a 4), giros en T, combos, jugadas difíciles seguidas y tablero limpio.
- Un nivel cada 10 líneas, cada vez más rápido. Récord y partida guardados automáticamente; se pausa al cambiar de pestaña.
- Controles táctiles: desliza para mover, toca para girar, desliza rápido abajo para soltar y arriba para guardar. También botones en pantalla y teclado (flechas, Z/X, espacio, C, P).

## Tecnología

Un único `index.html` en JavaScript puro, sin librerías, dibujado en `<canvas>` con un bucle a paso fijo de 120 Hz.

`index.html?reel` abre el modo de grabación vertical (1080×1920) con una partida determinista que juega un piloto automático; `render_reel.py` la graba con Playwright y ffmpeg monta el vídeo de Instagram.

---

Más juegos: https://jrubioadies.github.io/juegos/

Hecho por **Javier Rubio** · [Adilco Tech Center, SL](https://adilcotech.com) · [jrubioadies.github.io](https://jrubioadies.github.io)
