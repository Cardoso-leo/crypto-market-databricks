📘 Crypto Market Analytics Pipeline — Databricks & Delta Lake

🧠 Visão Geral

Este projeto consiste na construção de um pipeline completo de dados para análise do mercado de criptomoedas, utilizando Databricks, Delta Lake e Databricks SQL.

O objetivo é demonstrar habilidades práticas em:

Ingestão de dados via API

Processamento e modelagem em camadas (Bronze, Silver e Gold)

Criação de dashboards interativos

Storytelling analítico para apoio à tomada de decisão

🏗️ Arquitetura do Projeto
🔄 Fluxo de Dados
API Coinbase
   ↓
Bronze Layer (dados brutos)
   ↓
Silver Layer (dados tratados)
   ↓
Gold Layer (indicadores analíticos)
   ↓
Databricks SQL Dashboard


📌 Arquitetura baseada no conceito de Lakehouse.

🧪 Tecnologias Utilizadas

Databricks

Apache Spark (PySpark)

Delta Lake

Databricks SQL

Python

REST API (Coinbase)

📂 Estrutura do Projeto
📁 notebooks/
 ├── 01_ingestao_bronze_crypto.py
 ├── 02_tratamento_silver_crypto.py
 └── 03_analise_gold_crypto.py

📄 README.md

🔄 Pipeline de Dados
🟤 Bronze Layer — Ingestão

Consumo de dados da API de criptomoedas

Armazenamento em formato Delta

Dados mantidos sem transformações

⚪ Silver Layer — Tratamento

Limpeza e padronização dos dados

Conversão de preços para BRL

Ajuste de tipos e nomes de colunas

Criação da tabela silver_crypto_prices

🟡 Gold Layer — Analytics

Cálculo de indicadores analíticos

Variação percentual de preços

Preparação dos dados para consumo analítico

Otimização para visualização em dashboards

📊 Dashboard Analítico

O dashboard foi desenvolvido no Databricks SQL e inclui:

📈 Market Share por Capitalização

🚀 Principais variações de preço

📋 Tabela consolidada do mercado

🚀 Como Executar o Projeto

Criar um workspace no Databricks

Importar os notebooks

Executar os notebooks na seguinte ordem:

01_ingestao_bronze_crypto

02_tratamento_silver_crypto

03_analise_gold_crypto

Acessar o dashboard no Databricks SQL

💡 Possíveis Evoluções

Agendamento automático do pipeline

Histórico temporal de preços

Alertas de variação de mercado

Integração com novas APIs

👤 Autor

Leonardo Cardoso
📍 Analista de Dados | Engenharia de Dados
🔗 LinkedIn: https://www.linkedin.com/in/leonardo-l-cardoso/
