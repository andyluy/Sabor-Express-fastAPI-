import requests
import json

# URL da API que contém os dados dos restaurantes
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

# Faz uma requisição GET para a API
response = requests.get(url)
print(response)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Converte a resposta JSON para um dicionário Python
    dados_json = response.json()

    # Cria um dicionário para armazenar os dados dos restaurantes, organizados por nome
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']

        # Verifica se o restaurante já existe no dicionário
        if nome_do_restaurante not in dados_restaurante:
            # Se não existir, cria uma nova entrada no dicionário
            dados_restaurante[nome_do_restaurante] = []

        # Adiciona o item do cardápio ao restaurante correspondente
        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
    
    # Imprime os dados dos restaurantes (para fins de depuração)
    print(dados_json)
else:
    # Imprime uma mensagem de erro caso a requisição falhe
    print(f'O erro foi {response.status_code}')

    # Cria um arquivo JSON para cada restaurante
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        # Escreve os dados do restaurante no arquivo JSON, formatado
        json.dump(dados, arquivo_restaurante, indent=4)