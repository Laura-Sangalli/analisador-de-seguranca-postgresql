import psycopg
import pandas as pd
from sshtunnel import SSHTunnelForwarder
from config.secrets import Secrets as s
from tabulate import tabulate
from reports.generate_report import escreva
class Users:
     def __init__(self, arquivo):
          self.arquivo = arquivo
          print(self.arquivo)


     def ListUsers(self, conn): 
          cur = conn.cursor()
          escreva("\n\n ## USUÁRIOS ENCONTRADOS:", self.arquivo)
          try:
               cur.execute(
                   """SELECT rolname FROM pg_roles;"""
               )
               obj_names = cur.fetchall()
               names = [row[0] for row in obj_names]

               for name in names:
                    escreva(f'- {name}', self.arquivo)

          except Exception as e:
               escreva(f'Não foi possível identificar nenhum usuário: Erro {e}', self.arquivo)
          return names
          
     
     def ScanSuperusers(self, conn):
        names = []
        with conn.cursor() as cur:
          try:
               cur.execute(
                    """SELECT rolname, rolsuper, rolcreaterole, rolcreatedb, 
                    rolcanlogin FROM pg_roles WHERE rolsuper = True;"""
               )
               superusers = cur.fetchall()
               if superusers:
                    escreva("\n\n ## SUPERUSUÁRIOS ENCONTRADOS:", self.arquivo)
                    tabela = tabela_md = tabulate(
                    superusers,
                    headers=["Role", "Superuser", "Create Role", "Create DB", "Can Login"],
                    tablefmt="pipe"  # ou "pipe"
                    )

                    escreva(tabela, self.arquivo)
               else:
                    escreva("\n[+] Nenhum superusuário além do padrão foi encontrado.", self.arquivo)
          except Exception as e:
               escreva(f"Erro ao escanear tabela de usuários: {e}", self.arquivo)

          cur.close()



     def PasswordsSecurity(self, users):
          passwords = ['123', 'admin', 'postgres', 'senha123', '1234', 'adminadmin', '', ' ', 'senha']
          count = 0
          escreva('\n\n ## USUÁRIOS UTILIZANDO SENHA PADRÃO: ', self.arquivo)
          for user in users:
               for pwd in passwords:
                    try:
                         conn = psycopg.connect(
                              dbname=s.db_pg,
                              user=user,
                              password=pwd,
                              host=s.host_pg
                         )
                         escreva(f"- **Usuário '{user}' AUTENTICADO com senha '{pwd}'**", self.arquivo)
                         conn.close()
                         count += 1
                    except Exception:
                         pass
          
     
          if count == 0:
               escreva('\nNenhum usuário possui senha padrão!', self.arquivo)
          return 

