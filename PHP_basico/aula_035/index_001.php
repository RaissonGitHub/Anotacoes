<?php


// INCLUDE e REQUIRE

/* 
Tradicionalmente uma aplicação de PHP pode conter dezenas de scripts que,
combinados entre sí, permitem executar as operações desejadas.
Até agora vimos scripts isolados.
Podemos separa o código entre vários scripts e, no momento da execução,
"importar"o código para o interior da nossa aplicação.

Existem 4 fomras de executar esta tarefa:
    include
    include_once
    require
    require_once
*/


// -------------------------------------------------

// INCLUDE

include 'script.php';
include 'outro.php'; // o arquivo não existe. Irá aparecer um aviso.
include 'script.php';

/* 
A principal diferença entre inlcude e o require:
include - Mostra aviso se o script não existe e permite continuar a execução.
require - Mostra um erro se o script não existe e interrompe a execução.
*/