import pandas as pd

planilha = pd.read_excel('aula 10/Planilha.xlsx')
print(planilha)

# A linha 7 localiza a linha, no caso é a 19 e adiciona um vetor com as informações
planilha.loc[len(planilha)] = ['Ivan Paulino', 40,'M', 85,1.75]

planilha.loc[len(planilha)] = ['Izabel', 17,'F', 78,1.85]

# a linha 11 atualiza
planilha.loc[19] = ['Ivan Paulino', 40,'M', 85,1.75]

#remove um registro da planilha
planilha = planilha.drop(19)

#ou

planilha.drop(19, inplace=True)

planilha.loc(19, "Idade") = 25
planilha.loc(19, ["Idade", 'Peso']) = 25, 112



print(f'A planilha tem {len(planilha)} linhas')

