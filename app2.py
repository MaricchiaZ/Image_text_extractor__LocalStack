import requests

resposta_imagem = requests.get("http://cdn.pensador.com/img/imagens/pe/ns/pensador_mensagens_de_bom_dia_21.jpg", stream=True)
data = {'file': open(resposta_imagem.raw) }
resposta_api = requests.request("POST", "https://freeocrapi.com/api", files=data)
print(resposta_api.text)