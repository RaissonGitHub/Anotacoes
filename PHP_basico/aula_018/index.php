<?php

// OPERADOR DE CONTROLE DE ERRO

// Existem várias formas de contornar erros no PHP
// Este operador, quando aplicado a uma expressão que vai gerar um erro, 
// permite que esse erro seja ignorado.

// $arquivo = file('teste123.txt');

// este código vai gerar um aviso.
// se adicionarmos o operador de controle de erro,
// a mensagem do aviso vai desaparecer, sendo a instrução ignorada.

$arquivo = @file('teste123.txt');

echo 'fim';

// Não é aconselhável usar este operador, exeto em situações
// muito específicas, uma vez que a supressão da mensagem de erro 
// pode impedir que encontremos um erro no nosso código.