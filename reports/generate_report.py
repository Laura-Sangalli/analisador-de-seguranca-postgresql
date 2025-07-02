import datetime
from config.secrets import Secrets as s
import datetime

caminho_arquivo = ''
def criar_arquivo(): 

    agora = datetime.datetime.now()

    caminho_arquivo = f"output/RELATORIO_{s.db_pg}__{agora.strftime('%Y-%m-%d__%H-%M-%S')}.md"
    
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"# RELATÓRIO ANÁLISE DE SEGURANÇA {s.db_pg} (POSTGRESQL)\n")
    
    return caminho_arquivo


def ler_arquivo(caminho):
    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            pass
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")


def escreva(texto, caminho):
    with open(caminho, 'a', encoding='utf-8') as arquivo:
        arquivo.write(texto + '\n')

def mostrar_imagem(img_path, caminho):
    with open(caminho, 'a', encoding='utf-8') as arquivo:
        arquivo.write('\n\n ![Gráfico INSERT](' + img_path + ')')