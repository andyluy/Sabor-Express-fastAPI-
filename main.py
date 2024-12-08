from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint básico para retornar a mensagem "Hello, World!"
    '''
    return {'Hello' : 'World'}

@app.get('/api/restaurantes/')
def get_restairamtes(restaurante: str = Query(None)):

    '''
    Endpoint para buscar informações sobre um restaurante específico.

    Args:
        restaurante (str, optional): Nome do restaurante a ser buscado. Defaults to None.
    '''

    # Faz uma requisição HTTP GET para obter os dados dos restaurantes
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Converte a resposta JSON para um dicionário Python
        dados_json = response.json()

        # Se nenhum restaurante foi especificado, retorna todos os dados
        if restaurante is None:
            return{'dados':dados_json}

        # Filtra os dados para encontrar o restaurante especificado
        dados_restaurante = []
        for item in dados_json:
            if item ['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return {'Restaurante':restaurante,'Cardápio':dados_restaurante}
    else:
        # Retorna uma mensagem de erro caso a requisição falhe
        return {'Erro' :f'{response.status_code} - {response.text}'}
