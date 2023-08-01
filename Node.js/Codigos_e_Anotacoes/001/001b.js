// Sistema de rotas com switch case

const fs = require('fs');
const http = require('http');

const server = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/html');
    let html = '';
    switch (req.url) {
        case '/':
            html = 'index.html'
            res.statusCode = 200 // indicando o status code da resposta (200 => certo, 301 => redirecionado, 404 => nao encontrado)
            break;
        case '/home': //caso coleque /home na url
            res.setHeader('Location', '/') //sera redicionado para /
            res.statusCode = 301 // indicando o status code da resposta 
            res.end() //encerrando a resposta   
            break;
        case '/exemplo':
            html = 'exemplo.html'
            res.statusCode = 200
            break;
        case '/sobre':
            html = 'sobre.html'
            res.statusCode = 200
            break;
        default:
            html = 'erro.html'
            res.statusCode = 404
            break;
    }
    fs.readFile('./html/' + html, (err, data) => {
        if (err) {
            console.log(err)
            res.statusCode = 404
            res.end()
        }
        else {
            res.write(data)
            res.end()
        }
    })
})

server.listen(3000, 'localhost', () => {
    console.log('Servidor rodando na porta 3000!')
})