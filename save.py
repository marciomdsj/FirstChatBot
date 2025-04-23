import csv
import os

def salvar_avaliacao(nome_arquivo, relatorio, criterios, pontuacoes):
    """
    Salva uma avaliação de relatório em formato CSV.

    :param nome_arquivo: nome do arquivo CSV a ser salvo
    :param relatorio: o texto do relatório avaliado
    :param criterios: lista com os critérios de avaliação
    :param pontuacoes: lista com as pontuações atribuídas a cada critério
    """
    if not os.path.exists(nome_arquivo):
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Relatório'] + criterios)
            writer.writerow([relatorio] + pontuacoes)
    else:
        with open(nome_arquivo, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([relatorio] + pontuacoes)
