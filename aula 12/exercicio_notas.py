import pandas

df_notas = pandas.read_excel("aula 12/notas_estudantes.xlsx", sheet_name="Notas")
df_atividades = pandas.read_excel("aula 12/notas_estudantes.xlsx", sheet_name="Atividades")

print(df_notas)
print(df_atividades)

# 2 Inserção de registro
'''
Nome: 'Lucas Silva'
Atividade: 'Prova Final'
Nota: 8.5
'''
df_notas.loc[len(df_notas)] = ['Lucas Silva', 'Prova Final', 8.5]
print(df_notas)

# 3 Atualização de dados

# v1
df_notas.loc[1, "Nota"] = 9
print(df_notas)

# v2
condicao1 = df_notas['Nome'] == 'Ana Souza'
condicao2 = df_notas['Atividade'] == 'Trabalho 1'

df_notas.loc[condicao1 & condicao2, 'Nota'] = 9

print(df_notas)

# 4 Exclusão de registro

# v1
df_notas.drop(2, inplace=True)
print(df_notas)

# v2
condicao1 = df_notas["Nome"] == "Pedro Santos"
condicao2 = df_notas["Atividade"] == "Prova 1"

resposta = df_notas.loc[condicao1 & condicao2]
print(resposta)

# excluir o registro encontrado
df_notas.drop(resposta.index, inplace=True)

print(df_notas)

#5 Filtragem Simples
print('-'*100)

condicao2 = df_notas["Nota"] > 7

resposta = df_notas.loc[condicao2]
print(resposta)

#6 Agrupamento 
resposta = df_notas.groupby("Nome")["Nota"].mean()
print(resposta)

#7 Projeção de colunas
print(df_notas.loc[:, ["Nome", "Nota"]])

print('-'*100)

#8 Filtragem por texto
condicao1 = df_notas['Atividade'] == "Prova Final"
resposta = df_notas.loc[condicao1]
print(resposta)

#9 Filtragem composta e Projeção
condicao1 = df_notas["Nota"] > 7
condicao2 = df_notas['Atividade'] == "Prova Final"
resposta = df_notas.loc[condicao1 & condicao2, ["Nome", "Nota"]]
print(resposta)

#10 Ordenação

resposta = df_notas.sort_values("Nome", ascending=True)
print(resposta)

#11 Junção de DataFrames
nova_planilha = pandas.merge(df_notas, df_atividades, on="Atividade", how="inner") 
print(nova_planilha)

#12 Exportação de Dados
df_notas.to_excel("PlanilhaNova.xlsx", index=False)