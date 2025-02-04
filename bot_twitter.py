import tweepy
import time

# Reemplaza estos valores con tus credenciales de la API de Twitter
API_KEY = '***'
API_SECRET_KEY = '***'
ACCESS_TOKEN = '***'
ACCESS_TOKEN_SECRET = '***'

# Autenticación con la API de Twitter
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Función para leer el archivo de texto y obtener el siguiente tweet
def obtener_siguiente_tweet(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        tweets = file.readlines()
    return tweets

# Función para publicar un tweet
def publicar_tweet(tweet):
    try:
        response = client.create_tweet(text=tweet)
        print(f"Tweet publicado con éxito: {tweet}")
        print(f"ID del tweet: {response.data['id']}")
    except tweepy.errors.Forbidden as e:
        print(f"Error al publicar el tweet: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Archivo de texto con los tweets
archivo_tweets = 'tweets.txt'  # Cambia esto por la ruta de tu archivo

# Leer todos los tweets del archivo
tweets = obtener_siguiente_tweet(archivo_tweets)

# Bucle infinito para publicar un tweet cada 24 horas en orden
indice = 0
while True:
    if indice < len(tweets):
        tweet = tweets[indice].strip()  # Elimina espacios y saltos de línea
        publicar_tweet(tweet)
        indice += 1  # Avanza al siguiente tweet
    else:
        print("No hay más tweets por publicar. Reiniciando el ciclo...")
        indice = 0  # Reinicia el índice para volver a publicar desde el principio
    time.sleep(86400)  # Espera 24 horas (86400 segundos)
