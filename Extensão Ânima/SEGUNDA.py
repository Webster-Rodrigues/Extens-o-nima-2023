
#Primeiro exemplo de PANDAS

import pandas as pd
import openpyxl

combustiveis_df = pd.read_excel("NovaBase.xlsx")
combustiveis_df.head()

print(combustiveis_df)

#Mostrar o tipo de dado
print(combustiveis_df.info())

#Visualizar estatísticas básicas
print(combustiveis_df.describe())

#Filtrar por coluna (cria uma lista e usa o nome da colunaex)
print(combustiveis_df["Revenda"])


#Criar um novo dataframe apenas com as colunas desejadas
especificas_df = combustiveis_df[["Revenda", "Municipio", "Produto", "Valor de Venda"]]
print(especificas_df)

'''Criei uma nova base de dados a partir de um dataframe, porque utilizei o Pycharm e não era possível a visualização 
das 4 colunas escolhidas. Então para ter certeza que estava dando certo coloquei no excel e já está pronto
para ser utilziado.'''
especificas_df.to_excel('especificas.xlsx', sheet_name = "Planilha com dados selecionados")


'''Criar um dataframe gasolina_df contendo  apenas as 4 colunas (Revenda, Municipio, Produto, Valor de Venda) 
somente com combustível sendo GASOLINA. Com a utilização da ferramenta LOC[]'''

gasolina_df = especificas_df.loc[especificas_df["Produto"] == 'GASOLINA']
print(gasolina_df)
#Mesmo caso que o anterior, poderia criar um arquivo em excel apenas disso se quisesse
print(gasolina_df.max())
'''serve para visualizar qual o maior preço vendido da gasolina e o município onde é vendido
#a resposta é Município: XANXERE com o valor de  R$7.99'''


#DataFrame.loc[] com múltiplas condições para filtragem
'''Quais são os preços, postos que vendem ETANOL na minha cidade (São Paulo)
ordenado do menor valor de venda para o maior'''

etanol_SaoPaulo_df = especificas_df.loc[(especificas_df["Produto"] == "ETANOL") &
                                        (especificas_df["Municipio"] == "SAO PAULO")]
print(etanol_SaoPaulo_df.sort_values(by = "Valor de Venda"))
etanol_SaoPaulo_df.to_excel('etanol_SaoPaulo.xlsx', sheet_name = "ETANOL em São Paulo")
#Achei interessante criar um base de dados de uma cidade interira, seria útil em caso de relatórios.

#Qual a média de preços dos combustíveis GASOLINA e GASOLINA ADITIVADA do Bairro MOOCA em SÃO PAULO?
mooca_df = combustiveis_df. loc[(combustiveis_df["Municipio"] == "SAO PAULO") &
                                (combustiveis_df["Bairro"] == "MOOCA") &
                                ((combustiveis_df["Produto"] == "GASOLINA") |
                                (combustiveis_df ["Produto"] == "GASOLINA ADITIVADA"))]
print(f'{mooca_df["Valor de Venda"].mean():.2f}')


# Como mostrar média de valor de venda POR COMBUSTÍVEL do Brasil
media_Combustivel_Brasil_df = especificas_df[["Produto", "Valor de Venda"]].groupby(by = "Produto").mean().round(2)
print(f'{media_Combustivel_Brasil_df}')


#Adicionar uma coluna de valor booleano no combustiveis_df chamada "Ativo" que, por padrão, vai ser True para TODAS as linhas
combustiveis_df["Ativo"] = True
print(f'{combustiveis_df.head().info()}')




