accion_one = "estoy en la entradad del evento"

accion_two = "me estoy registrando"

dato_comparacion = 18 and 19 and 21
edad = 20
boleta = True
prick_zone = 1

if edad == dato_comparacion and boleta:
    print('tu sueldo es superior a 1.500.000')
else:
    print('habrace del parche')

if prick_zone == 1 and edad == dato_comparacion and boleta:
    print('your ticket selct is VIP. enjoy you stay in this space')
    
if prick_zone == 2 and edad >= dato_comparacion and boleta:
    print('your ticket selct is PREFERENCIAL. enjoy you stay in this space')

if prick_zone == 3 and edad >= dato_comparacion and boleta:
    print('your ticket selct is GENERAL. enjoy you stay in this space')

if prick_zone == 4 and edad >= dato_comparacion and boleta:
    print('your ticket selct is BAJA. enjoy you stay in this space')
if prick_zone < 1 or prick_zone > 4:
    print('mire bien que no la ubico')