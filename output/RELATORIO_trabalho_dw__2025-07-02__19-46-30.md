# RELATÓRIO ANÁLISE DE SEGURANÇA trabalho_dw (POSTGRESQL)


BANCO DE DADOS ANALISADO: **TRABALHO_DW**


 ## USUÁRIOS ENCONTRADOS:
- pg_database_owner
- pg_read_all_data
- pg_write_all_data
- pg_monitor
- pg_read_all_settings
- pg_read_all_stats
- pg_stat_scan_tables
- pg_read_server_files
- pg_write_server_files
- pg_execute_server_program
- pg_signal_backend
- pg_checkpoint
- pg_use_reserved_connections
- pg_create_subscription
- laura
- administrador
- postgres
- usuario


 ## SUPERUSUÁRIOS ENCONTRADOS:
| Role          | Superuser   | Create Role   | Create DB   | Can Login   |
|:--------------|:------------|:--------------|:------------|:------------|
| laura         | True        | True          | True        | True        |
| administrador | True        | False         | False       | True        |
| postgres      | True        | True          | True        | True        |


 ## USUÁRIOS UTILIZANDO SENHA PADRÃO: 
- **Usuário 'usuario' AUTENTICADO com senha 'admin'**


 ## SCHEMAS ENCONTRADOS:
- pg_toast     
- pg_catalog     
- public     
- information_schema     


 ## SCHEMAS COM PERMISSÕES DE CRIAÇÃO/DELEÇÃO DE TABELAS:
- pg_catalog     
- public     
- information_schema     

 ## MONITORAMENTO DE INSERÇÕES
Foram encontradas 24 inserções:


 ![Gráfico](graphics/grafico_inserts_2025-07-02_Jul:46:1751496395.png)
 ## MONITORAMENTO DE DELEÇÕES
Foram encontradas 2 deleções:


 ![Gráfico](graphics/grafico_deletes_2025-07-02_Jul:46:1751496397.png)

## MONITORAMENTO DE LOGINS
Foram encontradas 41776 tentativas de login:


 ![Gráfico](graphics/grafico_logins_2025-07-02_Jul:46:1751496399.png)