import json
from datetime import datetime
import sqlite3
from flask import Flask, jsonify
import requests
import pandas as pd
from sqlalchemy import create_engine


app = Flask(__name__)


#LISTA COM ELEMENTOS
lista_cidades = [
    "Salvador",
    "Feira de Santana",
    "Vitória da Conquista",
    "Camaçari",
    "Juazeiro",
    "Itabuna",
    "Lauro de Freitas",
    "Rio de Janeiro",
    "Petrópolis",
    "São Paulo",
]


#FUNÇÕES
def coleta_clima():
    url = "https://api.openweathermap.org/data/2.5/weather"
    parametro = {
        "appid": "7058a786edbe467bb14b38cd5bdc54dd",
    }
    dados = []
    for cidade in lista_cidades:
        parametro["q"] = cidade
        consulta = requests.get(url, params=parametro)

        if consulta.status_code == 200:
            dado = consulta.json()
            dados.append(dado)
        else:
            print(f"Error: {consulta.status_code} - {consulta.text}")
    return dados


def gerar_tabela():
    dia = datetime.now()

    valores = coleta_clima()
    valores = [json.dumps(item) for item in valores]

    dados_df = {
        'Tipo': [f"Clima {cidade}" for cidade in lista_cidades],
        'Valores': valores,
        'Uso': ["Previsão do Tempo"] * len(valores),
        'Data de Ingestão': [dia] * len(valores)
    }

    df = pd.DataFrame(dados_df)

    engine = create_engine('sqlite:///dados_armaz.db', echo=False)

    df.to_sql('tabela_tempo', con=engine, if_exists='replace', index=False)

    return df


def conexao_banco():
    conn = sqlite3.connect('dados_armaz.db')
    return conn


#ROTAS
@app.route('/')
def inciar_api():
    return 'API Flask Rodando!'

@app.route('/etl')
def sua_funcao_etl():
    return 'ETL ok'

@app.route('/clima')
def clima():
    if 'cached_response' not in app.config:
        app.config['cached_response'] = gerar_tabela().to_dict(orient='records')

    return jsonify(app.config['cached_response'])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
