/* Desabilitar acoes padrao */

// Desabilitando um link
document.querySelector('a').addEventListener('click',(e)=>{
    e.preventDefault()
})

// Desativando o envio do formulario
document.querySelector('input[type ="submit"]').addEventListener('click',(event)=>{
    event.stopPropagation()
    console.log(event)
    event.preventDefault()
})

// Cuidado com a propagacao
// Se nao houver um stopPropagation() essa funcao ira excutar ao apertar no input submit 
document.querySelector('div').addEventListener('click',()=>{
    console.log('div')
})