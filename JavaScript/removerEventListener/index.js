/* Criando e removendo EventListeners */
let b = document.querySelector('#botao')
function mudar(){
    let body = document.querySelector('body')
    body.style.background = 'blue'
    console.log('mudei')
    b.removeEventListener('click',mudar)//Remove um EventListener, não executa mais
}
b.addEventListener('click',mudar) //Cria um EventListener
