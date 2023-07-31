const fs = require('fs');

//Criar/escrever arquivos de forma sincrona

let log = 'Uma mensagem de log \n'; // \n Sera usado para pular uma linha


fs.writeFileSync('./logs02.log',log, {flag:'a+'}); 
// O objeto com propriedade flag:'a+' garante que o arquivo sera criado se nao exister
// E tambem que sera atualizado quando executado
