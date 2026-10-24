# hangman_1_0
Danna camila aristizabal calvo 
danna.aristizabal@utp.edu.co

# Juego del Ahorcado Hangman en Python

Proyecto desarrollado para la práctica de programación en Python.

# Sobre el Juego
Implementación del clásico Juego del Ahorcado en Python.
Objetivo: Adivinar la palabra secreta oculta bajo guiones bajos antes de que se agoten tus vidas.
Dinámica:El sistema elige al azar una palabra de un banco de 20 términos tecnológicos.
Tienes 6 vidas. Cada error dibuja una parte del monigote en formato ASCII.
Ingresa una letra a la vez por la terminal para descubrir el reto
##  Reglas del Juego
1. El programa seleccionara una palabra secreta al azar de un banco de 20 palabras en mayúsculas.
2. Se mostrará en pantalla la palabra oculta en forma de guiones bajos .
3. Tienes un total de 6 vidas que estan representadas gráficamente con etapas de un monigote en ASCII.
4. En cada turno debes ingresar una sola letra alfabética.
5. Si la letra está en la palabra, se revelará en su posición correspondiente. Si no está perderás una vida y se dibujará una parte del monigote.
6. Ganas si descubres todas las letras antes de quedarte sin vidas. Pierdes si se agotan tus 6 vidas.

## Como Ejecutar el Juego
Asegúrate de tener Python instalado y debe estar dentro de la carpeta hangman_1_0:


# Planificación y Configuración Inicial

[x] 1. Definir los requerimientos del proyecto del juego del ahorcado.

[x] 2. Planificar la estructura del programa dividida en tres archivos principales.

[x] 3. Crear el repositorio publico en GitHub,

[x] 4. Redactar la estructura base y la informacion de mi en el archivo README.md.

[x] 5. Configurar el entorno de desarrollo local en Python.

Fase 2: Desarrollo de Modulos Secundarios
[x] 6. Crear el archivo palabras.py para almacenar el banco de palabras.

[x] 7. Escribir la lista de palabras en formato de cadena y en mayusculas ([A-Z]).

[x] 8. Crear el archivo monigote.py para almacenar la representacion gráfica.

[x] 9. Diseñar las etapas del monigote en texto ASCII desde 0 hasta 6 errores.

[x] 10. Validar que las importaciones entre archivos funcionen correctamente.

Fase 3: Logica y Validaciones en hangman.py
[x] 11. Importar los módulos de palabras, monigote y la librería random.

[x] 12. Implementar la selección aleatoria de la palabra secreta con random.choice.

[x] 13. Inicializar la lista para mostrar los guiones bajos según la longitud de la palabra.

[x] 14. Configurar las variables iniciales de control vidas y letras usadas.

[x] 15. Diseñar el ciclo principal del juego while basado en las vidas restantes.

[x] 16. Implementar la solicitud de entrada por consola input al usuario.

[x] 17 hacer la validación de longitud de un carácter (len()) y si es una letra (isalpha()).

[x] 18. Agregar la transformacion a  la letra ingresada a mayúscula (upper()).

[x] 19. Implementar el control de letras repetidas comparando con el historial de la lista.

[x] 20. Desarrollar el sistema de actualización de la palabra mostrada y el descuento de vidas por errores.

Fase 4: Pruebas Finales y Entrega
[x] 21. Vincular los dibujos del monigote según el número de fallos acumulados.

[x] 22. Programar las condiciones de salida para victoria y derrota.

[x] 23. Realizar pruebas  en la consola para corregir errores de sintaxis y lógica.

[x] 24. Actualizar el archivo README.md con las instrucciones finales de ejecución.

[x] 25. Subir y confirmar todos los cambios en el repositorio pblico de GitHub antes de la hora de entrega.