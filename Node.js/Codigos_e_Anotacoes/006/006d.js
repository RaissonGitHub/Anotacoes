const fs = require('fs');

//Remover arquivos de forma sincrona

if(fs.existsSync('./logs.log')){
    fs.unlinkSync('./logs.log')
} else{
    console.log('Ocorreu um erro')
}