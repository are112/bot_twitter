# Bot de Twitter con Python y Tweepy

Este es un bot de Twitter desarrollado en Python que publica automáticamente tweets desde un archivo de texto en intervalos de 24 horas.

## Características
- Publica tweets desde un archivo `tweets.txt`.
- Usa la API de Twitter a través de la librería Tweepy.
- Maneja errores en la publicación de tweets.
- Se ejecuta en un bucle infinito, reiniciando el ciclo al llegar al final de la lista de tweets.

## Requisitos
Antes de ejecutar el bot, asegúrate de tener:

- Python 3 instalado.
- Una cuenta de desarrollador en Twitter.
- Credenciales de API de Twitter (API Key, API Secret Key, Access Token, Access Token Secret).
- Librerías necesarias instaladas.

## Instalación

1. Clona este repositorio:
   ```sh
   git clone https://github.com/are112/bot_twitter
   cd bot_twitter
   ```

2. Instala las dependencias necesarias:
   ```sh
   pip install tweepy
   ```

3. Configura tus credenciales de la API de Twitter en el código:
   ```python
   API_KEY = 'TU_API_KEY'
   API_SECRET_KEY = 'TU_API_SECRET_KEY'
   ACCESS_TOKEN = 'TU_ACCESS_TOKEN'
   ACCESS_TOKEN_SECRET = 'TU_ACCESS_TOKEN_SECRET'
   ```

4. Crea un archivo `tweets.txt` con los tweets que deseas publicar (un tweet por línea).

5. Ejecuta el bot:
   ```sh
   python bot_twitter.py
   ```

## Uso
El bot leerá los tweets desde `tweets.txt` y los publicará en orden, esperando 24 horas entre cada publicación. Si llega al final del archivo, reiniciará el ciclo y comenzará desde el principio.

## Notas
- Si deseas cambiar el intervalo de tiempo, modifica la línea:
  ```python
  time.sleep(86400)  # Espera 24 horas
  ```
  Por ejemplo, para publicar cada hora, usa `3600` segundos.

- Asegúrate de que `tweets.txt` contenga contenido válido, sin líneas en blanco innecesarias.

## Contribuciones
Las contribuciones son bienvenidas. Puedes abrir un issue o enviar un pull request.

## Licencia
Este proyecto está bajo la licencia MIT.

