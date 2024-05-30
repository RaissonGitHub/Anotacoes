<?php

// BREAK e CONTINUE

/* 

Os loops são usados para excutar o mesmo código múltiplas vezes.
Em determinadas situações, podemos querer que o ciclo não execute todas as
suas iterações, ou queremos que seja simplesmente interrompido.

É neste cenários que entra  o break e o continue. 

*/

// BREAK

$paragem = 5;
for($i = 0; $i <=10; $i++){
    echo "$i<br>";
    if($i == $paragem){
        break;
    }

    // ou
    // if($i == $paragem) break;
}

echo '<hr>';

$nomes = ['joao', 'ana', 'carlos', 'andre', 'ricardo'];
$nome_que_vai_interromper = 'carlos';
foreach($nomes as $nome){
    echo "$nome<br>";
    if($nome == $nome_que_vai_interromper) break;
}

// IMPORTANTE: tanto o break ou o continue,
// também funcionam nos ciclos while e do while