<?php

// PARAMETROS DE UMA FUNÇÃO

// como forçar os  strict types?

declare(strict_types=1);

// string agora dá erro
// se não haver |float irá ocorrer um erro caso algum argumento seja float
function multiplicar($a,$b) : int|float{
    return $a * $b;
}

echo multiplicar(10.5,2);