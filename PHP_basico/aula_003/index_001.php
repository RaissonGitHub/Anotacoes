<?php
    // Constantes

    // Definir uma constante
    define('nome','valor');
    
    // por convenção as constantes são definidas com letras maiúsculas
    define('TAXA_FIXA', 10);
    define('APRESENTAR_DADOS', false);

    // Apresentar o valor de uma constante
    echo TAXA_FIXA; // 10

    // Usar o valor  de uma constante

    $preco_inicial = 500;
    $preco_final = $preco_inicial + TAXA_FIXA;
    echo $preco_final; //510

    // Não podemos alterar o valor de uma constante

    // Também podemos definir uma constante utilizando const

    const NOME = 'Jorge';
    echo NOME;

    // Não é uma forma comum de declarar constantes
    // Com define podes declarar uma variável em qualquer lugar do código
    // Com const existem estruturas das quais não podemos criar as constantes.

    // O PHP possui constantes próprias

    echo PHP_VERSION;
    echo '<br>';

    // e tem alguns tipos de constantes que são definidas de forma dinâmica
    // são designadas por constantes mágicas

    echo "Estou executando este código na linha " . __LINE__;
    
    