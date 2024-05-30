/* ----------------------------------------------------------------------------

Exercício: 027
Enunciado:
    Existe um input de texto no qual, sempre que for alterado o seu conteúdo,
    o mesmo deve ser apresentado em tempo real no div cujo id é igual a "conteudo".
    Contudo, se o texto contém a palavra "olá", a cor do texto deve ser verde.
    Caso contrário deverá ser sempre branca.
---------------------------------------------------------------------------- */
document.querySelector('#text_frase').addEventListener('input',(e)=>{
    let conteudo = document.querySelector('#conteudo')
    conteudo.textContent =  e.target.value
    conteudo.style.color =  e.target.value.includes('olá') ? 'green': 'white'

})