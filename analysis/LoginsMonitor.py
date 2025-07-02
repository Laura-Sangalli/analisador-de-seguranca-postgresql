import re
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from config.secrets import Secrets as s
from reports.generate_report import criar_arquivo, escreva, mostrar_imagem

def monitorar_logins(log_path, file_path):

    padrao_sucesso = re.compile(r'connection authorized: user=([a-zA-Z0-9_]+)')
    padrao_falha = re.compile(r'FATAL: .*user "?([a-zA-Z0-9_]+)"?')

    dados = []
    escreva ("\n\n## MONITORAMENTO DE LOGINS", file_path)
    with open(log_path, 'r', encoding='utf-8', errors='ignore') as log:
        for linha in log:
            datahora = linha[0:16].strip()

            if 'connection authorized' in linha:
                match = padrao_sucesso.search(linha)
                if match:
                    usuario = match.group(1).strip()
                    dados.append({
                        "usuario": usuario,
                        "situacao": "sucesso",
                        "datahora": datahora
                    })


            elif 'FATAL:' in linha and 'password authentication failed' in linha:
                match = padrao_falha.search(linha)
                if match:
                    usuario = match.group(1).strip()
                    dados.append({
                        "usuario": usuario,
                        "situacao": "falha",
                        "datahora": datahora
                    })
    if not dados:
        escreva("Nenhuma tentativa de login encontrada.", log_path)
        return

    

    df = pd.DataFrame(dados)
    size = len(dados)
    escreva(f'Foram encontradas {size} tentativas de login:', file_path)

    df = df[df["usuario"].str.match(r"^[a-zA-Z0-9_]+$")]

    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x="usuario", hue="situacao", palette="Set2_r")
    plt.title("Tentativas de Login por Usuário")
    plt.xlabel("Usuário")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()


    img_path = f"output/graphics/grafico_logins_{datetime.now().strftime('%Y-%m-%d_%h:%M:%s')}.png"
    plt.savefig(img_path, dpi=300)
    mostrar_imagem(img_path=img_path[7:], caminho=file_path)
    plt.show()
