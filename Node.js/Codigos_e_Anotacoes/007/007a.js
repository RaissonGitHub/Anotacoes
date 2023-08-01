// Utilizando express
// Com o npm instalado

const express = require('express'); //importando o modulo express
const server = express(); // criando um objeto que é uma instancia do express, esse objeto tambem é chamado de app

//Criando uma conexao com express

//Na funcao get, defina a porta,
//a funcao callback para trabalhar com request e response
server.get('/', (req, res) => {
    res.send('Olá, express!')//Envia a mensagem
});
server.listen(3000); //Define a porta do servidor