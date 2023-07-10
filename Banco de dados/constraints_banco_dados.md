# CONSTRAINTS (restricoes):

## NOT NULL

* **Nao permite entradas nulas**, torna o campo como **preenchimento obrigatorio**;

## UNIQUE

* Identifica de forma **unica** cada registro em uma tabela;

* Primary keys **ja possuem** uma restricao **unique**;

* Pode haver varias constraints unique, mas **apenas uma primary key**;

* Exemplo: CPF;

## PRIMARY KEY - Chave primaria

* Identifica de forma **unica** cada regisro em uma tabela;

* Deve haver **uma e somente uma** em uma tabela;

* Nao nula;

## FOREIGN KEY - Chave estrangeira

* Campo que aponta para uma chave primaria de outra tabela;

## DEFAULT

* Usada para inserir um valor padrao em uma coluna;

* Sera adicionada caso o valor nao seja especificado;
