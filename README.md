# Índice
<ul>
<li>Introducción</li>
<li>Manual</li>
<li>Descripción Técnica</li>
<li>Hiatorias de Usuario</li>
<li>Diagrama de Componentes</li>
<li>Implementación</li>
<li>Pruebas</li>
<li>Estudio de Tiempo Invertido</li>
<li>Uso de IA</li>
<li>Conclusión</li>
</ul>


# Introducción
Juan Mateo Álvarez Álvarez - <a href="https://github.com/Juan071825">@Juan071825</a>

<p>El fin de este proyecto es crear en el lenguaje de programación <a href="https://www.python.org/">python</a>, un programa capaz de obtener la puntuación total de una tarjeta de bolos. Para el desarrollo de este proyecto he utilizado, además de python, el control de versiones <a href="https://git-scm.com/">git</a>, el lenguaje <a href="https://www.markdownguide.org/">markdown</a> y el gestor de proyectos <a href="https://docs.astral.sh/uv/">uv</a></p>

<p>Este proyecto fue hecho a modo de aprendizaje en el módulo de programación de 1ºDAM para aprender a utilizar clases en python.</p>

# Manual

## Instalación en Linux

<p>Si deseas ejecutar este proyecto en local debes seguir estos pasos: </p>
<ol>
<li>Debes tener instalado Python en tu equipo, la versión 3.12., para saber si lo tienes instalado o no, ejecuta python --version</li>

<li> Instala uv con curl -LsSf https://astral.sh/uv/install.sh | sh, verifica que ha funcionado con uv --version</li>

<li>Clona el proyecto pulsando en la página principal del repositorio "<> Code" y dentro pulsa el símbolo de los 2 cuadrados que aparece a la derecha del enlace del repositorio. Ya tendrás copiada la URL del proyecto, la cual tendrás que pegar en la terminal después del comando git clone tal que así:
git clone &lt;URL&gt;.</li>

<li>Crea el entorno del proyecto con uv venv y activalo con source .venv/bin/activate</li>

<li>Ejecuta en terminal uv sync para instalar las dependencias necesarias del proyecto.</li> 
</ol>

## Uso
<p>Por último para ejecutar el proyecto utiliza uv run python &lt;nombre módulo&gt;, que puede ser score_counter.py para la versión que no utiliza <a href="https://es.wikipedia.org/wiki/Programaci%C3%B3n_orientada_a_objetos">POO</a> o scoreCard para la que si la utiliza.</p>


# Metodología
Utilicé la <a href="https://es.wikipedia.org/wiki/Desarrollo_guiado_por_pruebas">TDD</a> como metodología, cogí los casos test de este <a href="https://github.com/dfleta/bowling-game-kata-automata"> repositorio</a>. Primero me centré en pasar los casos test más sencillos y que no tenían ningún caso especial  que se pudiera dar en una partida de bolos, una vez pasados estos casos báscicos fui a cubrir las situaciones excepcionales una a una.


## Historias de usuario
La lógica del programa consta de 2 funciones: 

<ul>
<li>frame_dict_creator: recibe todos los rolls en un strings sin que estos estén divididos por frames y su papel es meter estas rolls en un diccionario donde cada llave representa un frame y su valor asociado es una tupla que contiene los resultados de las rolls de ese frame.</li>
<li>score_counter: recibe el diccionario creado por frame_dict_creator y es quien se encarga de calcular la puntuación total de la tarjeta.</li>
</ul>

## Diagrama de componentes

El diagrama es simple, los módulos score_counter.py y scoreConter.py, recordemos que son lo mismo pero con distinto paradigma, dependen del módulo constants.py para funcionar.

## Reglas de puntuación de los bolos

<ul>
    <li>
        Cada partida ("line") de bolos incluye 10 turnos ("frames").
    </li>
    <li>
        Por cada "frame" el jugador ("bowler") tiene dos intentos (bowlings o rolls) para tirar todos los bolos.
    </li>
    <li>
        Si en los 2 intentos no tira todos los bolos se suma a su puntuación el número de bolos ("pins") tirado.
    </li>
    <li>
        Si en 2 tiradas tira todos los bolos, hace un "spare" y su puntuación es 10 más el número de "pins" tirados en el siguiente lanzamiento.
    </li>
    <li>
        Si con un solo lanzamiento tira todos los bolos es un "strike" y el jugador no dispondrá del segundo lanzamiento de la ronda pero a los 10 puntos por tirar todos los "pins" se le sumará la puntuación de las 2 siguientes tiradas.
    </li>
    <li>
        Si en el décimo frame el jugador hace un "spare" recibirá una tirada extra, si hace un "strike" recibirá 2. Esto se hace para poder calcular la puntuación de este turno.
    </li>
    <li>
        LA puntuación ("score") final es la suma de la puntuación obtenida en todos los turnos.
    </li>
</ul>

