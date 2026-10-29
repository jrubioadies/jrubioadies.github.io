# Cuatro en Raya

El clásico de soltar fichas y juntar cuatro, para jugar en el navegador del móvil.

**Juega aquí:** https://jrubioadies.github.io/cuatro-en-raya/

## Qué tiene

- Contra la CPU con tres niveles (Fácil, Medio y Difícil) o a dos jugadores en el mismo dispositivo.
- Fichas que caen con gravedad y rebote, por detrás de la placa del tablero, y la línea ganadora iluminada.
- Marcador, se turnan para empezar, deshacer y partida guardada automáticamente.

## Tecnología

Un único `index.html` en JavaScript puro, sin librerías. La CPU usa búsqueda minimax (negamax) con poda alfa-beta y una evaluación por ventanas de cuatro casillas; el nivel cambia la profundidad de búsqueda.

`index.html?reel` abre el modo de grabación vertical (1080×1920) con una partida real calculada por el propio motor; `render_reel.py` la graba con Playwright y ffmpeg monta el vídeo de Instagram.

---

Más juegos: [Othello](https://jrubioadies.github.io/othello/) · [Torre Tambaleante](https://jrubioadies.github.io/torre-tambaleante/) · [Sudoku](https://jrubioadies.github.io/sudoku/) · [Solitario](https://jrubioadies.github.io/solitario/) · [2048](https://jrubioadies.github.io/2048/) · [Palabra del día](https://jrubioadies.github.io/palabra/) · [Cuatro en raya](https://jrubioadies.github.io/cuatro-en-raya/)

Hecho por **Javier Rubio** · [Adilco Tech Center, SL](https://adilcotech.com) · [jrubioadies.github.io](https://jrubioadies.github.io)
