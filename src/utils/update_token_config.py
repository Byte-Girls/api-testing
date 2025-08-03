import requests
from bs4 import BeautifulSoup
import os

# URL de la página Try Yourself
url = "https://api-starter-orangehrm.readme.io/reference/try-it-yourself" 

# solicitud GET a la página
response = requests.get(url)
response.raise_for_status()  # Lanza error si la respuesta no es 200

# Analiza el contenido HTML
soup = BeautifulSoup(response.text, "html.parser")

# Encuentra el tag <code> con name="OAuth2 Bearer Token"
code_tag = soup.find("code", attrs={"name": "OAuth2 Bearer Token"})
if not code_tag:
    raise ValueError('No se encontró el tag <code> con name="OAuth2 Bearer Token"')
token = code_tag.get_text(strip=True)

# Ruta al archivo config.py (sube un nivel desde 'utils')
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../config.py"))

# Leer contenido actual de config.py
with open(config_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Reescribir el valor de TOKEN
with open(config_path, "w", encoding="utf-8") as file:
    for line in lines:
        if line.startswith("TOKEN ="):
            file.write(f'TOKEN = "{token}"\n')
        else:
            file.write(line)

