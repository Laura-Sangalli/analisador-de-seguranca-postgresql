import psycopg
from sshtunnel import SSHTunnelForwarder
from config.secrets import Secrets as s

from tabulate import tabulate
from analysis.Schemas import Schemas
from analysis.Users import Users
from connect.connect_db import create_connection
from reports.generate_report import criar_arquivo, escreva
from analysis.InsertDeleteMonitor import *
from analysis.LoginsMonitor import monitorar_logins

try:
    conn = create_connection()
except Exception:
    print(1)

arquivo = criar_arquivo()
escreva(f'\n\nBANCO DE DADOS ANALISADO: **{s.db_pg.upper()}**', arquivo)

users = Users(arquivo)
x = Schemas(arquivo)
try:
    count=0

    try:
        usuarios = users.ListUsers(conn=conn)
        superusers = users.ScanSuperusers(conn)
    except Exception:
        print(2)


    users.PasswordsSecurity(usuarios)

    print('\n')
    conn.close()
    conn = create_connection()

    x.verificarPermissaoAcesso(conn)

    insertMonitor(s.log_path, file_path=arquivo)
    deleteMonitor(s.log_path, arquivo)

    monitorar_logins(s.log_path, arquivo)
except:
    print('Erro ao conectar ao banco de dados')




conn.close()

