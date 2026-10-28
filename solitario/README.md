# Solitario de Canicas

El solitario de canicas (senku) de toda la vida, para jugar en el navegador del móvil.

**Juega aquí:** https://jrubioadies.github.io/solitario/

## Cómo se juega

- Toca una canica y luego un hueco libre a dos casillas: salta por encima de la de en medio, que se retira.
- Solo en línea recta (en el tablero triangular también en diagonal).
- La partida acaba cuando no quedan saltos. El reto: dejar una sola canica, y en el clásico, que quede en el centro.

## Qué tiene

- Dos tableros: Clásico (cruz de 33 huecos) y Triángulo (15 huecos).
- Pista que calcula en el momento un camino hasta dejar una sola canica y avisa si desde la posición actual ya no es posible.
- Deshacer, récord por tablero y partida guardada automáticamente.

## Tecnología

Un único `index.html` en JavaScript puro, sin librerías. La pista usa una búsqueda en profundidad con memoria de posiciones sin salida.

`index.html?reel` abre el modo de grabación vertical (1080×1920) que juega una solución real del tablero clásico; `render_reel.py` lo graba con Playwright y ffmpeg monta el vídeo de Instagram.

---

Más juegos: [Othello](https://jrubioadies.github.io/othello/) · [Torre Tambaleante](https://jrubioadies.github.io/torre-tambaleante/) · [Sudoku](https://jrubioadies.github.io/sudoku/)

Hecho por **Javier Rubio** · [Adilco Tech Center, SL](https://adilcotech.com) · [jrubioadies.github.io](https://jrubioadies.github.io)
