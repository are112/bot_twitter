## [0.2] - 11/02/2025

### Added
- **Uso de Variables de Entorno**: Se implementó un archivo `.env` para almacenar las credenciales de la API de Twitter.
- **Sistema de Logging**: Se agregó un sistema de logging para registrar eventos, errores y advertencias en un archivo `registro.log` y en la consola.
- **Manejo de Hashtags**: Se añadió un archivo `hashtag.txt` para almacenar hashtags y una función para seleccionar 5 hashtags al azar.
- **Persistencia del Estado**: Se implementó un archivo `estado.txt` para guardar el último índice de tweet publicado.
- **Tiempo de Espera Aleatorio**: El tiempo de espera entre tweets ahora es aleatorio, entre 1 y 3 horas.
- **Reintentos de Publicación**: Se agregó un sistema de reintentos (hasta 3 veces) en caso de fallos al publicar un tweet.
- **Manejo de Errores Mejorado**: Se agregaron controles de errores y excepciones para mejorar la robustez del programa.
- **Uso de `Path` para Rutas de Archivos**: Se utilizó la clase `Path` de `pathlib` para manejar rutas de archivos de manera más eficiente.

### Changed
- **Refactorización de Funciones**:
  - La función `obtener_siguiente_tweet` fue reemplazada por una función genérica `leer_archivo`.
  - La lógica principal del programa se movió a una función `main`.
- **Autenticación Modularizada**: La autenticación con la API de Twitter se encapsuló en una función separada (`autenticar_twitter`).
- **Eliminación de Variables Globales**: Se eliminó el uso de variables globales para mejorar la claridad y mantenibilidad del código.

### Fixed
- **Validación de Archivos**: Se agregaron validaciones para asegurar que los archivos (`tweets.txt`, `hashtag.txt`, `estado.txt`) existan y no estén vacíos.
- **Manejo de Excepciones**: Se mejoró el manejo de excepciones para errores específicos, como fallos de autenticación o problemas al publicar tweets.

### Removed
- **Variables Globales**: Se eliminaron las variables globales para mejorar la estructura del código.

### Dependencies
- **Nuevas Librerías**:
  - `python-dotenv`: Para cargar variables de entorno desde un archivo `.env`.
  - `logging`: Para el sistema de registro de logs.
  - `random`: Para seleccionar hashtags y generar tiempos de espera aleatorios.

---

## [0.1] - 04/02/2025

### Added
- **Publicación de Tweets**: Implementación inicial para publicar tweets desde un archivo de texto (`tweets.txt`).
- **Autenticación con Twitter**: Uso de la librería `tweepy` para autenticarse con la API de Twitter.
- **Bucle Infinito**: Publicación de tweets en un ciclo infinito con un intervalo fijo de 24 horas.
