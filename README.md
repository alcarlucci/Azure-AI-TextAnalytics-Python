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

Ver código de exemplo em Python usando SDK: [Sentiment-Analysis](./Sentiment-Analysis/sentiment_analysis.py)

```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# pega as Credenciais do recurso Text Analytics no Azure
credential = AzureKeyCredential("3269************************71cb")
endpoint = "https://eastus.api.cognitive.microsoft.com/"

# client do TextAnalytics
textAnalyticsClient = TextAnalyticsClient(endpoint, credential)

# frases (sentenças) para serem analisadas
documents = [
    "Não gostei do restaurante. A comida era de alguma forma muito picante e pouco temperada. Além disso, achei que o local era muito longe do teatro.",
    "O restaurante foi lindamente decorado. A atmosfera era diferente de qualquer outro restaurante que já estive.",
    ":)",
    ":(",
    "O Restaurante não era nem bom nem ruim."
    "A comida era gostosa."
]

# pega o retorno da Análise de Sentimentos guardando apenas os resultados que não retornaram erros
response = textAnalyticsClient.analyze_sentiment(documents, language="pt")
result = [doc for doc in response if not doc.is_error]

# apresenta o Resultado da Análise de Sentimentos realizada pelo "Azure Text Analytics"
print("Análise de Sentimento - Resultados obtidos:\n")
i = 0
for doc in result:
    print("Sentença analisada: \"{}\"".format(documents[i]))
    print("Sentimento geral: {}".format(doc.sentiment))
    print("Scores: positivo={}; neutro={}; negativo={} \n".format(
        doc.confidence_scores.positive,
        doc.confidence_scores.neutral,
        doc.confidence_scores.negative
    ))
    i += 1
```

## Key Phrase Extration (Extração de frase-chave)

A extração de frase-chave identifica os principais pontos do texto de entrada. Por exemplo, para o texto de entrada “*A comida estava deliciosa e havia uma equipe maravilhosa*”, a API retorna: “*comida*” e “*equipe maravilhosa*”.

Ver código de exemplo em Python usando SDK: [Key-Phrase-Extraction](./Key-Phrase-Extraction/key_phrase_extraction.py)

```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# pega as Credenciais do recurso Text Analytics no Azure
credential = AzureKeyCredential("3269************************71cb")
endpoint = "https://eastus.api.cognitive.microsoft.com/"

# client do TextAnalytics
textAnalyticsClient = TextAnalyticsClient(endpoint, credential)

# frases (sentenças) para serem analisadas
documents = [
    "Não gostei do restaurante. A comida era de alguma forma muito picante e pouco temperada. Além disso, achei que o local era muito longe do teatro.",
    "O restaurante foi lindamente decorado. A atmosfera era diferente de qualquer outro restaurante que já estive.",
    "A comida era gostosa."
]

# pega o retorno da Análise guardando apenas os resultados que não retornaram erros
response = textAnalyticsClient.extract_key_phrases(documents, language="pt")
result = [doc for doc in response if not doc.is_error]

# apresenta o Resultado da Análise realizada pelo "Azure Text Analytics"
print("Extração de Frase-Chave - Resultados obtidos:\n")
for doc in result:
    print(doc.key_phrases)
```

---
Bons estudos! - ***André Carlucci***
