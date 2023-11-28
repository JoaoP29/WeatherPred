from flask import Flask, request, jsonify
import requests
from googletrans import Translator
from datetime import datetime

app = Flask(__name__)

# Chave da API da OpenWeatherMap
api_key = "SUA CHAVE DE API AQUI"

# Função para converter temperatura de Kelvin para Celsius
def kelvin_para_celsius(temp_kelvin):
    return temp_kelvin - 273.15

# Função para traduzir texto para um idioma específico
def traduzir(texto, idioma_destino='pt'):
    translator = Translator()
    traducao = translator.translate(texto, dest=idioma_destino)
    # Torna maiúscula a primeira letra da tradução
    return traducao.text.capitalize()

# Função para converter o Unix timestamp para data e hora legíveis
def converter_unix_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

# Rota para obter a previsão do tempo
@app.route('/previsao_tempo/<cidade>', methods=['GET'])
def obter_previsao_tempo(cidade):
    if not cidade:
        return jsonify({'erro': 'Parâmetro "cidade" é obrigatório'}), 400

    # Chamada à API da OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    # Verifique se a chamada foi bem-sucedida
    if response.status_code != 200:
        return jsonify({'erro': 'Erro ao obter dados de previsão do tempo'}), 500

    # Extraia os dados relevantes
    temperatura_kelvin = data['main']['temp']
    descricao = data['weather'][0]['description']
    data_previsao_unix = data['dt']

    # Converta a temperatura para Celsius
    temperatura_celsius = kelvin_para_celsius(temperatura_kelvin)

    # Traduza a descrição para o idioma desejado (opcional)
    descricao_traduzida = traduzir(descricao, idioma_destino='pt')

    # Converta o Unix timestamp para uma data legível
    data_previsao = converter_unix_timestamp(data_previsao_unix)

    resultado = {
        'Cidade': cidade,
        'Temperatura': f'{temperatura_celsius:.2f} ºC',
        'Descrição': descricao_traduzida,
        'Data prevista': data_previsao
    }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
