<?php

// A declaração de variáveis em php é feita usando o símbolo de $ antes do nome

// Estou declarando uma variável nome e atribuindo uma String 'João'
// Strings sempre devem conter '' ou ""
$nome = 'João';

echo $nome; //Imprimindo a variável

// Uma variavel pode mudar de valor

$nome = 'Carlos';

echo $nome; //Imprimindo a variável com novo valor


// Uma forma peculiar de declarar multiplas variáveis com o mesmo valor pode ser feita assim

$laranja = $banana = $pera = 'Frutas';
echo $laranja; //Frutas
echo $banana; //Frutas
echo $pera; //Frutas

// Uma variavel pode conter números inteiros

$valor1 = 100;

echo $valor1;

// Pode ser feita como no exemplo anterior

$v1 = $v2 = $v3 = 100;

// Pode conter operações

$soma = 1+1;

// Pode conter operações entre variáveis

$total = $valor1 - $v1;

// Para apresentar o valor de uma variável dentro de uma string

// Com aspas simples ele não imprime o valor das variáveis
echo 'Meu nome é $nome, olá!'; // Meu nome é $nome, olá!

// Com aspas duplas ele imprime
echo "Meu nome é $nome, olá!"; //Meu nome é Carlos, olá!
