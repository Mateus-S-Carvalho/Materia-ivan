import requests

urlNomes = 'https://economia.awesomeapi.com.br/json/available'
responseN = requests.get(urlNomes)
dadosN = responseN.json()


print('\n')
for abreviacao, nome in dadosN.items():
    print(f'Você pode usar "{abreviacao}" para a combinação "{nome}"')
    print('-' * 85)


print('Digite a moeda que deseja sabe o valor:')
moedaDesejada = input()
print('Digite a moeda que usara como base:')
moedaReferente = input()


url = f"https://economia.awesomeapi.com.br/json/last/{moedaReferente}-{moedaDesejada}"



response = requests.get(url)
dados = response.json()

print(dados)

