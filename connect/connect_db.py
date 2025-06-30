import psycopg
from sshtunnel import SSHTunnelForwarder
from config.secrets import Secrets as s

def create_connection():
    # tunnel = SSHTunnelForwarder(
    #     (s.host_ssh, s.port_ssh),
    #     ssh_username=s.user_ssh,
    #     ssh_password=s.senha_ssh,
    #     remote_bind_address=(s.host_pg, s.port_pg)
    # )
    # tunnel.start()

    conn = psycopg.connect(
        host=s.host_pg,
        port=s.port_pg,
        user=s.user_pg,
        password=s.senha_pg,
        dbname=s.db_pg,

    )

    return conn

