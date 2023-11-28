# WeatherPred
Trabalho final de DAD. É pra ser simples mesmo.

Documentação da API Weather Pred
Introdução
Bem-vindo à Documentação da API de Previsão do Tempo! Esta API foi desenvolvida em Python usando o framework Flask e integra a OpenWeatherMap para fornecer informações de previsão do tempo. Siga as instruções abaixo para configurar o ambiente, instalar as bibliotecas necessárias e obter uma chave de API.

Configuração do Ambiente
Certifique-se de ter o Python instalado em sua máquina. Se ainda não o tiver, você pode baixá-lo em python.org.

Instalação das Bibliotecas
Abra o terminal e execute o seguinte comando para instalar as bibliotecas necessárias:

pip install Flask requests googletrans==4.0.0-rc1

Flask: Framework web Python para construir APIs. Facilita a criação de rotas, gerenciamento de requisições e respostas;
Requests: Biblioteca simplificada para realizar requisições HTTP. Utilizada para acessar a API da OpenWeatherMap e obter dados de previsão do tempo;
Googletrans==4.0.0-rc1: Interface Python para o Google Translate API, empregada na tradução de descrições obtidas da API de previsão do tempo.

Obtendo a Chave da API da OpenWeatherMap
Crie sua própria chave. Para isso, basta seguir os passos a seguir:

Acesse OpenWeatherMap e crie uma conta;
Faça login em sua conta e vá para a seção de API Keys;
Crie uma nova chave de API.

Configuração da Chave de API
Abra o arquivo app.py e substitua a variável api_key pelo valor da sua chave de API da OpenWeatherMap.

api_key = "SUA_CHAVE_AQUI"

Iniciando a API
No terminal, navegue até o diretório onde está o arquivo app.py e execute o seguinte comando:

python app.py

A API estará disponível em http://localhost:5000.

Uso da API

Obter Previsão do Tempo
Endpoint: /previsao_tempo/<cidade>

Método: GET

Parâmetros:
<cidade> (obrigatório): Nome da cidade para a qual você deseja obter a previsão do tempo.

Exemplo de Chamada:
curl http://localhost:5000/previsao_tempo/Londres
OBS: Também é possível realizar essa chamada direto no navegador, ao digitar a URL em seu mesmo formato na barra de endereço.

Exemplo de Resposta:
{
  "Cidade": "Londres",
  "Data prevista": "15/11/2023 14:30:00",
  "Descrição": "Céu limpo",
  "Temperatura": "20.00 ºC".
}

Possíveis Usos
A API Weather Pred pode ser utilizada em inúmeras aplicações, dentre elas:
Desenvolvimento de Aplicações Móveis: Integre esta API em aplicativos móveis para fornecer aos usuários informações de previsão do tempo em tempo real;
Aplicações Web: Incorpore os dados da previsão do tempo em seu site para manter os visitantes informados sobre as condições climáticas;
Integração com Sistemas Internos: Utilize a API para integrar informações de previsão do tempo em sistemas internos de monitoramento ou planejamento;
Análise de Dados: Colete dados históricos da API para análises de longo prazo ou para identificar padrões climáticos em uma determinada região.
Lembre-se de sempre respeitar os termos de serviço da OpenWeatherMap e garantir que o uso da API esteja de acordo com as políticas deles. Este é um guia básico, e você pode expandir e personalizar a API conforme necessário para atender às suas necessidades específicas.
