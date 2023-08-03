const fs = require('fs');

//Criar/escrever arquivos de forma assincrona

let log = 'Uma mensagem de log \n'; // \n Sera usado para pular uma linha


fs.writeFile('./logs02.log',log, {flag:'a+'}, (err)=>{
    if(err){
        console.log(err)
    }
}); 
// O objeto com propriedade flag:'a+' garante que o arquivo sera criado se nao exister
// E tambem que sera atualizado quando executado

// fs.writeFile() possui uma funcao de callback para verificar erros

console.log('Fim')