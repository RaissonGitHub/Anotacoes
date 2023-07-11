# COMANDOS DE TABELAS

## CRIAR TABELAS

```
CREATE TABLE [IF NOT EXISTS] nome_tabela(
	coluna tipo_dados constraints
)
```

\# IF EXISTS é opicional


## MOSTRAR TABELAS

```
SHOW TABLES;
```

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

## INSERIR DADOS NA TABELA

```
INSERT INTO nome_tabela (coluna_1,coluna_2,...)
VALUES (valor1,valor2,...);
```

## MOSTRAR TODOS OS CAMPO DA TABELA

```
SELECT * FROM nome_tabela;
```

## CONSULTA SIMPLES

```
SELECT nome_coluna FROM nome_tabela;
```

## CONSULTAR MULTIPLAS COLUNAS

```
SELECT nome_coluna1, nome_coluna2, nome_coluna3 FROM nome_tabela;
```

## CONSULTAR COM ORDENACAO ASC DESC

\# ASC crescente, DESC decrescente

```
SELECT * FROM nome_tabela
ORDER BY nome_coluna ASC;
```

```
SELECT * FROM nome_tabela
ORDER BY nome_coluna DESC;
```

## CONSULTAR COM ODERNACAO POR COLUNA

```
SELECT nome_coluna FROM nome_tabela ORDER BY nome_coluna;
```

## CONSULTA COM FILTRAGEM (WHERE)

Simples:

```
SELECT nome_coluna FROM nome_tabela WHERE nome_coluna = valor;
```

Com operador AND:

```
SELECT nome_coluna FROM nome_tabela WHERE nome_coluna > valor AND nome_coluna < valor;
```

Com operador OR

```
SELECT nome_coluna FROM nome_tabela WHERE nome_coluna > valor OR nome_coluna < valor; 
```

Com operador AND e NOT:

```
SELECT nome_coluna FROM nome_tabela WHERE nome_coluna > valor AND NOT nome_coluna < valor;
```

## VERIFICAR O VALOR ATUAL DO AUTO_INCREMENT

```
SELECT MAX(nome_coluna) FROM nome_tabela;
```
