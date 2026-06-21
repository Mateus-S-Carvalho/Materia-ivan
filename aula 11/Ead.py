'''1) Considere que a tabela abaixo representa uma planilha do Excel chamada
estudantes.xlsx. Crie o código para importar a bibliote pandas e para ler a planilha
do Excel para um DataFrame chamado tabela.'''

import pandas as pd 

tabela = pd.read_excel('aula 11/dados.xlsx', sheet_name='alunos')

print(tabela.head(5)) #Lê os 5 primeiros 
print(tabela.tail(5)) # Lê os 5 ultimos


tabela.loc[len(tabela)] = [5, 'enzo', 'Tecnico em jogos', '1GMA']
print(tabela)

