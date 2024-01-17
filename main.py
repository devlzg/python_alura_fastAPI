from fastapi import FastAPI, Query
import requests
import json
app = FastAPI()

@app.get('/api/hello') #Endpoint
def hello_world():
    '''
    Endpoint que mostra uma mensagem muito importante do mundo da programação.
    '''
    return {'Hello World!'}
  
@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint que mostra o cardápio de um restaurante específico ou de todos, caso nao seja passada a query
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    
    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_do_restaurante = [] # lista
        for item in dados_json:
            if item['Company'] == restaurante: 
                dados_do_restaurante.append({
                "item": item['Item'],
                "price": item['price'],
                "description": item['description'],
            })
        return {'Restaurante': restaurante, 'Cardapio': dados_do_restaurante}
    else:
        return {'Erro':f'{response.status_code} - {response.text}'}