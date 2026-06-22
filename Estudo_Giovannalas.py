#Chamamos o pandas e demos um apelido de pd
import pandas as pd

#Lemos as notas
planNotas = pd.read_excel('notas_estudantes.xlsx',sheet_name= 'Notas')
print(planNotas)

print('\n\n')

#Lemos atividades
planAtividades = pd.read_excel('notas_estudantes.xlsx',sheet_name= 'Atividades')
print(planAtividades)

print('-'*100)

#Colocamos uma nova fileira
planNotas.loc[len(planNotas)] = ['Mateus', 'Prova', 10]
print(planNotas)

print('-'*100)

#Forma 1
#Localizamos na linha 8 coluna nota e trocamos a nota 
#IMPORTANTISSIMO --> PARA A LINHA É ESTRITAMENTE NECESSARIO SER A LINHA QUE APARECE NO TERMINAL ABAIXO
planNotas.loc[8, 'Nota'] = 0
print(planNotas)

print('-'*100)

#Forma 2
#A primeira condição é que na coluna atividade tem que estar escrito trabalho 1
condicao1 = planNotas['Atividade'] == 'Trabalho 1'
#A segunda condição é que na coluna nota tem que ser 8.5 NÃO SE USA '' PARA NUMERO
condicao2 = planNotas['Nota'] == 8.5

#Ele vai localizar uma linha onde tem as duas condições e vai trocar 
planNotas.loc[condicao1 & condicao2, 'Nome'] = 'Ana escura'
print(planNotas)

print("-"*100)

#Forma 1
#Escolhemos uma linha inteira para deletar e sem criar uma copia
planNotas.drop(7, inplace=True)
print(planNotas)

print('-'*100)
#Forma 2
#A primeira condição é que na coluna atividade tem que estar escrito trabalho 1
condicao1 = planNotas['Atividade'] == 'Trabalho 1'
#A segunda condição é que na coluna nota tem que ser 8.5 NÃO SE USA '' PARA NUMERO
condicao2 = planNotas['Nota'] == 8.5

#É OBRIGATORIO O USO DO INDEX QUANDO É COLOCADO DUAS OU + CONDIÇÕES EM UMA VARIAVEL
condTotal = planNotas.loc[condicao1 & condicao2]

planNotas.drop(condTotal.index, inplace=True)
print(planNotas)

print('-'*100)

#Ele vai encontrar todas as linhas que tenha a nota 6
filtro = planNotas['Nota'] == 6
encontrados = planNotas.loc[filtro]
print(encontrados)

print('-'*100)

#Podemos fazer um agrupamento para diversas finalidades
grupo = planNotas.groupby('Nota')['Nota'].mean()
print(grupo)

print('-'*100)

#Serve para mostrar colunas especificas e é obrigatorio colocar    :,   (caso seja mais de uma coluna tem que estar dentro de [])
notas = planNotas.loc[:,['Nome','Nota']]
print(notas)

print('-'*100)

#Junta duas planilhas usando a coluna que elas tem em comum
planilhaJuntada = pd.merge(planNotas,planAtividades, on='Atividade', how='inner')
print(planilhaJuntada)

#Exportando em forma de exel
#LEMBRANDO QUE IRA EXPORTAR A PLANILHA/VARIAVEL QUE VOCÊ COLOCAR PRIMEIRO
planilhaJuntada.to_excel('Estudo_Prova_Juntada.xlsx', index=False)