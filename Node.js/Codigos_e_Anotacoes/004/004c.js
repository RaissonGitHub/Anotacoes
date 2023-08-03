let fs = require('fs')//importando o modulo nativo fs


//Utilizando a funcao readFileSync:

//A funcao readFileSync é uma funcao sincrona
//Entao ela  sera executada de forma a seguir o fluxo do codigo
//dados retorna um buffer, coloque toSting() para que leia conforme o arquivo

//Forma tradicional

// dados = fs.existsSync('./004a.txt')
// console.log(dados.toString())

//Ira funcionar
//Porem, essa forma nao lida bem com erros

//Para melhor controle da funcao readFileSync faca assim:


let dados = '';
if (fs.existsSync('./004a.txt')) { //verificando se existe o arquivo sync
    dados = fs.readFileSync('./004a.txt') //se existir dados recebe o arquivo
    console.log(dados.toString())
} else { //senao
    console.log('Arquivo inexistente') //imprime esta mensagem
}

console.log("fim") //executado por ultimo