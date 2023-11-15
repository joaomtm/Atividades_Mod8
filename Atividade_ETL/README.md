# Atividades ETL

O objetivo desta atividade é criar uma ETL em flask com teste de integração que leia da API OpenWeather, manipulando os dados em uma tabela nova guardando as informações em 4 colunas: Data da Ingestão, Tipo, Valores, Uso.

## Organização dos Arquivos

A solução consiste em três arquivos principais:
<br>
<br>
<strong>app.py:</strong> este é o arquivo principal (formato python), ele conterá todas as funções de coleta, criação e ingestão de dados. Nele também estará as configurações de servidor/rotas. Aqui, toda a aplicação será feita.
<br>
<br>
<strong>dados_armaz.db:</strong> este é o arquivo da base de dados, é nele que ficará armazenado todos os dados coletados pela solução.
<br>
<br>
<strong>test_api.py:</strong> este é o arquivo de testes, ele verificará se todas as funções em "app.py" estão funcionando corretamente.
<br>
<br>
Os outros arquivos são referentes a cache (do pytest e arquivo python)
<br>
<br>

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/3de955d5-27aa-4d96-828a-a3589f451dc4)

## app.py, centro da solução

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/57a13fde-1cb3-4e9e-b694-9db5f03e465d)
<br>
Primeiro, é necessário importar as bibliotecas referentes à micro biblioteca flask, formas de armazenamento e transferência de dados e outras extensões python.
<br>

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/f9b2b69b-3568-4c0f-964c-a1934ca9f135)

Criação do ambiente web em flask e definição de lista de elementos a serem requeridos.
<br>

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/0531c375-e12b-48c6-8edc-8a95adcddbf9)

Definição de função para coletar dados do tempo das cidades indicadas na lista
<br>

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/e3c62c4a-97f9-4851-8818-b4cfaecafde2)
<br>
Função para a criar uma tabela e organiza-la com base nos dados coletados
<br>

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/baf1dbd6-1cfe-468f-a419-0e20d44dbfe0)
<br>
Conexão da tabela gerada com o banco de dados (função)
<br>

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/33696b1b-728d-4573-ab51-f4c8421caf04)
<br>
Definição das rotas em Flask, uma para confirmar o funcionamento do flask, outra para o funcionamento do ETL, e, por último, a rota personalizada da solução.
<br>

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/f6de8932-8812-484b-ba2c-22d7a37972a4)
<br>
Essa parte verifica se o script Python está sendo executado como o programa principal para, assim, iniciar o host da página.
<br>
<br>
Para executar o código da solução, escreva em seu terminal:
<br>
```
python app.py
```
<br>

Essa mensagem deverá aparecer em seu terminal
<br>
![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/b2283c90-0f7f-4c41-9f16-332867847787)
<br>
<br>
Acesse o endereço do servidor indicado
<br>
adicione "/clima" na url para verificar se os dados estão sendo coletados de fato. A tela a seguir deve aparecer em seu navegador:

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/b7f9baaf-5110-4a14-adc9-c126e9db0efd)
<br>
![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/a80b04c0-1df0-4790-9b03-2c366b257f51)
<br>
A base de dados também deverá aparecer na sua pasta de arquivos, já com os dados coletados.
<br>
<br>
![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/1f773f1f-4c5a-4226-a5dd-8a0525798af0)
<br>
Você pode verificar diretamente pelo DB Browser se os dados foram de fato ingeridos.
<br>
<br>
## test_api.py, testes da aplicação

A partir do pytest, uma função de teste foi construída para cada função construída anteriormente. Todas possuem o prefixo "test_" acompanhada do nome da função que está sendo testada.
<br>
<br>
<strong>Exemplo de Função Teste</strong>
<br>
![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/06fe74dd-2bbb-4e8d-9355-b79f5f3716a4)

<br>
Para executar o código de teste, escreva em seu terminal:
<br>

```
pytest test_api.py
```

<br>
Caso dê certo, a seguinte mensagem aparecerá em seu terminal:

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/42a8fe24-8067-4e4a-9d12-2fdf335acdf1)

<br>
Cada pontinho verde indica o sucesso do teste da função, totalizando 6 testes bem sucedidos (100%) 
<br>
<br>
Caso uma função esteja com algum erro, ou se sua aplicação não for bem sucedida, um alerta será indicado em respectivo:
<br>

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/8400fde4-0a8d-4c46-bef1-027053553aba)

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/587cbb32-5f21-4311-b847-b5f24924d61a)

<br>

Neste caso, o primeiro e último testes deram erro por conta da lista das cidades (lista_cidades).





