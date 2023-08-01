// Utilizando express
// Com o npm instalado

const express = require('express'); //importando o modulo express
const app = express(); // criando um objeto que é uma instancia do express

//Criando rotas com express

//Na funcao get: defina a porta e
// a funcao callback para trabalhar com request e response

// O proprio express interpreta o tipo do arquivo
// nao é necessario definir um header

app.get('/', (req, res) => {
    res.send({'name':'Leonardo'})//Envia o objeto
});
app.get('/h1', (req, res) => {
    res.send('<h1>Título</h1>')//Envia o html
});

//Para pagina nao encontrada
app.use((req,res)=>{
    res.status(404).send('Erro!') //Defina o status e uma mensagem
})

app.listen(3000); //Define a porta do servidor