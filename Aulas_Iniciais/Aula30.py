# Constante = "Variaveis" que nao vao mudar
# muitas condiçoes no mesmo if (ruim)
#     Contagem de complexidade (ruim)

velocidade = 61 # Velocidade atual do carro
local_carro = 101 # local em que o carro esta na estrada

RADAR_1 = 60 # velocidade maxima permitida
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # a distancia onde o radar pega

velocidade_que_o_carro_passou = velocidade > RADAR_1

if velocidade_que_o_carro_passou:
    print('O carro passou da velocidade maxima permitida')

if local_carro <= (LOCAL_1 + RADAR_RANGE) and local_carro >= (LOCAL_1 - RADAR_RANGE) and velocidade_que_o_carro_passou:
    print('Voce foi multado')