# Comandos ALTER TABLE

## ALTERAR TABELAS

```
ALTER TABLE nome_tabela
alteracao;
```

ex: deletar uma coluna de uma tabela

```
ALTER TABLE nome_tabela
DROP COLUMN nome_coluna;
```


ex: adicionar uma coluna em uma tabela

```
ALTER TABLE nome_tabela
add column nome_coluna tipo constraints;
```


ex: adicionar uma foreign key

```
ALTER TABLE nome_tabela
ADD CONSTRAINT nome_para_constraint
FOREIGN KEY (nome_coluna)
REFERENCES nome_tabela_referencia nome_coluna_referencia;
```


ex: alterar o tipo de uma coluna

```
ALTER TABLE nome_tabela
ALTER COLUMN nome_coluna tipo;
```


ex: adicionar primary key em uma tabela existente


```
ALTER TABLE nome_tabela
ADD PRIMARY KEY (campo);
```


ex: excluir uma primary key

```
ALTER TABLE nome_tabela
DROP PRIMARY KEY;
```

ex: auterar o valor do auto_increment


```
ALTER TABLE nome_tabela AUTO_INCREMENT = valor;
```
