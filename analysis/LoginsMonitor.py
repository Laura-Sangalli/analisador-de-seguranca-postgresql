import psycopg
import re
from datetime import datetime
from config.secrets import Secrets as s 
from reports.generate_report import criar_arquivo, escreva, mostrar_imagem

def buscar_audit(log_path, desde_dias=10):
    print(f"\n[AUDITOR] Lendo logs desde os últimos {desde_dias} dias...\n")
    
    padrao_audit = re.compile(r'.*AUDIT:.*(ROLE).*statement:\s(.*)', re.IGNORECASE)

    agora = datetime.now()
    comandos = []

    with open(log_path, 'r', encoding='utf-8') as log:
        for linha in log:
            if 'AUDIT:' in linha:
                resultado = padrao_audit.search(linha)
                if resultado:
                    tipo, sql = resultado.groups()
                    comandos.append((tipo.upper(), sql.strip()))

    if comandos:
        print("[+] Comandos auditados encontrados:\n")
        for tipo, sql in comandos:
            print(f"[{tipo}] → {sql}")
    else:
        print("[!] Nenhuma linha AUDIT encontrada no período.")

def insertMonitor(log_path):
    pass

def deleteMonitor(log_path):
    pass


