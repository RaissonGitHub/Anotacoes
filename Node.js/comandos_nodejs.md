# Comandos Node.js

## Criar um servidor web

```
const http = require('http');

const server = http.createServer((request,response) => {
    response.end('Teste')
}).listen(3000,function(){
    console.log('Servidor rodando na porta 3000')
})
```

`const http = require('http');` 

O que faz:

Carrega o modulo http.

```
const server = http.createServer((request,response) => {
    response.end('Teste')
})
``` 

O que faz:

Cria uma conexão atraves do metodo `createServer()` que possui uma arrow function com dois parametros:request ou req e response ou res.

request: Representa a requisição feita pelo cliente ao servidor. 

response: Representa a resposta que o servidor enviará de volta ao cliente.

`response.end('Teste')` envia o texto "Teste" quando a página é carregada.

`response.end()` se estiver vazio, apenas termina o programa

```
server.listen(3000,function(){
    console.log('Servidor rodando na porta 3000')
})
```

O que faz:

Inicializa o servidor que fica escutando as conexoes na porta definida

O metodo `listen()` recebe dois parametros: a porta que ficara sendo ouvida e uma função que imprime uma mensagem no terminal quando o servidor é inicializado.

\# A porta escolhida foi a 3000, mas é possivel colocar outras portas também

\# Para verificar o servidor criado, no navegador, coloque a URL http://localhost:3000

__dirname => representa o diretorio atual

__filename => representa o arquivo atual

## Status codes HTTP

* 200 => Ocorreu tudo normalmente
* 301 => Recurso disponivel, mas em lugar diferente
* 404 => Recurso nao encontrado no servidor
* 500 => Erro no servidor

## Respostas com enviadas 

* 100 => Respostas informativas
* 200 => Codigos de status de sucesso
* 301 => Redirecionamentos
* 404 => Erros de clientes ou utilizador (recursos nao encontrados)
* 500 => Erro internos do servidor