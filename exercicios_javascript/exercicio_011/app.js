/* ----------------------------------------------------------------------------

Exercício: 011
Enunciado:
    A grelha inicial contém dezasseis imgs sem souce.
    Quando clicamos numa das imgs, vamos apresentar o símbolo X (imagem)
    No clique seguinte, que só pode acontecer numa img que não tenha símbolo,
    vamos apresentar o símbolo 'O'.
---------------------------------------------------------------------------- */
let x = true
let block = []
block.length = 16
for (let i = 1; i <= 16; i++) {
    document.querySelector(`#img${i}`).addEventListener('click', () => {
        if (!block[i]) {
            if (x) {
                document.querySelector(`#img${i}`).setAttribute('src', 'x.png')
                x = false
                block[i] = true
            } else {
                document.querySelector(`#img${i}`).setAttribute('src', 'o.png')
                x = true
                block[i] = true
            }
        }
    })
}