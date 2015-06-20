# Fractalis-AR

Este es un experimento de [Realidad Aumentada](https://es.wikipedia.org/wiki/Realidad_aumentada) en el que se mezcla tecnología y arte. Tanto en lo concreto como en lo abstracto.

En lo concreto: existe hardware, software, imágenes y el diseño de una instalación artística. En lo abstracto, la ciencia y la tecnología se acercan al arte, de la mano de los fractales y el glitch, ínstándonos a cuestionar ¿qué es lo real? ¿cómo luce el infinito?

El proyecto nace para el trabajo final de la carrera de Bellas Artes, de [Rocío Rojas Leighton](https://www.flickr.com/photos/dewcolors/).

## Realidad
A modo general, uno de los objetivos principales del proyecto es el de montar una instalación (puede ser una habitación, pasillo, salón, etc) en la que se captan datos de vídeo y de distintos sensores. Estos se combinan y muestran, continuamente, en tiempo real, con secuencias de imágenes pre-generadas.

Los datos de los sensores son usados para controlar el proceso de mezcla de las imágenes: tanto para seleccionar con qué imagen será _aumentado_ cada frame de video, como para definir cómo serán combinadas las dos imágenes.

El resultado, una secuencia de imágenes (video) con _realidad aumentada_, puede guardarse en un archivo, proyectarse, verse en un monitor o distribuirse por la web mediante streaming de video en tiempo real.

Todo este proceso es dirigido por un programa escrito específicamente para este proyecto (que puede obtenerse [aquí](https://github.com/cmdelatorre/fractalisar)).


### Posibilidades

Más allá de la implementación existente, el proyecto permite una infinidad de posibilidades. Tanto el hardware como el software pueden adaptarse fácilmente para obtener resultados muy distintos.

Las imágenes para _aumentar_ la realidad pueden obtenerse a partir de archivos pre-generados, de algún video o incluso generarse automáticamente (aunque esta última opción puede ser complicada por la necesidad de muchos recursos de cómputo).

Con respecto a los sensores, puede utilizarse básicamente cualquiera disponible: de distancia, de iluminación, de movimiento, de presión, micrófonos, botones, otras cámaras, etc. De esta manera pueden diseñarse instalaciones muy complejas, que provean infintas señales o datos al programa.

Todos estos datos parametrizan diversos procesos:
 * **Selección**: la selección de la imagen para mezclar con el frame de video. Pueden haber distintas fuentes de imágenes que se utilicen en distintos momentos o que a veces no se requiera modificar el video original.
 * **Transformación**: las transformaciones y filtros que se aplicarán a esta imagen o al frame de video real. Hay infinidad de cosas que pueden hacerse sobre las imágenes antes de mezclarlas (transformaciones geométricas, de colores, etc.)
 * **Mezcla**: el algoritmo que mezcla ambas imágenes puede hacerlo de muchas formas: superponiendo partes de una imagen a la otra, reemplazando pixels con diversos criterios, siguiendo algún _marcador_ predefinido, etc.

Lo anteriormente descripto son ejemplos de cosas que podrían hacerse con relativamente poco trabajo.


## Aumentada

## Trabajo Final: Escencia fractal: Realidades múltiples
La realidad, en el plano en que la percibimos, pareciera ser la composición de los mecanismos que adoptamos según  cómo y cuánto nuestros sentidos captan, lo que vamos transitando. A través de la historia, tanto la ciencia, el mito, los artistas, filósofos, antroposofías e incontables disciplinas,  contribuyen a las ideas y conceptos de lo que es “real”.
El lenguaje de la informática en su complejidad, funciona bajo la lógica de lo que es real para la máquina ,  su acción o respuesta será determinada por el código desarrollado entre “ciertos” y “falsos” lo que programará su funcionamiento.

En ambas dimensiones, tanto para la humanidad como en el plano virtual, no pareciera ser ni tan sencillo , ni mucho menos “inalterable” éste complejo código en el que se desarrollan nuestra vida cotidiana, el funcionamiento de una computadora, nuestro plano onírico, etc.

La realidad aumentada es el término que se usa para definir una visión a través de un dispositivo tecnológico, directa o indirecta, de un entorno físico del mundo real, cuyos elementos se combinan con elementos virtuales para la creación de una realidad mixta en tiempo real. Consiste en un conjunto de dispositivos que añaden información virtual a la información física ya existente, es decir, añadir una parte sintética virtual a lo real.

Como recurso tecnológico , combina los conceptos de múltiples y simultaneas situaciones,   disolviendo paralelismos, fractalizando la información, de lo virtual, a lo natural, de lo natural, a lo abstracto.

En el ámbito de la informática o los videojuegos un error que, al no afectar negativamente al rendimiento, jugabilidad o estabilidad del programa o juego en cuestión, no puede considerarse un bug, sino más bien una "característica no prevista”, éste concepto de error se lo conoce como Glitch.
Un glitch o algo “no previsto”  es algo inherente a nuestra realidad también, en diferentes manifestaciones, sin  brindar respuestas a esto, el glitch será la escencia por la que
se infiltran y conviven dimensiones en éste espacio.

Las imágenes que se alteran bajo la influencia de los movimientos de quien transite el espacio de obra, son fractales trabajados digitalmente bajo las ecuaciones matemáticas de mandelbrot, las que grafican virtualmente  patrones de la naturaleza, como entes que visitan el plano, infiltrados a través de los códigos que les abren camino.

Benoit Mandelbrot quien es el padre de la denominada Geometría Fractal, una nueva rama de la geometría que podemos decir que estudia los objetos tal como son. Mandelbrot pensó que las cosas en la realidad no son tan perfectas como las muestra la geometría euclídea: las esferas no son realmente esferas, las líneas no son perfectamente rectas, las superficies no son uniformes… Ello le llevó a estudiar estas “imperfecciones” pero hasta que no aparecieron los primeros ordenadores digitales no se pudo visualizar este fractal Z = Z2 + C con toda su complejidad.

### Instalación: prototipo funcional
La instalación fue montada para el trabajo final de [Rocío Rojas Leighton](https://www.flickr.com/photos/dewcolors/) en la [Escuela Superior de Bellas Artes "Dr. José Figueroa Alcorta"](http://figueroalcorta.blogspot.com.ar/).

Se utilizó una [cámara web](http://www.logitech.com/es-roam/product/hd-pro-webcam-c920?crid=34) y una placa [Arduino Uno](https://www.arduino.cc/en/Main/arduinoBoardUno) (con un [sensor ultrasónico de distancia](https://www.parallax.com/product/28015?SortField=ProductName,ProductName)), conectadas ambas via USB a una computadora con [Ubuntu 14.04](http://www.ubuntu.com/download) corriendo el [programa en Python](https://github.com/cmdelatorre/fractalisar).

Los fractales para mezclar con el video fueron generados con [Mandelbulb](http://mandelbulb.com/) y pueden [descargarse de aquí](https://mega.nz/#F!aAME2TgC!-yJrr7o-PNV7ljeSyIYoNg).

### Arduino, Python y OpenCV

La placa [Arduino](http://www.arduino.cc/) es perfecta para este proyecto porque es muy fácil de utilizar y provee la capacidad de conectar sensores muy variados. Además puede comunicarse fácilmente con la computadora mediante un puerto USB o por la red (Ethernet o WiFi).

El programa que conecta todas las partes fue escrito en el lenguaje de programación [Python 2.7](https://www.python.org/). Entre otras ventajas de esta desición, está el hecho de que se puede usar la librería [OpenCV](http://opencv.org/) que facilita enormemente el proceso de trabajar con video e imágenes.


# Autores

La idea original y el desarrollo artístico es obra de Rocío Rojas Leighton con la colaboración de Juan de la Torre. Otros de sus proyectos conjuntos son:
 * [Djalus](http://www.djalus.com/)
 * [Hû](https://www.facebook.com/hu.silvestre?pnref=story)
 * [lÖnG LïnG](https://www.flickr.com/photos/longundling/)

El software fue escrito por @cmdelatorre.