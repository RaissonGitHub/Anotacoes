# TABELA VIRTUAL VIEWS

## USO DE VIEWS:

* Simplificar o acesso a dados especificados em multiplas tabelas relacionadas (nao precisar colocar toda vez algum inner join na consulta);

* Implementar segurança nos dados de uma tabela, por exemplo criando uma visão que limite os dados que podem ser acessados, por meio de uma cláusula WHERE;

* Prover isolamento de uma aplicação da estrutura específica de tabelas do banco acessado;

---

## CRIAR UMA VIEW

`
CREATE VIEW nome_visao
AS SELECT nome_coluna
FROM nome_tabela
WHERE condicao;
`

ex:

`
CREATE VIEW vw_LivrosAutores
AS SELECT tbl_Livro.Nome_Livro AS Livro, tbl_autores.Nome_Autor AS Autor
FROM tbl_Livro
INNER JOIN tbl_autores
ON tbl_Livro.ID_Autor = tbl_autores.ID_Autor;
`

---

## USAR A VIEW

ex:

`
SELECT Livro, Autor
FROM vw_LivrosAutores
ORDER BY Autor;
`

---

## ALTERAR UMA VIEW

`
ALTER VIEW AS especificacoes;
`

ex:

`
ALTER  VIEW vw_LivrosAutores AS
SELECT tbl_Livro.Nome_Livro AS Livro, tbl_autores.Nome_Autor 
AS Autor, Preco_Livro AS Valor
FROM tbl_Livro
INNER JOIN tbl_autores
ON tbl_Livro.ID_Autor = tbl_autores.ID_Autor;
`

---

## CONSULTAR VIEWS

`
SHOW FULL TABLES IN nome_banco
WHERE TABLE_TYPE LIKE 'VIEW';
`

ex:

`
SHOW FULL TABLES IN db_MeusLivros
WHERE TABLE_TYPE LIKE 'VIEW';
`

\# Caso o a consulta seja referente ao banco de dados atual

`
SHOW FULL TABLES
WHERE TABLE_TYPE LIKE 'VIEW';
`

---

## VER TODOS AS VIEWS NO SCHEMA

`
SELECT TABLE_SCHEMA, TABLE_NAME
FROM information_schema.TABLES
WHERE TABLE_TYPE LIKE 'VIEW';
`

---

## DELETAR UMA VIEW

`
DROP VIEW vw_LivrosAutores;
`

