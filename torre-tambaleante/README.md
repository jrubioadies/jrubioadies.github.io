# Torre Tambaleante

Juego de torre de bloques en 3D que se juega en el navegador, en móvil u ordenador. Saca un bloque, ponlo arriba y que no se caiga.

**Juega aquí:** https://jrubioadies.github.io/torre-tambaleante/

## Cómo se juega

- Arrastra para girar la torre en 3D y pellizca (o usa la rueda) para acercar.
- Toca un bloque para elegirlo: verás el riesgo de derrumbe de esa jugada.
- Pulsa **Sacar** (o toca el bloque otra vez): sale de la torre y se coloca solo arriba.
- El último piso completo y el que se está construyendo no se pueden tocar.
- Si un piso se queda solo con un bloque lateral, la torre cae. Cada hueco y cada piso extra suben el riesgo.
- Quien derriba la torre, pierde. Modos: contra la CPU o dos jugadores en el mismo dispositivo.

## Tecnología

Un único `index.html` con [Three.js](https://threejs.org/) 0.149 cargado desde jsDelivr. Texturas de madera generadas en canvas, sombras en tiempo real y una física sencilla para el derrumbe. Sin build ni dependencias.

`index.html?reel` abre el modo de grabación vertical (1080×1920) que se usó para generar el vídeo de Instagram con `render_reel.py` (Playwright + ffmpeg).

---

Hecho por **Javier Rubio** · [Adilco Tech Center, SL](https://adilcotech.com) · [jrubioadies.github.io](https://jrubioadies.github.io)
