import psycopg
from reports.generate_report import criar_arquivo, escreva

class Schemas:
    def __init__(self, arquivo):
        self.arquivo = arquivo


    def verificarPermissaoAcesso(self, conn):
        cur = conn.cursor()

        try: 
            cur.execute("""
            SELECT nspname FROM pg_namespace;
            """)
            schemas = cur.fetchall()

            cur.execute(
                """
                SELECT nspname, nspacl
                FROM pg_namespace
                WHERE nspacl::text ~* '=[A-Z]*C';
                """
            )
            permissions = cur.fetchall()
            
            escreva('\n\n ## SCHEMAS ENCONTRADOS:', self.arquivo)
            string = ''
            count = 0

            for i in schemas:
                string += '- ' + str(i[0]) + '     '
                escreva(string, self.arquivo)
                string = ''

            escreva('\n\n ## PERMISSÕES DE CRIAÇÃO NO SCHEMA ENCONTRADAS:', self.arquivo)
            for i in permissions:
                string += '- ' + str(i[0]) + '     '
                escreva(string, self.arquivo)
                string = ''


        except Exception as e:
            escreva(f'Não foi possível verificar permissões {permissions}: {e}', self.arquivo)
