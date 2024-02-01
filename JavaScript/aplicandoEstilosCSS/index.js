/* Obter valores de um elemento através do window */

let h1 = document.querySelector('h1') //estilo inline
console.log(h1.style.color) //blue
let p = document.querySelector('p') //estilo atraves da tag style ou css externo
console.log(p.style.color) //sem retorno

const estilos = window.getComputedStyle(p) //através do window (janela) pego o estilo de (p)
console.log(estilos.getPropertyValue('color')) // white