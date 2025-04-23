import requests

def gerar_relatorio(respostas: dict) -> str:
    texto_base = "\n".join([f"{k}: {v}" for k, v in respostas.items()])

    mensagens = [
    {"role": "system", "content": "Você é um gerador de relatórios técnicos e deve seguir as instruções do usuário com precisão."},
    {"role": "user", "content": f"""
Gere um relatório técnico com base nas informações abaixo. Escreva **estritamente em um único parágrafo**, sem quebras de linha, sem títulos, subtítulos ou separações. Use linguagem contínua, formal e impessoal. Integre todos os pontos de forma coesa e lógica, sem usar marcadores ou tópicos.

Texto base:
{texto_base}
"""}
]


    payload = {
        "model": "llama3:8b",
        "messages": mensagens,
        "stream": False
    }

    try:
        resposta = requests.post("http://localhost:11434/api/chat", json=payload)
        resposta.raise_for_status()
        print("Resposta completa:", resposta.json())
        return resposta.json()["message"]["content"]
    except Exception as e:
        print("Erro ao gerar o relatório:", e)
        return "Erro ao gerar relatório."