velocidade = 61 
local_carro = 90

Radar_1 = 60 
Local_1 = 100 
Radar_range = 1 

if local_carro >= (Local_1 - Radar_range) and \
   local_carro <= (Local_1 + Radar_range) and \
   velocidade > Radar_1:
    print('Você está no radar 1')