"""
CONSTANTE = "variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
multado_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar_1 :
    print('Velocidae carro passou do radar 1')

# \ indica quebra de linha
if multado_1 and \
    vel_carro_pass_radar_1 :
    print('carro multado em radar 1')