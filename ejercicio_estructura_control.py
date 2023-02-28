
accion_one = "estoy en la entradad del evento"

accion_two = "me estoy registrando"


dato_comparacion = "18" and "19" and "21"
edad = "19"
boleta = True
prick_zone = 1

if edad >=  dato_comparacion and boleta:
    print('que tipo de voleta deseas: VIP = 500USD, PREFERENCIAL = 400USD, GENERAL = 200USD, BAJA = 100USD')
else:
    print('habrace del parche')

if prick_zone == 1 and edad >= dato_comparacion and boleta:
    print('your ticket selct is VIP. enjoy you stay in this space')
    
if prick_zone == 2 and edad >= dato_comparacion and boleta:
    print('your ticket selct is PREFERENCIAL. enjoy you stay in this space')

if prick_zone == 3 and edad >= dato_comparacion and boleta:
    print('your ticket selct is GENERAL. enjoy you stay in this space')

if prick_zone == 4 and edad >= dato_comparacion and boleta:
    print('your ticket selct is BAJA. enjoy you stay in this space')
if prick_zone < 1 or prick_zone > 4:
    print('mire bien que no la ubico')





    
