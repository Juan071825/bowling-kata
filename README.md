# Índice
<ul>
<li>Introducción</li>
<li>Manual</li>
<li>Descripción Técnica</li>
<li>Diseño</li>
<li>Implementación</li>
<li>Pruebas</li>
<li>Estudio de tiempo invertido</li>
<li>Uso de IA</li>
<li>Conclusión</li>
</ul>


# Introducción
Juan Mateo Álvarez Álvarez - <a href="https://github.com/Juan071825">@Juan071825</a>

<p>El fin de este proyecto es crear en el lenguaje de programación <a href="https://www.python.org/">python</a>, un programa capaz de obtener la puntuación total de una tarjeta de bolos. Para el desarrollo de este proyecto he utilizado, además de python, herramientas y otros lenguajes como <a href="https://git-scm.com/">git</a>, <a href="https://www.markdownguide.org/">markdown</a> y <a href="https://docs.astral.sh/uv/">uv</a></p>

<p>Este proyecto fue hecho a modo de aprendizaje en el módulo de programación de 1ºDAM para saber utilizar clases en python.</p>

# Manual

## Instalación

<p>Si deseas ejecutar este proyecto en local debes seguir estos pasos: </p>
<ol>
<li>Debes tener instalado Python en tu equipo, la versión 3.12., para asegurarse si lo tienes instalado o no ejecuta</li> 
```python
def 
```
<li>Descarga el proyecto del repositorio actual.</li>




## Reglas de puntuación de los bolos

<ul>
    <li>
        Cada partida ("line") de bolos incluye 10 turnos ("frames").
    </li>
    <li>
        Por cada "frame" el jugador ("bowler") tiene dos intentos para tirar todos los bolos.
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

