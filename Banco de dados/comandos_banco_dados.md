# Anotações de Banco de dados

## Comandos

* CRIAR BANCO DE DADOS

`
CREATE DATABASE [IF NOT EXISTS] nome_db;
`

IF NOT EXISTS é opicional

 

* MOSTRAR BANCOS

`
SHOW DATABASES;
`

### USAR BANCO DE DADOS

`
USE nome_db;
`

### VISUALISAR O BANCO DE DADOS ATUAL

`
SELECT DATABASE();
`

### DELETAR BANCO 

`
DROP DATABASE [IF EXISTS] nome_db;
`

IF EXISTS é opicional

### CRIAR TABELAS

`
CREATE TABLE [IF NOT EXISTS] nome_tabela(
	coluna tipo_dados constraints
)
`

IF EXISTS é opicional

### RENOMEAR TABELAS

`
RENAME TABLE nome_tabela TO nome_tabela_novo;
`

### DELETAR TABELAS

`
DROP TABLE nome_tabela;
`

### CRIAR UMA COLUNA CALCULADA

`
nome_coluna tipo_dados [GENERATE ALWAYS] AS expressao [VIRTUAL|STORED] constraints
`
virtual (calcula os dados na consulta mas nao armazena) padrao
stored (calcula nas insercoes e atualizacoes de dados e armazena na tabela)

ex:
` 
num3 SMALLINT GENERATED ALWAYS AS (num1 * num2) VIRTUAL
`

### MOSTRAR TABELAS

`
SHOW TABLES;
`

### ALTERAR TABELAS

`
ALTER TABLE nome_tabela
alteracao;
`
ex: deletar uma coluna de uma tabela
ALTER TABLE nome_tabela
DROP COLUMN nome_coluna;

ex: adicionar uma coluna em uma tabela
ALTER TABLE nome_tabela
add column nome_coluna tipo constraints;

ex: adicionar uma foreign key
ALTER TABLE nome_tabela
ADD CONSTRAINT nome_para_constraint
FOREIGN KEY (nome_coluna)
REFERENCES nome_tabela_referencia nome_coluna_referencia;

ex: alterar o tipo de uma coluna
ALTER TABLE nome_tabela
ALTER COLUMN nome_coluna tipo;

ex: adicionar primary key em uma tabela existente

ALTER TABLE nome_tabela
ADD PRIMARY KEY (campo);

ex: excluir uma primary key
ALTER TABLE nome_tabela
DROP PRIMARY KEY;

ex: auterar o valor do auto_increment

ALTER TABLE nome_tabela AUTO_INCREMENT = valor;

ex: adicionar um valor padrao a um campo

ALTER TABLE nome_tabela
MODIFY COLUMN nome_coluna tipo_dado
DEFAULT 'valor_padrao';

INSERIR REGISTROS NA TABELA

INSERT INTO nome_tabela (coluna_1,coluna_2,...)
VALUES (valor1,valor2,...);

ATUALIZAR REGISTROS DA TABELA

UPDATE nome_tabela 
SET nome_coluna = novo_valor 
WHERE nome_coluna = valor_filtro;

DELETAR REGISTROS DA TABELA

DELETE FROM nome_tabela 
WHERE nome_coluna = valor;

EXCLUIR TODOS OS REGISTROS DE UMA TABELA

TRUNCATE TABLE nome_tabela;

MOSTRAR TODOS OS CAMPO DA TABELA

SELECT * FROM nome_tabela;

CONSULTA SIMPLES

SELECT nome_coluna 
FROM nome_tabela;

CONSULTAR MULTIPLAS COLUNAS

SELECT nome_coluna1, nome_coluna2, nome_coluna3 
FROM nome_tabela;

CONSULTAR COM ORDENACAO ASC DESC

ASC crescente, DESC decrescente

SELECT * FROM nome_tabela
ORDER BY nome_coluna ASC;

SELECT * FROM nome_tabela
ORDER BY nome_coluna DESC;

CONSULTAR COM ODERNACAO POR COLUNA

SELECT nome_coluna 
FROM nome_tabela 
ORDER BY nome_coluna;

CONSULTA COM FILTRAGEM (WHERE)

simples:

SELECT nome_coluna 
FROM nome_tabela 
WHERE nome_coluna = valor;

com operador AND:

SELECT nome_coluna 
FROM nome_tabela 
WHERE nome_coluna > valor AND nome_coluna < valor;

com operador OR

SELECT nome_coluna 
FROM nome_tabela 
WHERE nome_coluna > valor OR nome_coluna < valor; 

com operador AND e NOT:

SELECT nome_coluna 
FROM nome_tabela 
WHERE nome_coluna > valor AND NOT nome_coluna < valor;

CONSULTA COM OPERADOR IN NOT IN

SELECT coluna(s)
FROM tabela
WHERE expressão | coluna [IN|NOT IN] (valor1, valor2,...);

ex:
SELECT NomeLivro, IdEditora
FROM tbl_livro
WHERE IdEditora IN (2,4);

ex:
SELECT NomeLivro, Edicao
FROM tbl_livro
WHERE Edicao NOT IN (1,2);

VERIFICAR O VALOR ATUAL DO AUTO_INCREMENT

SELECT MAX(nome_coluna) 
FROM nome_tabela;

CONSULTAR COLUNA DO TIPO ENUM EM ORDEM ALFABETICA

SELECT * FROM nome_tabela
ORDER BY CAST(nome_coluna AS CHAR);

CONSULTAR OS VALORES DE UMA COLUNA ENUM

SHOW COLUMNS
FROM nome_tabela
LIKE 'nome_coluna';

GERAR UM VALOR ALEATORIO

com casas decimais
SELECT RAND() * valor_maximo_escolhido;

inteiro
SELECT FLOOR(RAND()*valor_maximo_escolhido);

ex:
SELECT FLOOR(1 + RAND() * 100) AS Numero_Aleatorio;

ex:
SELECT Nome_Livro FROM tbl_Livros ORDER BY RAND() LIMIT 3;

DAR UM NOME DIFERENTE A COLUNA E OU TABELA EM UMA CONSULTA

SELECT nome_coluna AS nome_apelido 
FROM nome_tabela AS nome_apelido2;

ex:
SELECT Nome_livro AS Livro FROM tbl_livro;

ex:
SELECT Nome_livro AS L, Preco_Livro AS P FROM tbl_livro;

CONSULTAR COM FUNCOES DE AGREGACAO [MIN,MAX,AVG,COUNT,SUM]

funcao(ALL|DISTINCT expressao);
ALL todos os registros    padrao
DISTINCT valores distintos sem repeticao

MIN valor minimo
MAX valor maximo
AVG media aritimetica
COUNT contagem da quantidade de itens
SUM soma total dos itens

ex:
SELECT MIN(nome_coluna) FROM nome_tabela;

ex:
SELECT Max(nome_coluna) FROM nome_tabela;

ex:
SELECT AVG(nome_coluna) FROM nome_tabela;

ex:
SELECT COUNT(*) FROM nome_tabela;

ex:
SELECT COUNT(DISTINCT nome_coluna) FROM nome_tabela;

AGRUPAR REGISTROS GROUP BY

SELECT nome_coluna, funcao_agregacao()
FROM nome_tabela 
WHERE filtro
GROUP BY nome_coluna;

ex: Consulta contando o número de registros de vendas por cidade:

SELECT Cidade, COUNT(*) As Total
FROM Vendas
GROUP BY Cidade;

//retorno com GROUP BY
//Cidade  Total
//Recife  3240
//Rj      1700
//Sp      6745

//sem GROUP BY (errado)
//Cidade  Total
//Sp      11685

CONSULTA COM AGRUPAMENTO FILTRADOS HAVING

SELECT nome_coluna, funcao_agregacao()
FROM nome_tabela
WHERE filtro
GROUP BY nome_coluna
HAVING filtro_agrupamento;

ex:Consulta retornando total de vendas do produto ‘Teclado’ das cidades com menos de 1500 teclados vendidos:

SELECT Cidade, SUM(Quantidade) As TotalTeclados
FROM Vendas
WHERE Produto = 'Teclado'
GROUP BY Cidade
HAVING TotalTeclados < 1500;

CONSULTA COM SELECAO DE INTERVALOS BETWEEN

SELECT nome_coluna FROM nome_tabela 
WHERE nome_coluna BETWEEN valor1 AND valor2;

CONSULTA COM PADROES DE CARACTERES LIKE E NOT LIKE

LIKE determina se uma cadeia de caracteres corresponde ao padrao especificado
NOT LIKE inverte a comparacao

metacaracteres:

'%' Qualquer cadeia de 0 ou mais caracteres, (um caractere ou uma sequencia de caracteres)
'_' Qualquer caracter unico

SELECT nome_coluna FROM nome_tabela
WHERE nome_coluna LIKE 'valor';

SELECT nome_coluna FROM nome_tabela
WHERE nome_coluna NOT LIKE 'valor';

ex:
SELECT * FROM tbl_livro
WHERE Nome_livro LIKE 'F%'; 


'F%' => comece com F e tenha 0 ou mais caracteres apos

SELECT * FROM tbl_livro
WHERE Nome_livro NOT LIKE 'S%'; 

nao 'S%' => comece com S e tenha 0 ou mais caracteres apos

SELECT * FROM tbl_livro
WHERE Nome_livro  LIKE '_i%'; 

'_i%' => comece com 1 caracter, a segunda letra seja i e tenha 0 ou mais caracteres apos

CONSULTA COM EXPRESSOES REGULARES REGEXP

[...] = qualquer caracter unico no intervalo ou conjunto especificado 

ex:
[a-h] = qualquer caracter de a a h
[aeiou] = a ou e ou i ou o ou u

[^...] = qualquer caracter unico que nao esteja no intervalo ou conjunto especificado

ex:
[^a-h] = qualquer caracter fora do intervalo de a até h
[^aeiou] = qualquer caracter fora a, e, i, o, u

^ = inicio da string (fora dos colchetes)
$ = fim da string
a|b|c = alternacao (a ou b ou c)

SELECT nome_coluna FROM nome_tabela
WHERE nome_coluna REGEXP 'expressao';

exemplo de uso:

SELECT Nome_livro FROM tbl_Livro
WHERE Nome_livro REGEXP '^[FS]';

^[FS] = comece com F ou S

SELECT Nome_livro FROM tbl_Livro
WHERE Nome_livro REGEXP '^[FS]';

^[^FS] = nao comece com F ou S

SELECT Nome_livro FROM tbl_Livro
WHERE Nome_livro REGEXP '[ng]$';

[ng]$ = termine com n ou g

SELECT Nome_livro FROM tbl_Livro
WHERE Nome_livro REGEXP '^[FS]|MI';

^[FS]|MI = comece com F ou S ou MI

CONSULTA COM MAIS DE UMA TABELA JOIN

INNER JOIN = Retorna linhas (registros) quando houver pelo menos uma correspondência em ambas as tabelas.

OUTER JOIN = Retorna linhas (registros) mesmo quando não houver ao menos uma correspondência em uma das tabelas (ou ambas).
É DIVIDO EM RIGHT JOIN, LEFT JOIN E FULL JOIN

INNER JOIN

SELECT nome_coluna 
FROM nome_tabela1
INNER JOIN nome_tabela2
ON nome_tabela1 = nome_tabela2;  
(nome_tabela1 = nome_tabela2 = relacao entre as tabelas, chave primaria e chave estrangeira)

ex: selecionando tudo

SELECT * FROM tbl_Livro
INNER JOIN tbl_autores
ON tbl_Livro.ID_Autor = tbl_autores.ID_Autor; 

ex: selecao de algumas colunas
especificar o nome_tabela.nome_coluna

SELECT tbl_Livro.Nome_Livro, tbl_Livro.ISBN, tbl_autores.Nome_Autor
FROM tbl_Livro
INNER JOIN tbl_autores
ON tbl_Livro.ID_Autor = tbl_autores.ID_Autor;

ex: selecao de algumas colunas utilizando alias

SELECT L.Nome_Livro AS Livros, E.Nome_editora AS Editoras
FROM tbl_Livro AS L
INNER JOIN tbl_editoras AS E
ON L.ID_editora = E.ID_editora
WHERE E.Nome_Editora LIKE 'M%';

ex: consulta com tres tabelas

SELECT L.Nome_Livro AS Livro,
A.Nome_autor AS Autor,
E.Nome_Editora AS Editora,
L.Preco_Livro AS 'Preço do Livro'
FROM tbl_Livro AS L
INNER JOIN tbl_autores AS A
ON L.ID_autor = A.ID_autor
INNER JOIN tbl_editoras AS E
ON L.ID_editora = E.ID_editora
WHERE E.Nome_Editora LIKE 'O%'
ORDER BY L.Preco_Livro DESC;





