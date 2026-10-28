# Sudoku de bolsillo

Sudoku para jugar en el navegador, pensado para el móvil.

**Juega aquí:** https://jrubioadies.github.io/sudoku/

## Qué tiene

- Un sudoku nuevo en cada partida, generado en el momento y siempre con una única solución.
- Cuatro niveles: Fácil, Medio, Difícil y Experto.
- Resaltado de fila, columna, bloque y números iguales; los errores se marcan en rojo.
- Notas (candidatos) que se limpian solas al acertar un número.
- Deshacer, borrar y 3 pistas por partida.
- Cronómetro con pausa, récord por nivel y partida guardada automáticamente.
- Teclado en ordenador: flechas, números, Supr y N para notas.

## Tecnología

Un único `index.html` en JavaScript puro, sin librerías. El generador rellena un tablero con backtracking aleatorio y quita números comprobando con un solucionador (heurística de la casilla con menos candidatos) que la solución sigue siendo única.

`index.html?reel` abre el modo de grabación vertical (1080×1920) con una partida guionizada; `render_reel.py` lo graba con Playwright y ffmpeg monta el vídeo de Instagram.

---

Más juegos: [Othello](https://jrubioadies.github.io/othello/) · [Torre Tambaleante](https://jrubioadies.github.io/torre-tambaleante/)

Hecho por **Javier Rubio** · [Adilco Tech Center, SL](https://adilcotech.com) · [jrubioadies.github.io](https://jrubioadies.github.io)
