//Usando middlewares
// Middlewares sao partes de codigos executadas entre um request e um response

const express = require('express');
const app = express();
app.listen(3000);

// A funcao use() esta sendo executada como middleware
//use mais um parametro next para que o servidor nao fique experando uma resposta
app.use((req,res,next)=>{ //executada entre  request e  response
    console.log('Teste')
    next()// permite que o servidor prossiga
})

//Mais um middleware, agora pegando o horario que a funcao e executada
app.use((req,res,next)=>{
    req.requestTime = Date.now();
    next()
})

app.get('/',(req,res)=>{
    console.log(req.requestTime)
    res.send('<h1>Olá<h1>')
})