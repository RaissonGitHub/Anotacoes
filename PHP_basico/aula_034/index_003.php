<?php

// ESCOPO DE VARIÁVEIS

/* 
Neste caso, a variável $nome terá  duas versões:
Uma global que existe ao logno do script.
Outra local que é criada e terminada dentro do bloco da função.
*/

$nome = 'joao';

function dados(){
    $nome = 'joaquim';
}

dados();

echo $nome;