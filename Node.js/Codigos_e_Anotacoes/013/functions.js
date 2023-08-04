function response(status,mensage,aftrows,data = null){
    return{
        status,
        mensage,
        aftrows,
        data,
        timestamp: new Date().getTime
    }
}
module.exports = {
    response
}