<?php

// EXPRESSÃO MATCH

$estado_encomenda = 'em processamento';

switch ($estado_encomenda) {
    case 'em processamento' :
    case 'em análise' : 
        # código
        break;
    case 'anulada':
    case 'cancelada':
        # código
        break;
    case 'enviada':
        # código
        break;
    default:
        # código
        break;
}
// -------------------------------------------------

$resultado = match($estado_encomenda) {
    'em processamento' => 'A encomenda está sendo tratada',
    'anulada', 'cancelada' => 'A encomenda foi anulada ou cancelada',
    'enviada' => 'Encomenda enviada',
    default => 'Estado da encomenda desconhecido'
};

