// Sistema de rotas com switch case

const fs = require('fs');
const http = require('http');

const server = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/html');
    let html = '';
    switch (req.url) {
        case '/':
            html = 'index.html'
            break;
        case '/exemplo':
            html = 'exemplo.html'
            break;
        case '/sobre':
            html = 'sobre.html'
            break;
        default:
            html = 'erro.html'
            break;
    }
    fs.readFile('./html/' + html, (err, data) => {
        if (err) {
            console.log(err)
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