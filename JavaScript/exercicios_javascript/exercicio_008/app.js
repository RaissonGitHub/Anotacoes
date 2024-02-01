/* ----------------------------------------------------------------------------

Exercício: 008
Enunciado:
    Existem 5 botões, cada um com uma cor diferente do Bootstrap.
    A ideia é criar o código javascript que permita que o clique em cada
    um dos botões altere o texto acima para a cor de fundo do botão.
---------------------------------------------------------------------------- */
let texto = document.querySelector('h3')
let b = document.querySelectorAll('.btn')
b.forEach((e)=>{
    e.addEventListener('click',(event)=>{
        texto.style.color = window.getComputedStyle(event.target).getPropertyValue('background-color')
    })
})