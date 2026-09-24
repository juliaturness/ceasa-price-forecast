import requests

url = "https://www.ceasa.sc.gov.br/index.php/cotacao-de-precos"

# utiliza a header pra fazer request simulando um navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

resposta = requests.get(url, headers=headers)

print(resposta.status_code)