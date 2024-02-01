/* ----------------------------------------------------------------------------

Exercício: 023
Enunciado:
    Existem 4 checkboxes referentes a um conjunto de permissões de usuário.
    Cada checkbox pode ser checkada individualmente.
    Por baixo existem duas opções: todas e nenhuma.
    Ao clicar em todas, todas as checkboxes devem ser checkadas.
    Ao clicar em nenhuma, todas as checkboxes devem ser descheckadas.
---------------------------------------------------------------------------- */

document.querySelector('#all').addEventListener('click',()=>{
    document.querySelectorAll('[name^="check_"]').forEach(e=>e.checked =true)
})
document.querySelector('#none').addEventListener('click',()=>{
    document.querySelectorAll('[name^="check_"]').forEach(e=>e.checked =false)
})