/* ----------------------------------------------------------------------------

Exercício: 016
Enunciado:
    Ao clicar em "Adicionar", se o input tiver texto, adicionar o mesmo num
    parágrafo por baixo do botão. 
    Não importa a ordem das palavras e frases.
    Quando clicar em "Limpar", todas as palavras e frases devem desaparecer
    e o input deve ficar limpo e receber o focus.

    NOTA: O HTML não pode ser alterado.
---------------------------------------------------------------------------- */

let texto = document.querySelector('#text_post')
document.querySelector('.text-center').lastElementChild.addEventListener('click',()=>{
    if(texto.value){
        let p = document.createElement('p')
        p.textContent = texto.value
        document.querySelector('#posts').prepend(p)
        texto.value = ""
        texto.focus()
    }
})
document.querySelector('.text-center').firstElementChild.addEventListener('click',()=>{
    document.querySelector('#posts').innerHTML = null
    texto.value = ""
    texto.focus()
})