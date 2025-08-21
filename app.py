import os
import requests
# from bs4 import BeautifulSoup as bs4
from datetime import datetime
from endpoints import urls


# Variaveis de Configuração
query = "data engineer"
path = "lake"
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day

def createDir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

createDir(f"{path}")
createDir(f"{path}/{year}")
createDir(f"{path}/{year}/{month}")
createDir(f"{path}/{year}/{month}/{day}")


def extractData(query):
    for site, data in urls.items():
        endpoint = data["url_q"] + query.replace(" ", "+")
        print(endpoint)
        createDir(f"{path}/{year}/{month}/{day}/{site}")
    
        html_response = requests.get(endpoint)
        if html_response.status_code == 200:
            # query = query.replace(" ", "_")
            file_name_path = f"{path}/{year}/{month}/{day}/{site}/{query.replace(" ", "_")}.html"
            with open(file_name_path, "w") as f:
                f.write(html_response.text)


extractData(query)