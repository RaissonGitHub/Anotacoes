<?php

// OPERADORES LÓGICOS

// &&    ||    !   and    or 


// && - vai devolver true se todas as condições forem verdadeiras

$x = true;
$y = true;
var_dump($x && $y); // bool(true)

$x = 20;
$y = 10;
var_dump($x > 10 && $y < 20); // bool(true)
var_dump($x > 100 && $y < 20); // bool(false)


// || - vai devolver true se, pelo menos, uma das condições for verdadeira

$x = false;
$y = true;
var_dump($x || $y); // bool(true) porque o $y é verdadeiro

var_dump(10 > 1 || 10 > 200); // bool(true) porque 10 é maior que 1
var_dump(2 < 1 || 3 < 2); // bool(false) nenhuma das condições é verdadeira

// ! - operador de negação

$nome = 'joao';
var_dump(!is_string($nome)); // bool(false) - $nome é uma string

// ---------------------------------


// o operador 'and' e 'or' têm um comportamento semelhante ao && e ||
// com ligeiras diferenças que não vamos explorar no momento.

// O PHP implementa uma filosofia de short circuit evaluation. 
// Exemplo:
var_dump(true || false);

// vai avaliar o primeiro true.
// quando encontra o operador ||, verifica que já tem informação
// suficiente para definir que a condição é verdadeira, logo, não analisa
// o resto das condições.
