# Palabra del Día

Adivina la palabra oculta de 5 letras en 6 intentos, en español.

**Juega aquí:** https://jrubioadies.github.io/palabra/

## Modos

- **Del día**: la misma palabra para todos, cambia a medianoche.
- **Finanzas**: vocabulario de contabilidad y empresa (saldo, abono, cuota, haber…), también una al día.
- **Libre**: palabras al azar sin límite.

## Qué tiene

- Teclado en pantalla con Ñ y soporte de teclado físico; las tildes no cuentan.
- Comprobación de que cada intento es una palabra real (diccionario de unas 10.800 palabras de 5 letras).
- Estadísticas por modo: partidas, porcentaje de aciertos, racha, mejor racha y distribución de intentos.
- Botón para copiar el resultado en cuadraditos de colores y compartirlo sin desvelar la palabra.

## Tecnología

Un único `index.html` en JavaScript puro, sin librerías. El diccionario se ha generado a partir del paquete npm `an-array-of-spanish-words` (licencia MIT), filtrando las palabras de 5 letras y quitando tildes.

`index.html?reel` abre el modo de grabación vertical (1080×1920); `render_reel.py` lo graba con Playwright y ffmpeg monta el vídeo de Instagram.

---

Más juegos: [Othello](https://jrubioadies.github.io/othello/) · [Torre Tambaleante](https://jrubioadies.github.io/torre-tambaleante/) · [Sudoku](https://jrubioadies.github.io/sudoku/) · [Solitario](https://jrubioadies.github.io/solitario/) · [2048](https://jrubioadies.github.io/2048/) · [Palabra del día](https://jrubioadies.github.io/palabra/) · [Cuatro en raya](https://jrubioadies.github.io/cuatro-en-raya/)

Hecho por **Javier Rubio** · [Adilco Tech Center, SL](https://adilcotech.com) · [jrubioadies.github.io](https://jrubioadies.github.io)
