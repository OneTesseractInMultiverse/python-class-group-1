# Para instalar la dependencia que permite consumir servicios HTTP, tenemos que
# digitar lo siguiente: pip install requests

import requests
import pprint

stop_words = None
response = requests.get(url="http://codelab.subvertic.com/api/v1/stopwords/es")
if response.status_code == 200:
    stop_words = response.json()["swlist"]
    print(stop_words[0])
if 400 <= response.status_code < 500:
    print("La petición HTTP no es correcta [{}]".format(response.status_code))
print(response.status_code) # Leer el código de estado HTTP