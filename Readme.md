
```markdown
# Métodos Numéricos en Python

¡Bienvenido a mi proyecto de métodos numéricos! Soy Gregorio Cardona, estudiante de la Universidad de Pamplona en el 7mo semestre, y este trabajo fue realizado bajo la supervisión del ingeniero Jesús Durán. Aquí encontrarás implementaciones de varios métodos numéricos fundamentales: el método de la secante, la falsa posición, la bisección y Newton-Raphson.

## Descripción de los Métodos

### 1. Método de la Secante
El método de la secante es una técnica iterativa utilizada para encontrar raíces de funciones. A diferencia de otros métodos, utiliza una secante para aproximar la raíz, lo cual puede converger más rápido en algunos casos.

### 2. Método de la Falsa Posición (Regula Falsi)
Este método es similar al de la bisección, pero en lugar de tomar el punto medio del intervalo, se utiliza la recta que une los puntos finales del intervalo para encontrar una mejor aproximación de la raíz. Es una combinación entre la precisión de la bisección y la rapidez del método de la secante.

### 3. Método de Bisección
La bisección es un método sencillo y robusto para encontrar raíces de funciones continuas. Funciona dividiendo el intervalo en dos y seleccionando el subintervalo donde cambia el signo de la función, garantizando así la convergencia hacia la raíz.

### 4. Método de Newton-Raphson
Este es un método poderoso y eficiente que utiliza la derivada de la función para encontrar sucesivas aproximaciones a la raíz. Requiere una buena estimación inicial y la función debe ser derivable.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
algoritmos-numericos/
│
├── secante.py          # Implementación del método de la secante
├── falsa_posicion.py   # Implementación del método de la falsa posición
├── biseccion.py        # Implementación del método de la bisección
├── newton_raphson.py   # Implementación del método de Newton-Raphson
├── ejemplos/           # Ejemplos de uso de cada método
└── README.md           # Este archivo
```

## Ejecución

Para ejecutar cada uno de los métodos, puedes usar los siguientes comandos en la línea de comandos:

```bash
python secante.py
python falsa_posicion.py
python biseccion.py
python newton_raphson.py
```

Cada script incluye ejemplos de uso y cómo ingresar la función y los parámetros necesarios.

## Requisitos

Este proyecto está escrito en Python 3. Para ejecutarlo, necesitas tener instalado Python 3 en tu sistema. Puedes instalarlo desde [python.org](https://www.python.org/).

## Contacto

Para cualquier pregunta o sugerencia, puedes contactarme a través de mi correo estudiantil haciendo clic en el ícono a continuación:

[![Email](https://img.icons8.com/fluency/48/000000/email.png)](mailto:jose.cardona@unipamplona.edu.co)

¡Gracias por tu interés en mi proyecto y espero que encuentres útiles estas implementaciones!

---

**Gregorio Cardona**
Estudiante de Ingeniería
Universidad de Pamplona
```
