/* ----------------------------------------------------------------------------

Exercício: 004
Enunciado: TRÊS SLIDERS COM VALORES INDEPENDENTES
    
    Estão disponíveis três input ranges e respetivas áreas de apresentação dos valores.
    Criar os mecanismos que permitem visualizar os valores dos sliders.
    Todos os sliders devem variar entre 0 e 100. Essas propriedades devem ser
    definidas através do JavaScript.

---------------------------------------------------------------------------- */
let ranges = document.querySelectorAll('#range_1,#range_2,#range_3')
let values = document.querySelectorAll('#value_1,#value_2,#value_3')

for(let i = 0;i<ranges.length;i++){
    ranges[i].setAttribute('max',100)
    ranges[i].setAttribute('min',0)
    ranges[i].setAttribute('value',0)
    ranges[i].addEventListener('input',(event)=>{
        values[i].textContent = event.target.value
    })
}

