<?php

    // STRINGS

    $nome = 'João';
    $sobrenome = "da Silva"; 

    // As duas variáveis são do tipo String

    // Nas aspas duplas pode ser adiciona o valor de uma variável

    $saudacao = "O meu nome é $nome e meu sobrenome é $sobrenome.";

    // Podemos melhorar a leitura usando a seguinte equivalência

    $saudacao = "O meu nome é {$nome} e meu sobrenome é {$sobrenome}.";
   
    // Concatenação de Strings
    // utilize os . (pontos) para concatenar

    $nome_completo = $nome . ' ' . $sobrenome;

    echo $nome_completo;
    echo "<br>";
    
    // Como obter a primeira letra do nome
    
    echo $nome[0];
    echo "<br>";
    
    // Modificar letras
    
    $nome[1] = 'u';
    echo $nome;
