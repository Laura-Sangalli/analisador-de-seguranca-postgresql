# analizador de segurança para banco de dados

import psycopg
from sshtunnel import SSHTunnelForwarder
from config.secrets import Secrets as s
from analysis import *
from tabulate import tabulate
from analysis.Users import Users
from connect.connect_db import create_connection

## Conexão com o banco PostgreSQL e obtenção das informações de segurança. 

conn = create_connection()
users = Users()
try:
    count=0
    usuarios = users.ListUsers(conn=conn)
    for i in usuarios:
        print(f'{i}\t', end='')
        count += 1
        count = count % 5
        if count == 0:
            print('\n')

    superusers = users.ScanSuperusers(conn)


    users.PasswordsSecurity(usuarios)
except:
    print('Erro ao conectar ao banco de dados')

conn.close()
# tunnel.close()
