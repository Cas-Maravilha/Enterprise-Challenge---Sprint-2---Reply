# Estrutura de Arquivos do Projeto

Este documento descreve a estrutura de arquivos recomendada para o Sistema de Monitoramento Industrial com ESP32.

## Estrutura de Diretórios

```
sistema-monitoramento-industrial/
├── firmware/                      # Código para o ESP32
│   ├── main.py                    # Código principal
│   ├── main_csv.py                # Versão com saída CSV
│   ├── boot.py                    # Script de inicialização
│   └── wokwi_diagram.json         # Configuração do circuito
│
├── scripts/                       # Scripts de automação
│   ├── serial_data_collector.py   # Coleta de dados via serial
│   ├── scenario_simulator.py      # Simulador de cenários
│   ├── run_simulation.bat         # Script para Windows
│   └── run_simulation.sh          # Script para Linux/Mac
│
├── analysis/                      # Scripts de análise
│   ├── sensor_analytics.py        # Análise e visualização
│   ├── anomaly_detection.py       # Detecção de anomalias
│   ├── interactive_dashboard.py   # Dashboard interativo
│   └── run_analysis.bat           # Script de análise
│
├── data/                          # Dados coletados e simulados
│   ├── normal/                    # Cenário normal
│   ├── alert/                     # Cenário de alerta
│   └── failure/                   # Cenário de falha
│
├── docs/                          # Documentação
│   ├── images/                    # Screenshots e diagramas
│   ├── setup.md                   # Instruções de configuração
│   ├── hardware.md                # Detalhes do hardware
│   └── analysis.md                # Guia de análise de dados
│
├── .github/                       # Configurações do GitHub
│   ├── ISSUE_TEMPLATE/            # Templates para issues
│   └── workflows/                 # GitHub Actions workflows
│
├── README.md                      # Documentação principal
├── CONTRIBUTING.md                # Guia de contribuição
├── CODE_OF_CONDUCT.md             # Código de conduta
├── LICENSE                        # Licença do projeto
├── .gitignore                     # Configuração do Git
└── requirements.txt               # Dependências Python
```

## Organização dos Arquivos

### Firmware

- `main.py`: Código principal para o ESP32 com transmissão MQTT
- `main_csv.py`: Versão alternativa com saída CSV via monitor serial
- `boot.py`: Script executado na inicialização do ESP32
- `wokwi_diagram.json`: Configuração do circuito para simulação no Wokwi

### Scripts

- `serial_data_collector.py`: Script para coletar dados via porta serial
- `scenario_simulator.py`: Script para simular diferentes cenários de dados
- `run_simulation.bat`: Script batch para Windows para executar simulação
- `run_simulation.sh`: Script shell para Linux/Mac para executar simulação

### Analysis

- `sensor_analytics.py`: Script para análise e visualização de dados
- `anomaly_detection.py`: Script para detecção de anomalias
- `interactive_dashboard.py`: Dashboard interativo com Dash e Plotly
- `run_analysis.bat`: Script para executar análise completa

### Data

- `normal/`: Dados coletados em cenário normal
- `alert/`: Dados coletados em cenário de alerta
- `failure/`: Dados coletados em cenário de falha

### Docs

- `images/`: Screenshots, diagramas e outras imagens
- `setup.md`: Instruções detalhadas de configuração
- `hardware.md`: Especificações e detalhes do hardware
- `analysis.md`: Guia para análise de dados

### Arquivos na Raiz

- `README.md`: Documentação principal do projeto
- `CONTRIBUTING.md`: Guia para contribuição
- `CODE_OF_CONDUCT.md`: Código de conduta para contribuidores
- `LICENSE`: Licença do projeto (recomendado MIT)
- `.gitignore`: Configuração para ignorar arquivos no Git
- `requirements.txt`: Lista de dependências Python

## Convenções de Nomenclatura

1. **Arquivos Python**: Use snake_case para nomes de arquivos Python
   - Exemplo: `serial_data_collector.py`

2. **Documentação**: Use CamelCase para títulos de documentos
   - Exemplo: `SetupGuide.md`

3. **Diretórios**: Use lowercase para nomes de diretórios
   - Exemplo: `firmware/`

4. **Arquivos de Dados**: Use o formato `tipo_timestamp.csv`
   - Exemplo: `normal_20230615_120000.csv`

## Organização de Código

1. **Imports**: Organize imports em grupos (standard library, third-party, local)
2. **Classes**: Uma classe principal por arquivo
3. **Funções**: Funções relacionadas agrupadas em arquivos
4. **Constantes**: Definidas no topo do arquivo
5. **Documentação**: Docstrings para todas as funções e classes

## Versionamento

Utilize Git para controle de versão e siga o fluxo de trabalho:

1. `main`: Branch principal, sempre estável
2. `develop`: Branch de desenvolvimento
3. `feature/*`: Branches para novas features
4. `bugfix/*`: Branches para correções de bugs
5. `release/*`: Branches para preparação de releases

## Criação da Estrutura

Para criar esta estrutura de diretórios, execute:

```bash
# Criar diretórios principais
mkdir -p firmware scripts analysis data/normal data/alert data/failure docs/images .github/ISSUE_TEMPLATE .github/workflows

# Criar arquivos vazios para manter a estrutura no Git
touch firmware/.gitkeep scripts/.gitkeep analysis/.gitkeep data/.gitkeep docs/images/.gitkeep

# Criar arquivos de documentação básicos
touch README.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE .gitignore requirements.txt
touch docs/setup.md docs/hardware.md docs/analysis.md
```