# Simulação de Circuito com ESP32 e Sensores Virtuais

## 📋 Visão Geral
Este projeto implementa uma simulação virtual de um circuito com ESP32 e diversos sensores, utilizando Python para gerar dados realistas e simular o comportamento dos sensores em tempo real.

## 🎯 Objetivos
- Simular o comportamento de sensores comuns em projetos IoT
- Demonstrar a coleta e processamento de dados em tempo real
- Visualizar dados através de diferentes formatos (console, JSON, gráficos)
- Fornecer uma base para projetos reais com ESP32

## 🔧 Sensores Virtuais Utilizados

### 1. DHT22 (Temperatura e Umidade)
- **Justificativa**: Sensor digital preciso e confiável para medições ambientais
- **Características**:
  - Temperatura: -40°C a 80°C (±0.5°C)
  - Umidade: 0-100% (±2%)
  - Comunicação digital
  - Baixo consumo de energia
  - Excelente estabilidade a longo prazo

### 2. LDR (Sensor de Luz)
- **Justificativa**: Sensor analógico simples e efetivo para medição de luminosidade
- **Características**:
  - Faixa: 0-1023 (10 bits)
  - Resposta não-linear
  - Baixo custo
  - Fácil implementação
  - Ideal para monitoramento de ambientes

### 3. Sensor PIR (Movimento)
- **Justificativa**: Detecção de presença/movimento com baixo consumo
- **Características**:
  - Saída digital (HIGH/LOW)
  - Ângulo de detecção: ~110°
  - Alcance: ~7 metros
  - Baixo consumo
  - Ideal para monitoramento de ocupação

## 💻 Código-Fonte

### Estrutura do Projeto
```
.
├── src/esp32_simulator.py    # Script principal de simulação
├── data/                 # Diretório para armazenamento de dados
│   └── ultima_leitura.json  # Última leitura dos sensores
└── README.md            # Este arquivo
```

### Principais Componentes do Código

1. **Configuração dos Sensores**:
```python
SENSOR_PARAMS = {
    'dht22': {
        'temperature': {'mean': 25.0, 'std': 2.0, 'min': 20.0, 'max': 30.0},
        'humidity': {'mean': 60.0, 'std': 5.0, 'min': 40.0, 'max': 80.0}
    },
    'ldr': {
        'normal': {'mean': 500, 'std': 100, 'min': 0, 'max': 1023}
    },
    'pir': {
        'detection_prob': 0.1  # 10% de chance de detectar movimento
    }
}
```

2. **Geração de Dados**:
```python
def generate_dht22_data():
    """Gera dados simulados do DHT22"""
    temp = random.normalvariate(
        SENSOR_PARAMS['dht22']['temperature']['mean'],
        SENSOR_PARAMS['dht22']['temperature']['std']
    )
    # ... processamento dos dados ...
    return round(temp, 1), round(hum, 1)
```

3. **Armazenamento e Visualização**:
```python
def save_to_json(data, filename):
    """Salva os dados em formato JSON"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
```

## 📊 Visualização dos Dados

### 1. Console (Tempo Real)
```
=== Leituras dos Sensores ===
Timestamp: 2024-03-11 10:00:00
Temperatura: 25.5°C
Umidade: 62.3%
Luminosidade: 458 (0-1023)
Movimento: Detectado
```

### 2. Arquivo JSON
```json
{
  "timestamp": "2024-03-11 10:00:00",
  "sensores": {
    "dht22": {
      "temperatura": 25.5,
      "umidade": 62.3
    },
    "ldr": {
      "luminosidade": 458
    },
    "pir": {
      "movimento": 1
    }
  }
}
```

## 📈 Análise Exploratória

### Estatísticas Básicas
- **Temperatura**:
  - Média: 25.0°C
  - Variação: ±2.0°C
  - Faixa: 20.0°C - 30.0°C

- **Umidade**:
  - Média: 60.0%
  - Variação: ±5.0%
  - Faixa: 40.0% - 80.0%

- **Luminosidade**:
  - Média: 500
  - Variação: ±100
  - Faixa: 0-1023

### Insights
1. **Correlação Temperatura-Umidade**:
   - Geralmente inversa
   - Variações suaves ao longo do tempo
   - Mantém-se dentro de faixas seguras

2. **Padrões de Movimento**:
   - Detecções esporádicas (10% de probabilidade)
   - Independentes de outros sensores
   - Útil para detecção de ocupação

3. **Comportamento do LDR**:
   - Variações suaves
   - Resposta não-linear à luz
   - Valores típicos entre 400-600

## 🚀 Como Executar

1. **Pré-requisitos**:
   ```bash
   python -m pip install -r requirements.txt
   ```

2. **Executar Simulação**:
   ```bash
   python src/esp32_simulator.py
   ```

3. **Monitorar Dados**:
   - Console: Dados em tempo real
   - Arquivo: `data/ultima_leitura.json`
   - Gráficos: Implementação futura

## 🔄 Fluxo de Dados
1. Geração de dados simulados
2. Processamento e validação
3. Armazenamento em JSON
4. Visualização em tempo real
5. Análise e insights

## 📝 Notas de Implementação
- Dados gerados com distribuição normal
- Valores limitados a faixas realistas
- Timestamp em formato ISO
- JSON para fácil integração
- Console para monitoramento em tempo real

## 🔮 Próximos Passos
1. Implementar visualização gráfica
2. Adicionar mais tipos de sensores
3. Implementar detecção de anomalias
4. Criar dashboard web
5. Adicionar persistência de dados

## 📚 Referências
- [Documentação ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [Biblioteca DHT](https://github.com/adafruit/DHT-sensor-library)
- [Documentação Python](https://docs.python.org/3/)