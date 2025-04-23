# FirstChatBot

Este projeto é um chatbot simples criado para gerar relatórios técnicos a partir de respostas de desenvolvedores. A ideia é testar como diferentes formatos de prompts afetam a qualidade e o estilo das respostas geradas por um modelo de linguagem (neste caso, LLaMA3 rodando localmente via Ollama).

## Objetivo

Explorar como variações no prompt influenciam a saída do modelo. Foram utilizados três tipos de prompts:

- **Simples**: geração direta do relatório.
- **Chain-of-Thought (CoT)**: o modelo é instruído a refletir passo a passo antes de gerar a resposta final.
- **Valoration**: o modelo é instruído a avaliar coerência, organização e clareza técnica antes de gerar o relatório.

## Como Rodar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure o `.env`:
Crie um arquivo `.env` com sua chave da OpenAI **(caso for usar o modo cloud)**, ou apenas mantenha o modelo rodando localmente com:
```bash
ollama run llama3:8b
```

3. Execute o chatbot:
```bash
python main.py
```

4. Para testar diferentes tipos de prompts, altere o import no `main.py`:
```python
from prompts.cot_prompt import gerar_relatorio
# ou
from prompts.valoration_prompt import gerar_relatorio
# ou
from prompts.simples import gerar_relatorio
```

## Estrutura do Projeto

```
FirstChatBot/
├── main.py                   # Fluxo principal
├── prompts/                  # Variações de prompt
│   ├── cot_prompt.py         # Chain-of-Thought
│   ├── avaliador_generico.py # Avaliação
│   └── simples.py            # Geração direta
├── results/                  # Exemplos de saídas
├── arquivos_csv              # Conteúdo das avaliações
├── save.py                   # Utilitária para salvar arquivos csv
├── .env                      # Exemplo de arquivo de ambiente
├── requirements.txt          # Dependências
└── README.md                 # Documentação
```

## Exemplos de Resultados

Veja a pasta `results/` para comparação entre saídas usando prompts diferentes.

## Ideias de Melhorias

- Colocar a padronização dos relatórios da empresa no prompt do avaliador, para que seja testado eficientemente todos os relatórios gerados, com critérios específicos.

## Observações

- O uso de LLaMA3 localmente exige máquina com bom desempenho. A CPU pode atingir 100% durante a geração.
- O tempo de resposta pode ser alto (3 a 8 minutos), especialmente para prompts mais complexos.

---

Este projeto foi desenvolvido como estudo exploratório de prompt engineering em modelos locais.

