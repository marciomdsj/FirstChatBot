import os
from dotenv import load_dotenv
from prompts.cot_prompt import gerar_relatorio

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

def perguntas_para_dev():
    respostas = {}
    perguntas = [
        "O que você fez hoje?",
        "Encontrou algum desafio?",
        "Quais tarefas foram concluídas?",
        "Como as tarefas foram concluídas?",
        "Qual linguagem foi utilizada?"
    ]
    print("Responda as perguntas para gerar o relatório:\n")
    for pergunta in perguntas:
        resposta = input(pergunta + "\n ")
        respostas[pergunta] = resposta
    return respostas

if __name__ == "__main__":
    respostas = perguntas_para_dev()
    texto_relatorio = gerar_relatorio(respostas)
    print("\n--- Relatório Gerado ---\n")
    print(texto_relatorio)