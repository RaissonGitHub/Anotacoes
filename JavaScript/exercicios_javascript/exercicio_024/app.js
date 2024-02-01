/* ----------------------------------------------------------------------------

Exercício: 024
Enunciado:
    Existem 8 checkboxes referentes a um conjunto de permissões de usuário.
    Cada uma delas pode ser checkada individualmente.
    Por baixo, existe um select com 3 perfis de usuário: administrador, coordenador
    e operador.
    Ao selecionar um perfil, as checkboxes devem ser checkadas de acordo com o
    perfil selecionado.

    Administrador: 
        Todas as permissões

    Coordenador: 
        Coordenação dos trabalhos
        Gestão de calendário
        Utilização das máquinas
        Utilização das ferramentas

    Operador:
        Utilização das máquinas
        Utilização das ferramentas

    NOTA: sem perfil, todas as checkboxes devem estar descheckadas.

---------------------------------------------------------------------------- */

document.querySelector('#select_perfil').addEventListener('change', (e) => {
    document.querySelectorAll('input[type="checkbox"').forEach((c) => {
        c.checked = false
    })
    if (e.target.value == 'administrador') {
        document.querySelectorAll('input[type="checkbox"').forEach(c => c.checked = true)
    }
    else if (e.target.value == 'coordenador') {
        let c = document.querySelectorAll('input[type="checkbox"')
        c[4].checked = true
        c[5].checked = true
        c[6].checked = true
        c[7].checked = true
    }
    else if (e.target.value == 'operador') {
        let c = document.querySelectorAll('input[type="checkbox"')
        c[6].checked = true
        c[7].checked = true
    }
})
