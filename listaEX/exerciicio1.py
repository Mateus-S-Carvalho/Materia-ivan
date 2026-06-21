import pandas as pd

df_notas = pd.read_excel('listaEX/notas_estudantes.xlsx', sheet_name='Notas')
df_atividades = pd.read_excel('listaEX/notas_estudantes.xlsx', sheet_name='Atividades')

df_notas.loc[len(df_notas)] = ['Lucas Silva', 'Prova Final', 8.5]
df_notas.loc[1, 'Nota'] = 9

print(df_notas)

condicao1 = df_notas['Nome'] == 'Ana Souza'
condicao2 = df_notas['Atividade'] == 'Trabalho 1'

df_notas.loc[condicao1 & condicao2, 'Nota'] = 9