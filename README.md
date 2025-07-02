# Analisador de Segurança de Banco de Dados PostgreSQL

O PostgreSQL é um Sistema de Gerenciamento de Bancos de Dados open source, seguro e com desempenho bastante robusto. É muito utilizado por empresas e organizações de todo o mundo devido a sua confiabilidade.

Entretanto, mesmo com seu histórico positivo, é fundamental manter o banco sempre protegido com boas práticas de usuário ou administrador, mantendo senhas seguras, restrições de acesso e dados protegidos. 

Este trabalho tem como objetivo construir um analisador de segurança para bancos de dados PostgreSQL, que emita relatórios com informações cruciais sobre áreas do SGDB passíveis de ataques, destacando pontos a serem melhorados em questão de segurança.


### Este analisador realiza suas atividades subdivididas em quatro etapas, sendo elas:

## 1. Verificação da situação dos usuários e administradores do banco de dados

Nessa etapa, é emitido um parecer sobre quantos usuários existem no banco de dados analisado, bem como quais deles possuem permissões de admnistrador. Além disso, é efetuado um "ataque de dicionário" com senhas padrões, para verificar se algum usuário está utilizando uma senha simples. 

## 2. Análise da integridade dos schemas
São aqui listados todos os schemas presentes no banco de dados. Além disso, é verificado quais usuários possuem permissões criticas no banco (como criação e deleção de tabelas). 

## 3. Monitoramento das atividade de logins (com ou sem sucesso)

Nessa etapa, são contabilizadas todas as tentativas de login de cada usuário, divididas entre sucesso e fracasso. Essas informações são exibidas em um gráfico.

## 4. Verificação de atividade de inserções e deleções

Etapa na qual são exibidos gráficos contendo a quantidade de inserções e deleções que ocorreram no banco de dados a cada hora. 