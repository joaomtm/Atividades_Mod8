import json
import pytest
from datetime import datetime
from app import app, coleta_clima, gerar_tabela, conexao_banco

# FUNÇÕES TESTE

def test_coleta_clima():
    try:
        result = coleta_clima()
        assert isinstance(result, list)
        assert len(result) == len(app.config['lista_cidades'])
        print("Teste coleta_clima passou com sucesso!")
    except Exception as e:
        print(f"Erro no teste coleta_clima: {str(e)}")

def test_gerar_tabela():
    try:
        result = gerar_tabela()
        assert not result.empty
        assert 'Tipo' in result.columns
        assert 'Valores' in result.columns
        assert 'Uso' in result.columns
        assert 'Data de Ingestão' in result.columns
        print("Teste gerar_tabela passou com sucesso!")
    except Exception as e:
        print(f"Erro no teste gerar_tabela: {str(e)}")

def test_conexao_banco():
    try:
        conn = conexao_banco()
        assert conn is not None
        conn.close()
        print("Teste conexao_banco passou com sucesso!")
    except Exception as e:
        print(f"Erro no teste conexao_banco: {str(e)}")

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_inciar_api(client):
    try:
        response = client.get('/')
        assert response.data == b'API Flask Rodando!'
        print("Teste inciar_api passou com sucesso!")
    except Exception as e:
        print(f"Erro no teste inciar_api: {str(e)}")

def test_sua_funcao_etl(client):
    try:
        response = client.get('/etl')
        assert response.data == b'ETL ok'
        print("Teste sua_funcao_etl passou com sucesso!")
    except Exception as e:
        print(f"Erro no teste sua_funcao_etl: {str(e)}")

def test_clima(client):
    try:
        response = client.get('/clima')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == len(app.config['lista_cidades'])
        print("Teste clima passou com sucesso!")
    except Exception as e:
        print(f"Erro no teste clima: {str(e)}")
