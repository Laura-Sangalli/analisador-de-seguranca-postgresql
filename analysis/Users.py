import psycopg
from tabulate import tabulate
from sshtunnel import SSHTunnelForwarder
from config.secrets import Secrets as s
class Users:
     def __init__(self):
          pass
     
     def ListUsers(self, conn): 
          cur = conn.cursor()
          ("\n\n[!] USUÁRIOS ENCONTRADOS:")

          try:
               cur.execute(
                   """SELECT rolname FROM pg_roles;"""
               )
               obj_names = cur.fetchall()
               names = [row[0] for row in obj_names]

          except Exception as e:
               print(f'Não foi possível identificar nenhum usuário: Erro {e}')
          
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
                    print("\n\n[!] SUPERUSUÁRIOS ENCONTRADOS:")
                    print(tabulate(superusers, headers=["Role", "Superuser", "Create Role", "Create DB", "Can Login"]))
               else:
                    print("\n[+] Nenhum superusuário além do padrão foi encontrado.")
          except Exception as e:
               print(f"Erro ao escanear tabela de usuários: {e}")

          cur.close()
          conn.close()
          return names

     def PasswordsSecurity(self, users):
          passwords = ['123', 'admin', 'postgres', 'senha123', '1234', 'adminadmin', '', ' ', 'senha']
          count = 0
          print('\n\n[!]USUÁRIOS UTILIZANDO SENHA PADRÃO: ')
          for user in users:
               for pwd in passwords:
                    try:
                         conn = psycopg.connect(
                              dbname=s.db_pg,
                              user=user,
                              password=pwd,
                              host=s.host_pg
                         )
                         print(f"\n[!] Usuário '{user}' AUTENTICADO com senha '{pwd}'")
                         conn.close()
                         count += 1
                    except Exception:
                         pass
          if count == 0:
               print('\nNenhum usuário possui senha padrão!')


