/* ----------------------------------------------------------------------------

Exercício: 006
Enunciado:
    Existem 3 botões no layout. Cada botão está associado a uma área de
    informação. O objetivo é criar a lógica que permite apresentar cada
    uma das áreas de acordo com o botão clicado.
    A área de informação um deve estar visível por padrão.

    NOTA: quando uma área é apresentada, as outras devem ficar escondidas
---------------------------------------------------------------------------- */

let b = document.querySelectorAll('.btn-secondary')
let a = document.querySelectorAll('.caixa-informacao')

function ver(id){
    a[id].style.display = 'block'
}
function esconder(){
    a.forEach(e => e.style.display = 'none')
}
esconder()
ver(0)
for(let i =0; i< b.length; i++){
    b[i].addEventListener('click',()=>{
        esconder()
        ver(i)
    })
}
