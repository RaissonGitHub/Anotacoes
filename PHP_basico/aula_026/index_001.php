<?php

// OPERADOR TERNÁRIO

$idade = 15;
echo "Eu sou " . ($idade >= 18 ? 'menor de idade.' : 'maior de idade.');

echo '<br>';

$erro = true;

echo 'Resultado: ' . ($erro ? 'aconteceu um erro' : 'sucesso');
