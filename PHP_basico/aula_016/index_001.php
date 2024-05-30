<?php

// OPERADORES DE STRINGS

// . .=

// Operadores de concatenação

$nome = 'João';

$nome = $nome . 'Ricardo';

$apresentacao = "Bom dia, " .  $nome . ".";

// Simplificando o código 

$nome = 'João';
$nome .= 'Ricardo'; // João Ricardo

// Juntando mais

$cliente = 'João Ricardo';
$email = 'adfs@gmail.com';
$telefone = '12211212';

$completo = $cliente . ' - ' . $email . ' - ' . $telefone;
// João Ricardo - adfs@gmail.com - 12211212