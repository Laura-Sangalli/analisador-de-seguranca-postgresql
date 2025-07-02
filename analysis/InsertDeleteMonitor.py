import re
from datetime import datetime
from config.secrets import Secrets as s 
import seaborn as sns
import matplotlib.pyplot as plt
from reports.generate_report import criar_arquivo, escreva, mostrar_imagem

def insertMonitor(log_path, file_path):
    lista = []

    escreva("\n ## MONITORAMENTO DE INSERÇÕES", file_path)
    with open(log_path, 'r', encoding='utf-8') as log:
        for linha in log:
            linha = linha.strip()
            if 'AUDIT:' in linha and 'INSERT INTO' in linha.upper():
                lista.append(f'{linha[0:13]}h')
    
    escreva(f'Foram encontradas {len(lista)} inserções:', file_path)

    sns.countplot(x=lista)
    plt.title('INSERÇÕES POR HORA')
    img_path =  f"output/graphics/grafico_inserts_{datetime.now().strftime('%Y-%m-%d_%h:%M:%s')}.png"
    plt.savefig(img_path, dpi=300, bbox_inches='tight')  
    mostrar_imagem(img_path=img_path[7:], caminho=file_path)
    plt.show()



def deleteMonitor(log_path, file_path):
    lista = []

    escreva("\n ## MONITORAMENTO DE DELEÇÕES", file_path)
    with open(log_path, 'r', encoding='utf-8') as log:
        for linha in log:
            linha = linha.strip()
            if 'AUDIT:' in linha and 'DELETE FROM' in linha.upper():
                lista.append(f'{linha[0:13]}h')

    escreva(f'Foram encontradas {len(lista)} deleções:', file_path)

    sns.countplot(x=lista)
    plt.title('DELEÇÕES POR HORA')
    img_path =  f"output/graphics/grafico_deletes_{datetime.now().strftime('%Y-%m-%d_%h:%M:%s')}.png"
    plt.savefig(img_path, dpi=300, bbox_inches='tight') 
    mostrar_imagem(img_path=img_path[7:], caminho=file_path)
    plt.show()