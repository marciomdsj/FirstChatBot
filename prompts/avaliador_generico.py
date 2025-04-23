import requests
import json
from save import salvar_avaliacao

def avaliar_funcao_geradora(nome_arquivo_csv: str, funcao_geradora, respostas: dict) -> str:
    """
    Avalia a saída de uma função geradora de relatório técnico usando IA.

    :param nome_arquivo_csv: nome do arquivo CSV para salvar a avaliação
    :param funcao_geradora: função a ser avaliada (ex: gerar_relatorio, gerar_relatorio_cot)
    :param respostas: dicionário com as respostas do desenvolvedor
    :return: texto do relatório avaliado
    """
    try:
        relatorio_gerado = funcao_geradora(respostas)

        mensagens = [
            {"role": "system", "content": "Você é um avaliador técnico."},
            {"role": "user", "content": f"""
Avalie tecnicamente o relatório abaixo com base nos seguintes critérios, atribuindo uma nota de 1 a 5:

Relatório:
\"\"\"{relatorio_gerado}\"\"\"

Critérios:
- Clareza
- Profundidade Técnica
- Justificativa Técnica
- Coerência

Responda ESTRITAMENTE no seguinte formato JSON:

{{
  "avaliacao": {{
    "Clareza": <nota>,
    "Profundidade Técnica": <nota>,
    "Justificativa Técnica": <nota>,
    "Coerência": <nota>
  }},
  "relatorio": "<mesmo texto do relatório acima ou levemente reformulado com análise crítica>"
}}
"""}
        ]

        payload = {
            "model": "llama3:8b",
            "messages": mensagens,
            "stream": False
        }

        resposta = requests.post("http://localhost:11434/api/chat", json=payload)
        resposta.raise_for_status()
        texto = resposta.json()["message"]["content"]

        # Tentar limpar e carregar JSON mesmo que venha com crases ou texto extra
        texto = texto.strip("`\n ")
        try:
            resultado_json = json.loads(texto)
        except json.JSONDecodeError:
            print("⚠️ Erro: resposta da IA não está em JSON válido.")
            return "Erro ao avaliar: resposta inválida."

        avaliacao = resultado_json["avaliacao"]
        relatorio_avaliado = resultado_json["relatorio"]

        criterios = list(avaliacao.keys())
        pontuacoes = list(avaliacao.values())

        salvar_avaliacao(nome_arquivo_csv, relatorio_avaliado, criterios, pontuacoes)

        return relatorio_avaliado

    except Exception as e:
        print("Erro durante a avaliação:", e)
        return "Erro durante a avaliação."
