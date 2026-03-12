import requests

def requisitar_cotacao(moeda_inicial: str, moeda_final: str):

    # URL personalizado para acessar as informações sobre a cotação. 
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_inicial}-{moeda_final}"

    # Utilizando o modulo requests para consumir a API
    resposta = requests.get(url)

    # Verificando se o acesso a API foi um sucesso. 
    if resposta.status_code == 200:

        chave_moeda = f"{moeda_inicial}{moeda_final}"
        dados_json = resposta.json()

        return dados_json[chave_moeda]
    
    else:
        return resposta.status_code
