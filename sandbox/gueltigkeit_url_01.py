

import requests

urls = ['https://www.google.commm', 'https://www.facebook.com', 'https://www.twitter.com']

# Lese die Liste der URLs aus der Textdatei
# with open('urls.txt', 'r') as f:
#     urls = f.read().splitlines()

# Überprüfe jede URL auf Gültigkeit
for url in urls:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} ist gültig.")
        else:
            print(f"{url} ist ungültig. Respons Code= {response.status_code}")
    except:
        print(f"{url} ist ungültig.")
