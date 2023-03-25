import requests

#ETAPE 2
import requests

#ETAPE 3
URL = str(input('URL: '))

#ETAPE 4
request = requests.get(URL)

#ETAPE 5
print(request.text)                