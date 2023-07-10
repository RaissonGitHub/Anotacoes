# INDICES

* Indices sao usados para otimisar consultas do banco;

* Crie indices em colunas muito acessadas;

* Dispense seu uso em colunas que sao frequentemente atualizadas;

---

## CRIAR INDICES 

```sql
CREATE [UNIQUE] INDEX nome_indice on nome_tabela(
coluna1 [ASC|DESC],
coluna2 [ASC|DESC]..
);
```

---

## ADICIONAR INDICES

`
ALTER TABLE nome_tabela ADD INDEX nome_indice (nome_coluna);
`

---

## DELETAR INDICES

`
DROP INDEX nome_indice ON nome_tabela;
`

---

## VISUALISAR INDICES

`
SHOW INDEX FROM nome_tabela;
`

