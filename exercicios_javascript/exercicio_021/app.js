/* ----------------------------------------------------------------------------

Exercício: 021
Enunciado:
    Existem 4 inputs na página.
    1. Coloca o focus automaticamente no input acima e à esquerda.
    2. Sempre que pressionares a tecla Enter (return), o focus deverá
    passar para o input seguinte, mesmo que não tenhas escrito qualquer texto.
---------------------------------------------------------------------------- */
let a = document.querySelectorAll('.form-control')
a[0].focus()
let index = 1
a.forEach((element) => {
    element.addEventListener("keyup", (e) => {
        if (e.code == 'Enter') {
           a[index].focus()
           index++
           if(index>=a.length) index = 0;
        }
    })

})
