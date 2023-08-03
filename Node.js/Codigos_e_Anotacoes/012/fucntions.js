// Criando uma funcao de resposta para ser exibida
function response(status,mensage,data = null){
    return {
        status,
        mensage,
        data,
        timestamp: new Date().getTime()
    }
}
module.exports = {
    response
}