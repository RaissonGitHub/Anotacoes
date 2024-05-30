<?php

// Boleans

$apresentar_nome = true; 
$apresentar_idade = false;

// Os valores são caseinsentive

$mostar = FALSE; // o mesmo que $mostrar = false;

// O valor 0 é igual a false
// Qualquer outra valor é igual a true

// Podemos determinar se uma variável é booleana ou não

var_dump(is_bool($mostar));
echo '<br>';
$mostar = 1;
var_dump(is_bool($mostar));
