# Ajedrez

Ajedrez completo para el móvil, contra la CPU con tres niveles o a dos.

**Juega aquí:** https://jrubioadies.github.io/ajedrez/

Un único `index.html` en JavaScript puro, sin librerías, pensado para el móvil: tema claro y oscuro, partida guardada en el navegador, lista de jugadas en notación española y control con teclado o con mando (PlayStation, Xbox, MFi).

- Todas las reglas: enroque, captura al paso, coronación a elegir, jaque mate y tablas (ahogado, triple repetición, 50 jugadas y falta de material). El generador de jugadas está validado con las pruebas *perft* estándar.
- CPU con búsqueda alfa-beta, profundización iterativa y búsqueda de capturas; los niveles Fácil, Medio y Difícil cambian la profundidad, el tiempo y el margen de error.
- Piezas dibujadas en SVG propio.

`index.html?reel` abre el modo de grabación vertical (1080×1920) con la *Partida de la Ópera* (Morphy, París 1858); `render_reel.py` la graba con Playwright y ffmpeg monta `ajedrez_reel.mp4`.

---

Más juegos: https://jrubioadies.github.io/juegos/

Hecho por **Javier Rubio** · [Adilco Tech Center, SL](https://adilcotech.com) · [jrubioadies.github.io](https://jrubioadies.github.io)
