# Atividades Data Visualization

O objetivo desta atividade é criar um data visualization com alguma ferramenta entre: Metabase, Grafana ou PowerBI

## Escolha e justificativa da ferramenta
A ferramenta escolhida para a visualização foi o Power BI, da Microsoft. O primeiro motivo para essa escolha foi a fácil interação com arquivos Excel (formato em que os dados a serem manipulados estavam), sendo extremamente fácil e indicativa a importação e manipulação de dados nesse formato (.xlsx) na ferramenta. O segundo motivo é a fácil interface para criação de views: ao contrários de outras ferramentas, não é necessário manipular dados em "linguagem" SQL, basta arrastar diretórios e marcar checkboxes, uma interface bem familiar presente nos aplicativos do pacote Office. O terceiro e último motivo é a profundidade de interações que as views no Power BI permitem.

![apps 9729 14405452487353876 a6612b1c-3bfc-46da-ad7e-0dd83b65757d](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/a4a81e1a-88d8-4695-ad27-816da64cd27c)

## Importação de dados
Logo que o Power BI for aberto, basta fazer uma busca do arquivo a ser manipulado em sua máquina local. Feito isso, as colunas presentes nos dados já estarão organizadas para gerar as views.

![image](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/4d8a138b-ac02-4ab3-a705-64daa6c6d720)

## Visualização de Dados

A base de dados escolhida para desenvolver as views foi a "restricao_produtos_servicos_saude" do conjunto da POF. Essa base explora detalhes sobre a restrição à serviços e produtos ao longo do país.
<br>
<br>
A primeira view desenvolvida utiliza como base a estrutura de gráfico de pizza, comparando numericamente a incidência de casos de restrição de serviços e produtos na região urbana e rural no Brasil.
<br>
![BI 1](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/218deb01-1a52-4cb2-8ccb-5b5efbeb7a39)
<br>
Analisando o gráfico, é possível observar que proporcionalmente a região rural do Brasil sofre mais pela falta de acesso à produtos e serviços (a falta de acesso representa cerca de 25%, sendo que a população rural representa apenas 15,6% conforme o IBGE de 2010). Contudo, em números absolutos, a região urbana ainda sofre mais por essa falta de acesso.
<br>
<br>
A segunda view desenvolvida utiliza como base a estrutura de gráfico de colunas, comparando numericamente a incidência de casos de restrição de serviços e produtos por cada estado brasileiro.
<br>
![BI 4](https://github.com/joaomtm/Atividades_Mod8/assets/99208815/72a27bff-d767-4792-99e1-3ea8723aee88)
<br>
Analisando o gráfico, é possível observar que o Rio Grande do Sul é o que mais sofre de acesso a produtos e serviços, seguido de três estados do Nordeste (Bahia, Pernambuco, Maranhão). O primeiro estado possivelmente sofre por sua geolocalização, os outros por possíveis problemas de pobreza. 
<br>
<br>
Diante dessas views, é possível perceber quais mercados regionais estão mais aquecidos e quais ainda não foram explorados, tudo isso com base na capacidade de acesso a serviços e produtos da população brasileira.





