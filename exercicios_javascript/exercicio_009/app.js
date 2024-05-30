/* ----------------------------------------------------------------------------

Exercício: 009
Enunciado:
    Exercício simples: O texto é branco e o elemento range vai servir para
    alterar a transparência do texto. Do valor mais opaco à esquerda, até
    à transparência total à direita.

    NOTA: Deves definir os valores do range.
---------------------------------------------------------------------------- */
let range = document.querySelector('#range')
range.setAttribute('max', 100)
range.setAttribute('min', 1)
range.setAttribute('value', 100)
range.addEventListener('input', (e) => {
    document.querySelector('h3').style.opacity = e.target.value/100
})
