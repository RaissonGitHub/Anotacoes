/* ----------------------------------------------------------------------------

Exercício: 006
Enunciado:
    O mesmo exercício do vídeo anterior, mas com código mais sintético.
---------------------------------------------------------------------------- */
let b = document.querySelectorAll('.btn-secondary')
let a = document.querySelectorAll('.caixa-informacao')
a.forEach(e => e.style.display = 'none')
a[0].style.display = 'block'
for(let i =0; i< b.length; i++){
    b[i].addEventListener('click',()=>{
        a.forEach(e => e.style.display = 'none')
        a[i].style.display = 'block'
    })
}