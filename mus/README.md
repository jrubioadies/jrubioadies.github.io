# Mus

El mus por parejas con la baraja española: con un compañero CPU contra dos rivales, u online con tus amigos, cada uno desde su móvil.

**Juega aquí:** https://jrubioadies.github.io/mus/

- A ocho reyes (los treses valen como reyes y los doses como ases), con mus y descartes, y los cuatro lances: grande, chica, pares y juego (o punto si nadie tiene juego).
- Envites, subidas y órdago. Lo no querido se cobra al momento; lo querido y lo pasado se cuenta al final de la mano junto con los pares y el juego, con un recuento lance a lance y las cartas de todos.
- Partidas a 30 o 40 tantos.
- Modo online: el anfitrión crea una sala y pasa el enlace. Cada jugador ve solo sus cartas, la baraja se queda en el móvil del anfitrión y los sitios libres los juega la CPU. Si alguien se desconecta, puede volver a su sitio o pasarlo a la CPU.

## Tecnología

Un único `index.html` en JavaScript puro, pensado para el móvil: tema claro y oscuro, partida guardada en el navegador y naipes dibujados en SVG.

El modo online usa WebRTC con [PeerJS](https://peerjs.com): la conexión va directa entre móviles. El móvil del anfitrión ejecuta el motor de la partida y manda a cada jugador solo sus propias cartas, así nadie puede ver las de los demás ni siquiera mirando el código.

---

Más juegos: https://jrubioadies.github.io/juegos/

Hecho por **Javier Rubio** · [Adilco Tech Center, SL](https://adilcotech.com) · [jrubioadies.github.io](https://jrubioadies.github.io)
