# Backup e restauração de bancos de dados com mysqldump

## TERMINAL LINUX

### CRIANDO O ARQUIVO DE BACKUP

```
mysqldump -u root -p nome_banco > arquivo_backup.sql
```

ex:

```
mysqldump -u root -p db_Biblioteca > /home/fabio/db_Biblioteca.sql
```


### RESTAURAR BANCO DE DADOS


```
mysql -u root -p banco_criado < backup.sql
```


ex:
 
\#crie um banco de dados novo chamado teste-restore

```
mysql -u root -p teste-restore < /home/fabio/db_Biblioteca.sql
```
