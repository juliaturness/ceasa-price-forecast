import requests
from bs4 import BeautifulSoup
from config import settings

HEADERS = { "User-Agent":settings.user_agent}

BASE_URL = settings.ceasa_base_url

def pegar_sopa(url):
    resposta = requests.get(url, headers=HEADERS)
    return BeautifulSoup(resposta.text, "html.parser")


def listar_anos():
    sopa = pegar_sopa(f"{BASE_URL}/index.php/cotacao-de-precos")
    prefixo = "/index.php/cotacao-de-precos/"

    anos = set()
    for link in sopa.find_all("a"):
        href = link.get("href")
        if href is None:
            continue
        if href.startswith(prefixo):
            parte_final = href.replace(prefixo, "")
            if parte_final[:4].isdigit():
                anos.add(href)

    return sorted(anos)


if __name__ == "__main__":
    for link in listar_anos():
        print(link)