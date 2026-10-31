# Dominó

El dominó por parejas de toda la vida: con un compañero CPU contra dos rivales, u online con tus amigos, cada uno desde su móvil.

**Juega aquí:** https://jrubioadies.github.io/domino/

- Partidas por parejas a 50, 100 o 200 tantos, con las reglas de bar: sale el seis doble, se juega hacia la derecha y la pareja que domina se apunta los puntos que les quedan a los rivales. Si se cierra, gana la pareja con menos puntos.
- Modo online: el anfitrión crea una sala y pasa el enlace. Cada jugador ve solo sus fichas; los sitios libres los juega la CPU. Si alguien se desconecta, puede volver a su sitio o pasarlo a la CPU.
- CPU que tiene en cuenta los pases de los demás (qué números les faltan) para cerrar a los rivales y no cerrar al compañero.

## Tecnología

Un único `index.html` en JavaScript puro, pensado para el móvil: tema claro y oscuro y partida guardada en el navegador.

El modo online usa WebRTC con [PeerJS](https://peerjs.com): la conexión va directa entre móviles. El móvil del anfitrión ejecuta el motor de la partida y manda a cada jugador solo sus propias fichas, así nadie puede ver las de los demás ni siquiera mirando el código.

---

Más juegos: https://jrubioadies.github.io/juegos/

Hecho por **Javier Rubio** · [Adilco Tech Center, SL](https://adilcotech.com) · [jrubioadies.github.io](https://jrubioadies.github.io)
