"""
Para que o código funcione, será necessário a instalação da extensão
AnkiConnect no programa Anki

Anki -> Tools -> Add-ons -> Get Add-ons (ou simplesmente Ctrl+Shift+A)
Use o código 2055492159 para adicionar a extensão

Ao adicionar a extensão, reinicie o programa.

Lembre-se: quando for executar este código, mantenha o programa Anki aberto.

"""

import requests
import json

# Defina a URL do servidor da extensão AnkiConnect
ANKICONNECT_URL = "http://localhost:8765"

# Defina o tipo da NOTA
TIPO_NOTA = "Basic"

# Defina o deck para onde a nota (card) será adicionada
NOME_DECK = "Medicina" # Se o deck não existir, ele não será criado e o card não será adicionado

# Defina sua lista de notas/cards a serem adicionadas
cards = [
    # Você também pode inserir tags HTML
    {'Front': 'A frente do seu card aqui', 'Back': 'O verso do seu card aqui'},
    {'Front': 'Texto a ser exibido no frente do card', 'Back': 'texto a ser exibido no verso do card'},
    {'Front': '<h2>Card</h2><p>paragrafo aqui</p>', 'Back': '<p>texto a ser exibido no verso do card</p>'},
]

# Crie um loop para adicionar os cards
for card in cards:
    # Crie o card
    campos = card
    # Adicione o card ao deck
    novo_card = {
        'deckName': NOME_DECK,
        'modelName': TIPO_NOTA,
        'fields': campos,
        'options': {
            "allowDuplicate": False,
        },
        'tags': []
    }

    # Prepare os dados da requisição
    dados_requisicao = json.dumps({
        'action': 'addNote',
        'version': 6,
        'params': {
            'note': novo_card
        }
    })

    # Faça a requisição para o servidor AnkiConnect
    resposta = requests.post(ANKICONNECT_URL, dados_requisicao)

    # Verifique se a requisição foi bem sucedida
    if resposta.status_code == 200:
        print(f'O card {card} foi adicionado com sucesso')
    else:
        print(f'O AnkiConnect retornou o código de erro {resposta.status_code}')
