<?php

// Operadores de incremento e decremento
// ++ --

// Permite incrementar ou decrementar um valor em uma unidade
// Pode ser usado como pré-incremento ou pós-incremento.

$x = 10;

// pós-incremento e pós-decremento
$x++;
$x--;

// pré-incremento e pré-decremento

++$x;
--$x;

// Como funcionam os resultados?


$x = 100;
echo $x++; // vai apresentar o valor 100 e passasr a variável para 101
echo $x--; // vai apresentar o valor 100 e passasr a variável para 100

echo ++$x; // vai passar a variável para 101 e apresentar 101
echo --$x; // vai passar a variável para 100 e apresentar 100

