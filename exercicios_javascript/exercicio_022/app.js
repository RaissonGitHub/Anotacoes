/* ----------------------------------------------------------------------------

Exercício: 022
Enunciado:
    Está disponível um elemento select com 3 opções.
    Por baixo existem 4 checkboxes.
    Quando é selecionada a opção 3 no select, as checkboxes devem ficar ativas.
    Qualquer outra opção, devem desativar as checkboxes.
---------------------------------------------------------------------------- */
checar('disabled')
document.querySelector('.form-select').addEventListener('change',(event)=>{
    if(event.target.value == 3){
       checar('enabled')
    }
    else{
       checar('disabled')
    }
})

function checar(estado){
    if(estado == 'disabled'){
        document.querySelectorAll('input[type="checkbox"').forEach(e => e.setAttribute('disabled',true))
    }else{
        document.querySelectorAll('[id^="check_"]').forEach(e => e.removeAttribute('disabled'))
    }
}