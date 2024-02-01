/* Validacao de formularios no front-end */
// Formulario_login é o nome do formulario definido no HTML
document.formulario_login.addEventListener("submit",(e)=>{
    
    //buscar os valores
    let  user = e.target.user.value
    console.log(user)
    let  passwd = e.target.passwd.value
    let submit = true

    //validar user
    if(user === ""){
        submit = false

        //erro
        let tmp = document.querySelector('input[name="user"]')
        tmp.insertAdjacentHTML('afterend', '<span class="erro">Usuário é obrigatório</span>')
    }

    //validar passwd
    if(passwd === ''){
        submit = false
        //erro
        let tmp = document.querySelector('input[name="passwd"]')
        tmp.insertAdjacentHTML('afterend', '<span class="erro">Senha é obrigatória</span>')
    }

    //se pode ser enviado
    if(!submit){
        e.preventDefault()
        setTimeout(()=>{
            document.querySelectorAll('.erro').forEach(e=>e.remove())
        },2000)
    }
})
