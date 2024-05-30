<?php

// LOOP FOR

/* 
    for (expressao inicial; expressao condicional; expressao de incremento){
        # codigo
    }
} */

for ($indice = 1; $indice <= 10; $indice++) {
    echo "Índice: $indice<br>";
}

echo "<hr>";

// em cenários menos comuns, podemos remover alugumas expressões

/* 

for(;;){

}

Trata-se de  um cliclo infinito. Para que ele termine, será necessário
criar um cenário no interior do ciclo para que ele seja interrompido.

*/

echo '<hr>';

// Também é possivel algo do tipo: 
for ($i = 0; $i < 10; print $i, $i++) {
}
echo '<hr>';

// Também podemos usar o ciclo For para fazer uma iteração
// pelos dados de um array 
$nomes = ['joao', 'ana', 'carlos'];
for ($i = 0; $i < count($nomes); $i++) {
    echo $nomes[$i] . '<br>';
}

echo '<hr>';

// ou iterar pelas letras de uma string
$frase = "Teste com uma string.";
for ($i = 0; $i < strlen($frase); $i++) {
    echo $frase[$i] . '<br>';
}

// IMPORTANTE: sobre questões de perfomance
// se usármos uma função na expressão de avaliação da condição 
// podemos comprometer a perfomance, no caso de ser um ciclo longo. 
// Então:

$valores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]; // vamos imaginar um array gigante

//em vez de:
for ($i = 0; $i < count($valores); $i++) {
}

// podemos escrever:
for ($i = 0, $total_valores = count($valores); $i < $total_valores; $i++) {
}

// $total_valores só vai ser executado no primeiro passo do ciclo.
// A expressão de avaliação da condição vai apenas analisar o valor da variável.
