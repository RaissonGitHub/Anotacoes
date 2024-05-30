<?php

// ESTRUTURAS CONDICIONAIS IF...ESLEIF...ELSE


/* 
if(condição){
    ...executar o código 
}
*/

$valor = 10;

if ($valor = 10) {
    echo 'ok';
}

if ($valor > 10) {
    echo 'o valor é maior que 10';
} else {
    echo 'o valor é igual ou inferior a 10';
}

if ($valor > 100) {
    // ...
} elseif ($valor > 50) {
    // ...
} elseif ($valor > 30) {
    // ...
} elseif ($valor > 10) {
    // ...
} elseif ($valor > 5) {
    // ...
} else {
    // ...
}

// também é possivel usar IF dentro de IF  

if ($valor > 5) {
    if ($valor == 10) {
        // ...
    } else {
        // ...
    }
} else {
    // ...
}
