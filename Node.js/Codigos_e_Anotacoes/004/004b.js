let fs = require('fs'); //importando o modulo nativo fs

//Utilizando a funcao readFile:

//A funcao readFile é uma funcao assincrona
//Entao ela nao sera executada de forma a seguir o fluxo do codigo
//Ela sera executada no final

//ela recebe dois parametros: o arquivo e uma arrow function com parametros err e data
//se houver erro imprima o erro
//senao imprimia o conteudo do arquivo
//data retorna um buffer, coloque toSting() para que leia conforme o arquivo
fs.readFile('./004a.txt',(err,data)=>{
    if(err){
        console.log(err)
    } else{
        console.log(data.toString())
    }
})

console.log("fim") //executado primeiro