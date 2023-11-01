# Read.me - Atividade Kafka

&nbsp; O objetivo dessa atividade é criar um docker-compose com todos os parâmetros de um kafka e seus gerenciadores e um exemplo de produção e consumo de mensagem local, fazendo um script pyton que funcione como consumer e e outro como producer. 

O ambiente de programação escolhido foi o VsCode. Na solução, será usado o Docker Compose para aplicar os contêineres do Zookeeper e do Kafka, nessa parte será necessário indicar as portas e endereços a serem utilizados (docker-composer.yml)

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/e5fb7688-138f-4e76-860b-60b2c8dc7893)
>Atenção: o Docker já deverá estar aberto e em execução

O  Kafka é uma plataforma de streaming de dados distribuída, usada para transmitir, armazenar e processar dados em tempo real. O Zookeeper é um serviço de coordenação distribuída, utilizado para gerenciar configurações e sincronizar nós.
<br>
<br>
## Producer
O producer irá produzir a mensagem e envia-la

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/b6e5a2d7-70cf-479e-8f56-e5c9572072db)
>Importação de biblioteca e endereço

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/039bf6a7-f463-41bc-8d83-68213b1e6693)
>Função para retornar estado do envio da mensagem

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/5a70bf00-ec1b-43f3-aa83-2994b225de76)
>Envia a mensagem para a rota e aguarda esse enviar

## Consumer
O consumer irá receber a mensagem enviada

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/62c05375-7181-4f33-86cc-74ec6f7fb88c)
>Configuração de biblioteca e endereço

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/aa7dbfc3-304b-40f5-b032-ecd91e490e4b)
>Configuração para indicar o estado do envio da mensagem

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/f7c4aeac-678b-49f7-9ed1-dcb5f0a84a88)
>Recebe a mensagem enviada e acusa o recebimento

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/ae914af8-ba2c-428b-8e92-c04bfc4800b5)
>Finalizador do processo de consumo

Para rodar o Docker pelo CMD do VsCode, use o comando 

```
docker-compose up -d
```
Confira diretamente pelo Docker se está de fato rodando:
![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/e7ba740b-60ee-4ba5-9cd5-0d5a73c33a67)

Agora basta rodar os dois scripts em Pyton:

```
python producer.py
```

```
python consumer.py
```

Assim, a mensagem será recebida com sucesso
![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/42ed4c59-c26e-4053-bfa8-37e74a6344c5)



