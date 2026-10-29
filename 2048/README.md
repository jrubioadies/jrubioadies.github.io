# 2048 de Bolsillo

El clásico de deslizar y sumar fichas, para jugar en el navegador del móvil.

**Juega aquí:** https://jrubioadies.github.io/2048/

## Qué tiene

- Deslizamiento con el dedo o con flechas / W A S D, con animaciones de movimiento, aparición y fusión.
- Puntos y récord, 3 deshacer por partida y partida guardada automáticamente.
- Al llegar al 2048 puedes seguir jugando.

## Tecnología

Un único `index.html` en JavaScript puro, sin librerías.

`index.html?reel` abre el modo de grabación vertical (1080×1920). Reproduce una partida real que llega a 2048 en 963 jugadas, jugada por un jugador automático (expectimax) con una semilla fija; `render_reel.py` la graba con Playwright y ffmpeg monta el vídeo de Instagram.

---

Más juegos: [Othello](https://jrubioadies.github.io/othello/) · [Torre Tambaleante](https://jrubioadies.github.io/torre-tambaleante/) · [Sudoku](https://jrubioadies.github.io/sudoku/) · [Solitario](https://jrubioadies.github.io/solitario/) · [2048](https://jrubioadies.github.io/2048/) · [Palabra del día](https://jrubioadies.github.io/palabra/) · [Cuatro en raya](https://jrubioadies.github.io/cuatro-en-raya/)

Hecho por **Javier Rubio** · [Adilco Tech Center, SL](https://adilcotech.com) · [jrubioadies.github.io](https://jrubioadies.github.io)
