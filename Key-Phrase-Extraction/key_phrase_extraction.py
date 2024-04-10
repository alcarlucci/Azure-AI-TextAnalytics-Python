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
