# RELATÓRIO ANÁLISE DE SEGURANÇA trabalho_dw (POSTGRESQL)


 ## USUÁRIOS ENCONTRADOS:


 ## SUPERUSUÁRIOS ENCONTRADOS:
Role           Superuser    Create Role    Create DB    Can Login
-------------  -----------  -------------  -----------  -----------
laura          True         True           True         True
administrador  True         False          False        True
postgres       True         True           True         True


 ## USUÁRIOS UTILIZANDO SENHA PADRÃO: 
- Usuário 'postgres' AUTENTICADO com senha 'senha'


 ## SCHEMAS ENCONTRADOS:
- pg_toast     
- pg_catalog     
- public     
- information_schema     


 ## PERMISSÕES DE CRIAÇÃO NO SCHEMA ENCONTRADAS:
- pg_catalog     
- public     
- information_schema     

 ## MONITORAMENTO DE INSERÇÕES
2025-07-02 13:54:28.515 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,1,1,WRITE,INSERT,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:28.516 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,2,1,WRITE,DELETE,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:29.605 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,3,1,WRITE,INSERT,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:29.605 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,4,1,WRITE,DELETE,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:29.927 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,5,1,WRITE,INSERT,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:29.927 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,6,1,WRITE,DELETE,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:30.127 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,7,1,WRITE,INSERT,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:30.127 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,8,1,WRITE,DELETE,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:30.276 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,9,1,WRITE,INSERT,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:30.276 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,10,1,WRITE,DELETE,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:30.429 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,11,1,WRITE,INSERT,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:30.429 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,12,1,WRITE,DELETE,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:30.584 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,13,1,WRITE,INSERT,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:30.584 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,14,1,WRITE,DELETE,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:30.730 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,15,1,WRITE,INSERT,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:30.730 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,16,1,WRITE,DELETE,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:30.874 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,17,1,WRITE,INSERT,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:54:30.874 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,18,1,WRITE,DELETE,,,"INSERT INTO teste_audit (nome) VALUES ('Laura');
2025-07-02 13:58:50.673 -03 [19076] laura@trabalho_dw LOG:  AUDIT: SESSION,19,1,WRITE,INSERT,,,INSERT INTO teste_audit (nome) VALUES ('Laura');,<not logged>
