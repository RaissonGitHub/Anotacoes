//Usando desestruturacao
//Criando diferentes variaveis a partir de uma mesma fonte
//As variaveis devem estar definidas no outro arquivo em module.exports
let {pessoa,somar,number} = require('./003e');

console.log(pessoa);
console.log(somar(50,number));
