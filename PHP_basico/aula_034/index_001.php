<?php

// ESCOPO DE VARIÁVEIS

$nome = 'joao'; // é uma variável de escopo global

/* Esta varável vai estar diponível para ser usada dentro de instruções condicionais e 
ciclos neste script e em outros scripts que opssam ser importados 
para o interior deste script. (include e require) 
*/

if(true){
    echo $nome . "<br>";
}

for($i=1;$i<=2;$i++){
    echo $nome . '<br>';
}