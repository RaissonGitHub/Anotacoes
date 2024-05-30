<?php

// PARAMETROS DE UMA FUNÇÃO

/* 
O PHP vae sempre tentar determinar o data type dos parametros e do return.
Podemos reforçar o tipo de valores que vão ser retornados da seguinte forma:
*/

function adicionar($a, $b) : int{
    return $a + $b;
}

echo adicionar(10,20) . "<br>";

/* Se for alterado o data type para string... */

function multiplicar($a,$b) : string{
    return $a * $b;
}

echo multiplicar(10,2); // vai apresentar o resultado normalmente. Porquê?

// Existe um mecanismo no PHP designado por strict types.
// Se esse mecanismo não estiver ativo, o PHP  vai tentar sempre fazer
// a conversão implícita dos valores.