import requests

def gerar_relatorio_cot(respostas: dict) -> str:
    texto_base = "\n".join([f"{k}: {v}" for k, v in respostas.items()])
    
    # Define a delimiter
    delimiter = "####"
    
    # Create a structured system prompt with clear steps
    system_prompt = f"""
    Siga estas etapas para gerar um relatório técnico baseado nas respostas do desenvolvedor.
    As respostas serão delimitadas com quatro hashtags, ou seja, {delimiter}.

    Etapa 1:{delimiter} Identifique os principais pontos técnicos nas respostas do desenvolvedor.
    
    Etapa 2:{delimiter} Avalie a coerência técnica das informações fornecidas.
    
    Etapa 3:{delimiter} Organize as informações em uma estrutura lógica, conectando os diferentes pontos técnicos.
    
    Etapa 4:{delimiter} Redija um texto claro e técnico que incorpore e demonstre todos os pontos relevantes.
    Evite usar algo como "O desenvolvedor utilizou", opte por frases como: "Foi-se utilizado" para tornar o texto impessoal.
    Não invente informações ou números que não estejam no texto de entrada.
    Use linguagem contínua e sem tópicos.
    
    Use o seguinte formato:
    Etapa 1:{delimiter} <raciocínio da etapa 1>
    Etapa 2:{delimiter} <raciocínio da etapa 2>
    Etapa 3:{delimiter} <raciocínio da etapa 3>
    Etapa 4:{delimiter} <raciocínio da etapa 4>
    Ao final, inclua um parágrafo sob o título "Relatório Técnico Final:", e use **esse parágrafo como resposta final da API.**
    Relatório final:{delimiter} <relatório técnico em formato de texto>
    
    Certifique-se de incluir {delimiter} para separar cada etapa.
    """
    
    mensagens = [
        {
            "role": "system",
            "content": system_prompt
        },
        {"role": "user", "content": f"""
Você é um assistente que gera relatórios técnicos de atividades de desenvolvedores. 
Com base nas informações abaixo, **gere apenas o relatório final, em parágrafo único, com linguagem impessoal e contínua, pronto para ser usado como relatório técnico**. 
Não explique como chegou nele, apenas escreva o relatório final, claro, técnico e direto:

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
        
        # Extract just the final report from the chain of thought response
        conteudo_completo = resposta.json()["message"]["content"].strip()
        
        # Find the last occurrence of the delimiter + "Relatório final:"
        marcador_relatorio = f"Relatório final:{delimiter}"
        if marcador_relatorio in conteudo_completo:
            indice_relatorio = conteudo_completo.find(marcador_relatorio) + len(marcador_relatorio)
            relatorio_final = conteudo_completo[indice_relatorio:].strip()
            return relatorio_final
        else:
            # If the model didn't follow the format, return the whole response
            return conteudo_completo
            
    except Exception as e:
        print("Erro ao gerar o relatório:", e)
        return "Erro ao gerar relatório."