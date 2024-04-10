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
