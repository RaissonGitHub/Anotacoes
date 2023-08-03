//Lidando com parametros
//Usando modulos

const express = require('express');
const app = express();
const func = require('./funcoes')
app.listen(3000);


app.get('/somar/:a/:b', (req,res)=>{
    const a = parseInt(req.params.a)
    const b = parseInt(req.params.b)
    const somar = func.somar(a,b)
    res.send(`Resultado = ${somar}`) //send() precisa ter uma string, caso coloque apenas um numero, retornara um erro
})
app.get('/subtrair/:a/:b', (req,res)=>{
    const a = parseInt(req.params.a)
    const b = parseInt(req.params.b)
    const subtrair = func.subtrair(a,b)
    res.send(`Resultado = ${subtrair}`)
})