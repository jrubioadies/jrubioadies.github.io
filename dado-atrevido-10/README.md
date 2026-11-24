# Dado Atrevido 10

Juego para adultos (+18) en el navegador del móvil, **por parejas** (de 1 a 3 parejas) o **cada uno a su aire** (de 2 a 6 jugadores). Se tira por turnos un dado de diez caras en 3D:

| Cara | Qué pasa |
|---|---|
| Verdad | Contesta con sinceridad |
| Reto | Haz lo que dice la carta |
| Caricia | Una caricia al azar: qué, dónde y cuántos segundos (sube de tono con el nivel) |
| Desnúdame | Le quitas una prenda a tu pareja, la que tú elijas |
| Prenda | Fuera una prenda, la que tú elijas |
| Duelo | Un desafío al azar (miradas, cosquillas, cara o cruz, besos…); quien pierde paga lo que os jugáis, también al azar: una prenda, un reto, una caricia, una verdad… |
| Tú mandas | Eliges a quién y le pones verdad o reto |
| Comodín | Te lo guardas: te libra de una carta sin beber |
| Brindis | Bebe todo el mundo |
| Todos | Una acción que hacéis todos a la vez (besar a tu pareja, enseñar una parte del cuerpo, quitaros una prenda…) |

En Ajustes → «Vuestras cartas» podéis escribir retos y verdades propios (con el nombre de la pareja, el nivel desde el que salen y la opción de que solo salgan por parejas). Se guardan solo en el dispositivo y salen más a menudo que las del juego.

Las cartas con tiempo («durante 20 segundos», «un minuto»…) traen un contador: se toca para empezar, se puede pausar y pita en los tres últimos segundos y al terminar.

El dado suena al rodar (traqueteo, tres botes y una campanita); se puede silenciar con el botón del altavoz.

Cada jugador indica si es chico o chica (para que los textos concuerden) y, si jugáis cada uno, qué le gusta: las cartas se dirigen a alguien compatible de la mesa.

Con varias parejas se elige el juego entre parejas: solo con tu pareja, duelos cruzados (los duelos son contra alguien de otra pareja) o todo cruzado (también la mitad de retos, caricias, verdades y Desnúdame).

Quien no quiere cumplir, bebe y pasa el turno. Si una carta no os convence, se puede cambiar una vez con «Otra carta». El dado no repite la misma cara dos veces seguidas ni a un jugador la que le salió la vez anterior, y las cartas no se repiten hasta agotar el mazo. Por parejas, las verdades y los retos van siempre dirigidos a tu pareja. Tres niveles (suave, picante y muy picante), prendas iniciales distintas para cada persona (de 0 a 10; en Ajustes se pueden corregir en mitad de la partida) y castigo a elegir (trago, chupito o sin alcohol).

Está en cinco idiomas: español, inglés, portugués, francés e italiano. Se elige con el selector de la esquina del dado (o en la pantalla de inicio y en Ajustes) y por defecto coge el del dispositivo; también se puede forzar con `?lang=fr`. Las traducciones están en `i18n/*.json`; tras tocarlas hay que ejecutar `python3 build-i18n.py`, que comprueba que no falte ninguna clave y genera `i18n.js`.

**Juega aquí:** https://jrubioadies.github.io/dado-atrevido-10/

`index.html` más `i18n.js` (los textos); el dado es un trapezoedro pentagonal dibujado con [three.js](https://threejs.org).

La versión de seis caras para dos sigue en https://jrubioadies.github.io/dado-atrevido/
