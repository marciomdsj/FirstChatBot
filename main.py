import os 
from dotenv import load_dotenv
from prompts.simple_prompt import gerar_relatorio
from prompts.cot_prompt import gerar_relatorio_cot
from prompts.avaliador_generico import avaliar_funcao_geradora  # <-- usa agora o avaliador genérico

load_dotenv()

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

def main():
    print("Escolha o tipo de geração de relatório:")
    print("1 - Simples")
    print("2 - Chain-of-Thought")
    print("3 - Avaliação técnica com rubricas do Simples")
    print("4 - Avaliação técnica com rubricas do Chain-of-Thought")

    opcao = input("Digite o número da opção desejada: ")
    respostas = perguntas_para_dev()

    if opcao == "1":
        relatorio = gerar_relatorio(respostas)
    elif opcao == "2":
        relatorio = gerar_relatorio_cot(respostas)
    elif opcao == "3":
        relatorio = avaliar_funcao_geradora("avaliacoes_simples.csv", gerar_relatorio, respostas)
    elif opcao == "4":
        relatorio = avaliar_funcao_geradora("avaliacoes_cot.csv", gerar_relatorio_cot, respostas)
    else:
        print("Opção inválida. Gerando relatório simples por padrão.")
        relatorio = gerar_relatorio(respostas)

    print("\n--- Relatório Final ---\n")
    print(relatorio)

if __name__ == "__main__":
    main()
