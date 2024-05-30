<?php

// OPERADORES DE COMPARAÇÃO
// == === != <> !== < > <= >= <=> ?? ?:

// Verificar se os valores são iguais

var_dump(10 == 20); // bool(false)
var_dump(5 == 5); // bool(true)
var_dump('Relógio' == 'relógio'); // bool(false)
var_dump('Porto' . ' ' . 'Alegre' == 'Porto Alegre'); // bool(true)


var_dump(10 == '10'); // bool(true)
// O resultado ocorre porque há uma conversão implicita de string para número

// Para resolver compare o valor e o tipo de dado com o operador ===
var_dump(10 === '10'); // bool(false)

var_dump(1 == true); // bool(true)
var_dump(1 === true); // bool(false)

// Verificar se os valores são diferentes

var_dump(10 != 20); // bool(true) os valores são diferentes
var_dump(5 != 5); // bool(false) os valores não são diferentes
var_dump(5 != '5'); // bool(false) os valores não são diferentes

var_dump(5 !== '5'); // bool(true) O tipo de dados influenciou

var_dump(20 <> 30); // bool(true) É equivalente ao operador !=

// IMPORTANTE: No PHP 8 temos o seguinte código:

var_dump(0 == 'jorge');
// Uma vez que uma string não pode ser convertida em um número
// o PHP converte o 0 para string e compara ambos como string
// var_dump("0" == 'jorge');
// Neste caso da bool(false)

var_dump(10 > 5); // bool(true)
var_dump(10 < 5); // bool(false)
var_dump(10 > 10); // bool(false)
var_dump(10 >= 10); // bool(true)
var_dump(10 <= 10); // bool(true)

// IMPORTANTE:

var_dump('joao' >= 'sara'); // bool(false)
var_dump('joao' <= 'sara'); // bool(true)


// spaceship operator | operador nave espacial
// <=>
// Compara se o valor na esquerda é maior, igual, ou menor que o da direita
// Retorna 1 se o da esquerda for maior que o da direita
// Retorna 0 se ambos forem iguais
// Retorna -1 se o da esquerda for menor que o da direita

var_dump(20 <=> 10); // int(1)
var_dump(20<=>20); // int(0)
var_dump(20<=>30); // int(-1)

// Operadores condicionais
// ?? ?:

// Operador tenário 
$valor = 'joao';
echo $valor == 'joao' ? 'SIM' : 'NÃO'; // SIM
// Explicação: se $valor for igual a 'joao' então imprima 'SIM' senão imprima 'NÃO'

// null coalescing operator | operador de coalescência nulo
$valor = null;
$a = $valor ?? 'ok'; // $a = 'ok'
// Se a variavel $valor é nula $a assumirá o valor na frente do operador

$valor = 10;
$a = $valor ?? 'ok'; // $a = 10
