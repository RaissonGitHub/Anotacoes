<?php

// PARAMETROS DE UMA FUNÇÃO

/* 
Podemos definir parametros opcionais dentro de uma função.
São parametros que já têm um valor padrão atribuído.
Se passarmos um argumento para esse parametro, o valor passado será usado.
Vejamos:
*/

function multiplicar($a, $b=5){
    return $a * $b;
}

echo multiplicar(10); // 50
echo '<br>';
echo multiplicar(10,3); // 30

// IMPORTANTE: os parametros opcionais devem sempre sser definidos
// depois dos parametros não opcionais