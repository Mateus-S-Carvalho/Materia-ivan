import requests

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
response = requests.get(url)

print(response.json())

dados = response.json()
valorAlto = float(dados['USDBRL']['high'])
valorBaixo = float(dados['USDBRL']['low'])


print(f'\nData e hora que a api foi atualizada: {dados['USDBRL']['create_date']}')
print(f'\nO maior valor do dolar em Reais é: R${valorAlto:.2f}\n')
print(f'O Menor valor do dolar em Reais é: R${valorBaixo:.2f}\n')