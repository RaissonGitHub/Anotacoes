# COMANDOS SELECT

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


\#ASC crescente, DESC decrescente

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
