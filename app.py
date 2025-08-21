# from bs4 import BeautifulSoup as bs4
from datetime import datetime
from src.endpoints import urls
from src.methods.utils import Utils
from src.methods.extract import Extract

# Variaveis de Configuração
query = "data engineer"
path = "lake"
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day

utils = Utils()

utils.createDir(f"{path}")
utils.createDir(f"{path}/{year}")
utils.createDir(f"{path}/{year}/{month}")
utils.createDir(f"{path}/{year}/{month}/{day}")

extract = Extract(
    urls= urls,
    date= {
        "year"  : year,
        "month" : month,
        "day"   : day,
    },
    utils= utils
)

job_titles = [
    "Python Developer Junior",
    "Backend Developer Junior (Python)",
    "Fullstack Developer Junior (com Python)",
    "Django Developer Junior",
    "Flask Developer Junior",
    "FastAPI Developer Junior",
    "Data Engineer Junior",
    "Data Analyst Junior (Python)",
    "Machine Learning Engineer Junior",
    "AI Engineer Junior (Python)",
    "DevOps Engineer Junior (Python scripting)",
    "Automation Engineer Junior (Python)",
    "QA Engineer Junior (Python Testing)",
    "ETL Developer Junior (Python)",
    "Bioinformatics Developer Junior (Python)"
]

job_titles_br = [
    "Desenvolvedor Python Júnior",
    "Desenvolvedor Backend Júnior (Python)",
    "Desenvolvedor Fullstack Júnior (com Python)",
    "Desenvolvedor Django Júnior",
    "Desenvolvedor Flask Júnior",
    "Desenvolvedor FastAPI Júnior",
    "Engenheiro de Dados Júnior",
    "Analista de Dados Júnior (Python)",
    "Cientista de Dados Júnior",
    "Engenheiro de Machine Learning Júnior",
    "Engenheiro de DevOps Júnior (Python/Scripts)",
    "Engenheiro de Automação Júnior (Python)",
    "Analista de QA Júnior (Testes com Python)",
    "Desenvolvedor ETL Júnior (Python)",
    "Analista de Business Intelligence Júnior (com Python)"
]

job_titles_br_top5 = [
    "Desenvolvedor Python Júnior",
    "Desenvolvedor Backend Júnior (Python)",
    "Engenheiro de Dados Júnior",
    "Analista de Dados Júnior (Python)",
    "Cientista de Dados Júnior"
]

for job in job_titles_br_top5:
    extract.extractData(query=job)