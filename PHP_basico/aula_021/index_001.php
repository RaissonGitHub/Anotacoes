<?php


// PRECENDÊNCIA DE OPERADORES

// Frequentemente os operadores são combinados para formar expressões complexas.
// Quando isso acontece, eles são tratados de acordo com a sua precêdencia.
// No PHP ela funciona na maioria das vezes  da mesma forma como na Matemática.

$resultado = 10 + 20 * 4;
// a multiplição acontece primeiro (20 * 4 = 80)
// depois acontence a adição (10  + 80 = 90)

// Podemos forçar a precedência usando parêntesis

$resultado = (10 + 20) * 4;
// neste caso a adição acontece primeiro e só depois a multiplicação
// 30 * 4 = 120

$valor1 = 4;
$valor2 = 2;
$valor3 = 10;

// mesmo nível de procedência
$resultado = $valor1 / $valor2 * $valor3;
echo $resultado;
