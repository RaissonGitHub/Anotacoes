//Lidando com parametros

const express = require('express');
const app = express();
app.listen(3000);

const pessoas = [
    {nome:'Jose',sobrenome:'Silva', cpf:12345678910},
    {nome:'Joao',sobrenome:'Damasco', cpf:34512345678},
    {nome:'Jania',sobrenome:'Cardoso', cpf:34512387158}
]

app.get('/pessoas/:nome', (req,res)=>{
    const cliente = pessoas.find( c => c.nome === req.params.nome)//Procura o nome informado como parametro
    if(!cliente){//Se nao existir
        res.status(404).send('Erro')
    }
    else{//Se existir informe suas informacoes
        res.send(`O nome do cliente é ${cliente.nome}, seu sobrenome é ${cliente.sobrenome}, e seu cpf é ${cliente.cpf} `)
    }
})