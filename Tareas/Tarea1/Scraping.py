import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

#LUIS ROLANDO CALCINA QUISPE

url = "https://www.w3schools.com/html/html5_video.asp"  


os.makedirs("imagenes", exist_ok=True)
os.makedirs("audios", exist_ok=True)
os.makedirs("videos", exist_ok=True)
os.makedirs("textos", exist_ok=True)

# Obtener contenido
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extraer texto
textos = soup.get_text()
with open("textos/contenido.txt", "w", encoding="utf-8") as file:
    file.write(textos)

# Extraer imagen
imagenes = soup.find_all("img")
for i, img in enumerate(imagenes):
    src = img.get("src")
    if src:
        img_url = urljoin(url, src)
        try:
            img_data = requests.get(img_url).content
            with open(f"imagenes/imagen_{i}.jpg", "wb") as f:
                f.write(img_data)
        except Exception as e:
            print(f"Error al descargar imagen: {img_url} -> {e}")

# Extraer audio
audios = soup.find_all("audio")
for i, audio in enumerate(audios):
    src = audio.get("src")
    if src:
        audio_url = urljoin(url, src)
        try:
            audio_data = requests.get(audio_url).content
            with open(f"audios/audio_{i}.mp3", "wb") as f:
                f.write(audio_data)
        except Exception as e:
            print(f"Error al descargar audio: {audio_url} -> {e}")

# Extraer video
videos = soup.find_all("video")
for i, video in enumerate(videos):
    src = video.get("src")
    if src:
        video_url = urljoin(url, src)
        try:
            video_data = requests.get(video_url).content
            with open(f"videos/video_{i}.mp4", "wb") as f:
                f.write(video_data)
        except Exception as e:
            print(f"Error al descargar video: {video_url} -> {e}")

print("Extracción completada.")
