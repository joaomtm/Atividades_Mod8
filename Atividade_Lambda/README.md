# Atividades Lambda (AWS)
## Configuração do Ambiente
A solução será desenvolvida no Lambda, serviço da AWS que permite a execução de código sem provisionar ou gerenciar servidores. A linguagem escolhida é a python por conta da sua eficiência no ambiente. Além disso, o AWS Lambda também permite desenvolver funções serverless.
<br>
![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/80b856d0-96c4-4921-aeda-16076cf981f5)

## Função
A função construída em python é extremamente simples, consistindo em apenas uma dupla verificação construída por lógica. A primeira vericação confere se a requisição HTTP é POST, a segunda verifica se a senha está correta ou não
<br>
![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/63947f60-f098-4535-99ef-c57ac61e477a)

## Endpoint
O endereço do endpoint, via API Gateway, para fazer requisições é: 
<br>
https://acdwdvzao6.execute-api.us-east-1.amazonaws.com/default/joaoFunction
<br>

## Testes via Postman
Cenário:
<br>
<br>
Senha Correta
<br>
Requisição correta
<br>
<br>
Input:

```
{
  "senha": "12345"
}
```

Output:
```
{
    "mensagem": "Autenticação bem-sucedida"
}
```


![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/da97a415-d435-43dc-8bc2-f43d1b886ee0)

<br>
<br>

Cenário 2:
<br>
<br>
Senha incorreta
<br>
Requisição correta
<br>
<br>
Input:

```
{
  "senha": "1234"
}
```

Output:
```
{
    "mensagem": "Credenciais inválidas"
}
```

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/aecfa907-f202-4f4d-9da9-0e429dd1d1ae)
<br>
<br>
Cenário 3:
<br>
<br>
Senha correta
<br>
Requisição incorreta
<br>
<br>
Input:

```
{
  "senha": "12345"
}
```

Output:
```
Apenas solicitações POST são permitidas.
```
![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/8c75ffeb-2cb9-4004-a907-0557f53ba5bd)


Cenário 4 (especial):
<br>
campo senha não identificado
<br>
<br>
Input:

```
{
  "nome": "12345"
}
```

Output:
```
{
    "mensagem": "Campo 'senha' não encontrado na solicitação"
}
```

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/a1e09f80-d471-4e1a-add7-c8350c7ec501)








