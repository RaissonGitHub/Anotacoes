# Comandos git

## Configurar usuario

* `git config --global user.name "nome_do_usuario"`

## Configurar email do usuario

* `git config --global user.email "email_do_usuario"`

## Saber o diretorio atual

* `pwd`

## Mudar diretorio

* `cd local_do_diretorio`

* `cd ..` => muda para o diretorio anterior na hierarquia

## Limpar tela

* `clear`

* `Ctrl + l` => atalho

## Criar um diretorio

* `mdkir nome_do_diretorio`

## Visualisar o conteudo do diretorio

* `ls`

* `ls -l` => para infomacoes completas

## Inicializar repositorio git

* `git init`

* `git init .` => para reforçar que seja o diretorio atual

## Verificar o estado do git

* `git status`

## Adicionar um arquivo para a condicao rastreavel staging area 

* `git add nome_do_arquivo`

* `git add *` ou `git add .` => para todos os arquivos

* `git add *.extensao`=> para todos os arquivos de uma extensao especifica

## Remover um arquivo da condicao rastreavel

* `git rm --cached nome_arquivo`

## Adicionar as alteracoes feitas

* `git commit`

* `git commit -m "Mensagem"` => Coloca uma mensagem descritiva no commit

## Verificar historico de alteracoes e os autores, data, e descricao delas

* `git log`

* `git log nome_arquivo` => para verificar de um arquivo especifico

* `git log --oneline` => exibir de forma resumida

* `git log --all`=> exibir todo historico

## Fazer conexao com o github

* `git remote add origin git https://<seu_token>@github.com/<seu_usuário>/<seu_repositório>.git`

* `git remote set-url origin https://<seu_token>@github.com/<seu_usuário>/<seu_repositório>.git`

## Verificar conexao atual 

* `git remote -v`

## Enviar para o repositorio remoto

/# Apos commitar

* `git push`

* `git push -u origin master` => define a branch master como local padrao de commits

* `git push origin nome_ramificacao` => para outra branch

## Clonar repositorio remoto

* `git clone URL_do_repositorio_github`

## Renomear repositorio remoto

* `git remote rename nome_antigo novo_nome`

## Visualizar alteracoes realizadas

* `git show nome_do_commit`

* `git show` => lista as alteracoes do ultimo commit

/# Em vermelho está o que foi removido

/# Em verde está o que foi adicionado

/# Em azul está uma descricao

ex:

@@ -1 +1,3 @@

-1 => primeira linha retirada

+1,3 => tres linhas editadas a partir da primeira

/# - => retirado

/# + => adicionado

/# ,numero => numero de linhas a partir do ponto que foram alteradas

## Renomear um arquivo 

* `mv nome_atual novo_nome`

## Revisar/comparar alteracoes atuais

* `git diff`

* `git diff nome_arquivo` => para um arquivo especifico

* `git diff --staged` => para arquivos na staging area (add) mas nao commitados

## Visualisar conteudo

* `cat nome_arquivo`

## Remover arquivo

* `git rm nome_arquivo`

## Excluir tudo

/# Saia do diretorio

* `rm -rf nome_do_diretorio`

## Verificar arquivos excluidos

* `git log --diff-filter=D --sumary`

## Mudar de versao

* `git checkout nome_do_commit`

## Criar uma ramificacao branch

* `git checkout -b nome_da_ramificacao`

## Listar ramificacoes 

* `git branch`

* `git branch -r` => para ramificaoes remotas

## Mudar de mamificacao

* `git checkout nome_da_ramificacao`

## Incorporar ramificacoes

* `git merge nome_da_ramificacao`

## Restaurar arquivo excluido

* `git checkout nome_do_commit~1 nome_arquivo`

## Reverter um commit

* `git revert nome_do_commit`

## Ajuda do git

* `git help`

* `git help comando` => para saber mais do comando

* `git help -a` => listar subcomandos e guias de conceitos












