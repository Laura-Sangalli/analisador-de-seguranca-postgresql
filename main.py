# analizador de segurança para banco de dados

import psycopg
from sshtunnel import SSHTunnelForwarder
from config.secrets import Secrets as s

## Conexão com o banco PostgreSQL e obtenção das informações de segurança. 

with SSHTunnelForwarder(
            (s.host_ssh, s.port_ssh),
            ssh_username= s.user_ssh,
            ssh_password= s.senha_ssh,
            remote_bind_address=(s.host_pg, s.port_pg)
        ) as tunnel:
            conn = psycopg.connect(
                host='127.0.0.1',  
                port=tunnel.local_bind_port,  
                user=s.user_pg,
                password=s.senha_pg,
                dbname=s.db_pg,
            )

            cur = conn.cursor()

            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            print(f"PostgreSQL versão: {db_version}")

            # Fechar o cursor e a conexão
            cur.close()
            conn.close()