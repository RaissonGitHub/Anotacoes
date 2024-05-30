"""
 Ambientes virtuais em Python (venv)
 Um ambiente virtual carrega toda a sua instalação
 do Python para uma pasta no caminho escolhido.
 Ao ativar um ambiente virtual, a instalação do 
 ambiente virtual será usada.
 venv é o módulo que vamos usar para 
 criar ambientes virtuais.
 Você pode dar o nome que preferir para um
 ambiente virtual, mas os mais comuns são:
 venv env .venv .env
"""

# COMO CRIAR UMA VENV
# No powershell
# python -m venv venv

# Ativar a venv
# .\venv\Scripts\activate
# ou em mac/linux
# source venv/bin/activate

# Instalar algum pacote
# pip install nome_pacote

# Desistalar algum pacote
# pip uninstall nome_pacote

# Saber pacotes instalados
# pip freeze

# Arquivo contendo os pacotes e suas versões >>> requirements.txt 
# Gerar o arquivo requirements.txt
# pip freeze > requirements.txt

# Para executar a instalacao de todos os pacotes de requirements.txt use
# pip install -r requirements.txt