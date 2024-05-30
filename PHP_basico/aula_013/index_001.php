<?php

// OPERADORES MATEMÁTICOS

// + - * / % **

$x = 10;
$y = 5;

// Adição

echo '<pre>';

echo 10 + 20; // 30

echo '<br>';

var_dump($x + $y);

// Subtração

echo 20 - 10;

echo '<br>';


var_dump($x - $y);

// Multiplicação

echo 10 * 20;

echo '<br>';


var_dump($x * $y);

// Divisão

echo 20/10;

echo '<br>';

var_dump($x/$y);

// Resto da divisão

echo 20%3;

echo '<br>';

var_dump($x%$y);

// Potenciação

echo 5**3;
 
echo '<br>';

var_dump($x**$y);

// INTERESSANTE

var_dump(-10);  // int(-10)
var_dump("10"); // string(2)"10"
var_dump(+"10"); // int(10)

var_dump(10/2); // int(5)
var_dump(10/3); // float(3.33333333335)
var_dump(10/2.00); // float(5)

// var_dump(10/0);  // ERRO! divisão por zero
// Para evitar  o erro

var_dump(fdiv(10,0));

// Cuidado com os módulos

var_dump(10%2); // int(0)
var_dump(10%3); // int(1)
var_dump(10%6); // int(4)
var_dump(10.5%3.2); // Deprecated!
var_dump(fmod(10.5,3.2)); // float(0.8999999999995)
// Os valores envolvidos na operação são sempre modificados para int
// para valores float são removidos as casas decimais