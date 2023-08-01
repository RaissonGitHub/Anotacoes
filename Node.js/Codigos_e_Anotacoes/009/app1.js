//Utilizando o morgan para middlewares

const express = require('express');
const morgan = require('morgan');
const app = express();
app.listen(3000)

app.use((morgan(':method :status :url')))// Fornece o metodo, o status e a url do request
app.use((morgan('Método = :method | Url = :url | Status = :status' )))//Enfeitado

app.get('/', (req,res)=>{
    res.send('Teste')
})