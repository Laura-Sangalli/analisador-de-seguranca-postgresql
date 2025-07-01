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
                string += str(i[0]) + '     '
                count += 1

                if count % 5 == 0:
                    escreva(string, self.arquivo)
                    string = ''

            # escreve o que sobrou no final, se necessário
            if string:
                escreva(string, self.arquivo)

            escreva('\n\n ## Permissões ENCONTRADOS:', self.arquivo)
            for i in permissions:
                string += i[0]
                string += '     '
                count += 1
                count = count % 5
                if count == 0:
                    escreva(string, self.arquivo)
                    string = ''


        except Exception as e:
            escreva(f'Não foi possível verificar permissões {permissions} do squema {schema}: {e}', self.arquivo)
