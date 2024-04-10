# Azure AI Language Text Analytics - utilizando SDK para o Python

## Azure Text Analytics

**Text Analytics** é um serviço de IA do Azure que fornece processamento avançado de linguagem natural (NLP) em texto bruto e inclui as seguintes funções principais:

- Sentiment Analysis
- Named Entity Recognition
- Linked Entity Recognition
- Personally Identifiable Information (PII) Entity Recognition
- Language Detection
- Key Phrase Extraction
- Multiple Analysis
- Healthcare Entities Analysis

## Criando o recurso Text Analytics no Azure

Abaixo está um exemplo de como você pode criar um recurso **Text Analytics** usando a **Azure CLI**:

```bash
# Fazer login no Azure no terminal
az login
```

```bash
# Criar um Resource Group no Azure
az group create --name rg-ai --location eastus
```

```bash
# Criar o recurso Text Analytics no Azure
# obs.: usar sku "S" se "F0" não disponível
az cognitiveservices account create --name text-analytics-rs --resource-group rg-ai --kind TextAnalytics --sku F0 --location eastus --yes
```

## Obtendo o "Endpoint" e "API Key" do recurso Text Analytics no Azure

*Endpoint* e *API key* serão necessários para autenticação do *client* no Python, obtidos utilizando o **Azure CLI**:

```bash
# Pegar o endpoint do text analytics
az cognitiveservices account show --name "text-analytics-rs" --resource-group "rg-ai" --query "properties.endpoint"
```

Exemplo endpoint: `"https://eastus.api.cognitive.microsoft.com/"`

```bash
# Pegar a API Key do text analytics

```

Exemplo API Key: `{ "key1": "3269************************71cb" }`

## Instalação do SDK para o Python

Instalação do SDK do *Azure Text Analytics* para o Python usando **pip**:

```bash
pip install azure-ai-textanalytics
```

## Sentiment Analysis (Análise de Sentimento)

Analisa o texto de entrada e determina se seu sentimento é positivo, negativo ou neutro. Sua resposta inclui análise de sentimento por frase e pontuações de confiança.

Ver código de exemplo em Python usando SDK: [Sentiment-Analysis](./Sentiment-Analysis/)

## Key Phrase Extration (Extração de frase-chave)

A extração de frase-chave identifica os principais pontos do texto de entrada. Por exemplo, para o texto de entrada “*A comida estava deliciosa e havia uma equipe maravilhosa*”, a API retorna: “*comida*” e “*equipe maravilhosa*”.

Ver código de exemplo em Python usando SDK: [Key-Phrase-Extraction](./Key-Phrase-Extraction/)

---
Bons estudos! - ***André Carlucci***
