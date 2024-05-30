/* ----------------------------------------------------------------------------

Exercício: 015
Enunciado:
    Ao clicar em "Adicionar", se o input tiver texto, adicionar o mesmo num
    parágrafo por baixo do botão.

    As palavras e frases mais recentes devem ficar no topo.
---------------------------------------------------------------------------- */
let index = 0
document.querySelector('.btn').addEventListener('click',()=>{
    let texto = document.querySelector('#text_post')
    if(texto.value){
        let p = document.createElement('p')
        p.textContent = texto.value
        document.querySelector('#posts').prepend(p)
        texto.value = ''
        texto.focus()
    }
})
