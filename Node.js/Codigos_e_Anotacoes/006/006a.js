const fs = require('fs');

//Criar/escrever arquivos de forma sincrona

//A funcao writeFileSync é uma funcao sincrona
//Entao ela  sera executada de forma a seguir o fluxo do codigo

let log = 'Uma mensagem de log';

fs.writeFileSync('./logs.log',log); //So cria e nao acrescenta conforme atualiza
