<?php

// EXPRESSÃO MATCH

$valor = 50;

$resultado = match(true){
    $valor >100 => fn1(),
    $valor ==100 => fn2(),
    $valor <100 => fn3(),
};

echo $resultado;

function fn1(){
    return 'valor maior que 100';
}
function fn2(){
    return 'valor igual a 100';
}
function fn3(){
    return 'valor menor que 100';
}