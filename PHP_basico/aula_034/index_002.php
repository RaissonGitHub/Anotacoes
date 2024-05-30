<?php

// ESCOPO DE VARIÁVEIS

/* 
No entanto, a variável não estará acessível dentro de uma função.
*/

$nome = 'joao';

function executar(){
    echo $nome;
}

executar();

/* 
Todas as variáveis dentro de uma função têm escopo local.
Apenas existem dentro da função.
Elas são criadas dentro da função e destruidas assim que
a função termina a sua execução.
*/
function adicionar(){
    $a = 100;
}

echo $a;
