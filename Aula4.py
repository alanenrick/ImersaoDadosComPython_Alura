# Aula 4 - Criando dashboards


#importa a biblioteca pandas e numpy
import numpy as np
from pandas import (pandas as pd)

#Define um nome para a tabela
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

#Define variavéis para armazenar a quantidade de linhas e colunas
linhas, colunas = df.shape[0], df.shape[1]

#Dicionário de renomeação
novos_nomes = {'work_year': 'ano', 'experience_level': 'senioridade', 'employment_type': 'contrato', 'job_title': 'cargo', 'salary': 'salario',
    'salary_currency': 'moeda', 'salary_in_usd': 'usd', 'employee_residence': 'residencia', 'remote_ratio': 'remoto', 'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

#Aplica Renomeação
df.rename(columns=novos_nomes, inplace=True)

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

#Exibe os campos que são nulos ou não
nulos = df.isnull()

#Exibe a soma dos campos que são nulos
soma_nulos = df.isnull().sum()

#exibir anos que constam na tabela
anos = df['ano'].unique()

#exibir as linhas que possuem valores nulos
exibir_nulos = df[df.isnull().any(axis=1)]

df_salarios = pd.DataFrame({
    'nome': ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
    'salario': [4000, np.nan, 5000, np.nan, 100000]
})

#preencher valores nulos com a média dos salários
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

#preencher valores nulos com a mediana dos salários
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median().round(2))

#Limpar dados nulos criando nova variável
df_limpo = df.dropna()

#Converter tipo de dado do ano de float64 para inteiro64
df_limpo['ano'] = df_limpo['ano'].astype('int64')

print("\n")
print(df_limpo.info())
print("\n")