import pandas

#manipula dados

#iremos ler uma planilha e criar um DataFrame

df = pandas.read_excel('aula 9/Planilha.xlsx')

print(df)

print('\n--------------------------------------------------------------------\n')

print(df.loc[10])

print('\n--------------------------------------------------------------------\n')

print(df.loc[10, "Nome"])
print('\n--------------------------------------------------------------------\n')

print(df.loc[10,['Nome','Idade']])

print('\n--------------------------------------------------------------------\n')
print()