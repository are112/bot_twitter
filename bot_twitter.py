import tweepy
import time
import random
import logging
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Constantes
ARCHIVO_ESTADO = Path('estado.txt')  # Archivo para guardar el último índice publicado
ARCHIVO_LOG = Path('registro.log')   # Archivo para guardar los logs
ARCHIVO_TWEETS = Path('tweets.txt')  # Archivo con los tweets
ARCHIVO_HASHTAGS = Path('hashtag.txt')  # Archivo con los hashtags

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(ARCHIVO_LOG),  # Escribe logs en un archivo
        logging.StreamHandler()  # Muestra logs en la consola
    ]
)

# Cargar credenciales de Twitter desde variables de entorno
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Autenticación con la API de Twitter
def autenticar_twitter():
    try:
        client = tweepy.Client(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET_KEY,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )
        logging.info("Autenticación con Twitter exitosa.")
        return client
    except Exception as e:
        logging.error(f"Error al autenticar con Twitter: {e}")
        raise

# Función genérica para leer archivos
def leer_archivo(archivo):
    if not archivo.exists():
        logging.error(f"El archivo {archivo} no existe.")
        raise FileNotFoundError(f"El archivo {archivo} no existe.")

    with open(archivo, 'r', encoding='utf-8') as file:
        lineas = file.readlines()

    if not lineas:
        logging.error(f"El archivo {archivo} está vacío.")
        raise ValueError(f"El archivo {archivo} está vacío.")

    return [linea.strip() for linea in lineas]

# Función para seleccionar 5 hashtags al azar
def seleccionar_hashtags(hashtags):
    return random.sample(hashtags, min(5, len(hashtags)))

# Función para publicar un tweet con hashtags
def publicar_tweet(client, tweet, hashtags, max_reintentos=3):
    tweet_con_hashtags = f"{tweet} {' '.join(hashtags)}"
    for intento in range(max_reintentos):
        try:
            response = client.create_tweet(text=tweet_con_hashtags)
            logging.info(f"Tweet publicado con éxito: {tweet_con_hashtags}")
            logging.info(f"ID del tweet: {response.data['id']}")
            return True
        except tweepy.errors.Forbidden as e:
            logging.error(f"Error al publicar el tweet (intento {intento + 1}): {e}")
        except Exception as e:
            logging.error(f"Ocurrió un error inesperado (intento {intento + 1}): {e}")
        time.sleep(5)  # Espera 5 segundos antes de reintentar
    return False

# Función para guardar el estado (último índice publicado)
def guardar_estado(indice):
    try:
        with open(ARCHIVO_ESTADO, 'w', encoding='utf-8') as file:
            file.write(str(indice))
        logging.info(f"Estado guardado: Índice {indice}")
    except Exception as e:
        logging.error(f"Error al guardar el estado: {e}")

# Función para cargar el estado (último índice publicado)
def cargar_estado():
    try:
        if not ARCHIVO_ESTADO.exists():
            logging.warning("No se encontró un archivo de estado. Comenzando desde el principio.")
            return 0

        with open(ARCHIVO_ESTADO, 'r', encoding='utf-8') as file:
            estado = file.read().strip()
            if estado.isdigit():
                return int(estado)
            else:
                logging.warning("El archivo de estado está corrupto. Comenzando desde el principio.")
                return 0
    except Exception as e:
        logging.error(f"Error al cargar el estado: {e}")
        return 0

# Función principal
def main():
    try:
        client = autenticar_twitter()
        tweets = leer_archivo(ARCHIVO_TWEETS)
        hashtags = leer_archivo(ARCHIVO_HASHTAGS)

        # Cargar el último índice publicado
        indice = cargar_estado()

        while True:
            if indice >= len(tweets):
                logging.info("No hay más tweets por publicar. Reiniciando el ciclo...")
                indice = 0  # Reiniciar el índice

            tweet = tweets[indice]
            hashtags_seleccionados = seleccionar_hashtags(hashtags)

            # Publicar el tweet y guardar el estado solo si se publica correctamente
            if publicar_tweet(client, tweet, hashtags_seleccionados):
                guardar_estado(indice + 1)  # Guardar el índice del próximo tweet
                indice += 1  # Incrementar el índice

            # Espera entre 1 y 3 horas para evitar patrones predecibles
            tiempo_espera = random.randint(3600, 10800)
            logging.info(f"Esperando {tiempo_espera // 3600} horas antes del próximo tweet...")
            time.sleep(tiempo_espera)

    except Exception as e:
        logging.error(f"Error en la ejecución del programa: {e}")

if __name__ == "__main__":
    main()