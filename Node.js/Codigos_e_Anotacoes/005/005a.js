const fs = require('fs');

//Criar e remover diretorios/pastas de forma sincrona

//A funcao mkdirSync e rmdirSync sao funcoes sincronas
//Entao elas  serao executadas de forma a seguir o fluxo do codigo

fs.mkdirSync('./pasta01'); //Cria um diretorio chamado pasta01

if(fs.existsSync('./pasta01')){ //Verifica se o diretorio existe
    fs.rmdirSync('./pasta01') //Se existe é removido
}