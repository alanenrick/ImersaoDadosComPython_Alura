# Aula 1 - Análise de Dados com Pandas
# Ensinar a carregar arquivos CSV no Google Colab, realizar leitura e visualização inicial de dados com Pandas. 
# O aluno começará a manipular bases reais de dados com comandos simples de análise.


#importa a biblioteca pandas
from pandas import (pandas as pd)

#Define um nome para a tabela
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

#Mostra as 5 primeiras linhas do arquivo
#print(df.head())

#Mostra estatísticas do arquivo
#print(df.info())

#Mostra descrição do arquivo
#print(df.describe())

#Mostra a quantidades de linhas e colunas
#print(df.shape)

#Define variavéis para armazenar a quantidade de linhas e colunas
linhas, colunas = df.shape[0], df.shape[1]

#Mostra a quantidade de linhas e colunas armazenadas nas variáveis
#print(f"linhas: {linhas} colunas: {colunas}")

#mostra os titulos(Index) das colunas
#print(df.columns)

#Dicionário de renomeação
novos_nomes = {'work_year': 'ano', 'experience_level': 'senioridade', 'employment_type': 'contrato', 'job_title': 'cargo', 'salary': 'salario',
    'salary_currency': 'moeda', 'salary_in_usd': 'usd', 'employee_residence': 'residencia', 'remote_ratio': 'remoto', 'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

#Aplica Renomeação
df.rename(columns=novos_nomes, inplace=True)

#Verificar resultado,, mostrando as primeiras 5 linhas e as 5 ultimas, além de informações sobre a tabela
#print(f"\n{df.head}")

#Verificar resultado,, mostrando as primeiras 5 linhas
#print(f"\n{df.head()}")

#Mostrar quantas vezes se repetem os níveis de senioridade
#print(f"\n{df["senioridade"].value_counts()}")

#Mostrar quantas vezes se repetem os tipos de contrato
#print(f"\n{df["contrato"].value_counts()}")

#Mostrar quantas vezes se repetem a % de remoto
#print(f"\n{df["remoto"].value_counts()}")

#Renomear siglas
senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}

df['senioridade'] = df['senioridade'].replace(senioridade)

contrato = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}

df['contrato'] = df['contrato'].replace(contrato)

tamanho_empresa = {
    'L': 'grande',
    'S': 'pequena',
    'M':	'media'

}

df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)

mapa_trabalho = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}

df['remoto'] = df['remoto'].replace(mapa_trabalho)

#Verifica novos valores
#print(f"\n{df['senioridade'].value_counts()}")
#print(f"\n{df['contrato'].value_counts()}")
#print(f"\n{df['tamanho_empresa'].value_counts()}")
#print(f"\n{df['remoto'].value_counts()}")

#Verifica tabela novamente
#print(f"\n{df.head()}")

#Exibe a quantidade de categorias únicas, qual é categoria mais frequente e sua respectiva frequência:
print(f"\n{df.describe(include='object')}")

'''O "include='object' => faz com que o método gere estatísticas descritivas apenas para as colunas do tipo "object" 
(ou seja, colunas com dados categóricos ou strings)
Com isso já conseguimos responder algumas perguntas, como:

Qual o nível de experiência mais comum na base de dados?
Qual é o tipo de contrato mais frequente?
Qual o cargo mais frequente na amostra?
De qual país são a maioria dos profissionais da base?
Qual é o país onde mais empresas da amostra estão sediadas?
Qual o regime de trabalho mais comum?
Qual é o tamanho mais comum das empresas na amostra?'''