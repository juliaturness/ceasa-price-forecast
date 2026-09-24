import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

BASE_URL = "https://www.ceasa.sc.gov.br"


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