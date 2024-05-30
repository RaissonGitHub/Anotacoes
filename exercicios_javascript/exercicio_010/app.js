/* ----------------------------------------------------------------------------

Exercício: 010
Enunciado:
    Existem 4 áreas a cinza.
    Ao clicar numa das áreas a área clicada deve ficar com fundo
    amarelo e as restantes a vermelho.
---------------------------------------------------------------------------- */

let boxes = document.querySelectorAll('.box')
boxes.forEach((c)=>{
    c.addEventListener('click',(e)=>{
        boxes.forEach((b)=>{
            b.style.background = 'red'
        })
        e.target.style.background = 'yellow'
    })
})
