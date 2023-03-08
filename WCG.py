print("welcome")
print("please add the next data")

print("name")
name = str (input())

print("add your document")
document = int (input())

print("add origin currency")
currency_origin = str (input())

print("add destini currency")
currency_destination = str (input())

print("how much money you do want to changer")
how_moch = int (input())

list_1 = {
    'usd': 'usd',
    'euro': 'euro',
    'cod': 'cod',
    'yen': 'yen',
    'sol': 'sol'
}

list_cod = {
    'usd': 4800,
    'euro': 5100,
    'cod': 5000,
    'yen': 35,
    'sol': 1300
}

porcentaje_divisa_usd = ((list_cod['cod'] * how_moch) * (1/100))
cod_usd = ((how_moch * list_cod['usd']) - ((list_cod['usd'] * how_moch) * (12/100)))

porcentaje_divisa_yen = ((list_cod['yen'] * how_moch) * (1/100))
cod_yen = ((how_moch * list_cod['yen']) - ((list_cod['yen'] * how_moch) * (4.6/100)))

porcentaje_divisa_euro = ((list_cod['euro'] * how_moch) * (1/100))
cod_euro = ((how_moch * list_cod['euro']) - ((list_cod['euro'] * how_moch) * (10/100)))

porcentaje_divisa_sol = ((list_cod['sol'] * how_moch) * (1/100))
cod_sol = ((how_moch * list_cod['sol']) - ((list_cod['sol'] * how_moch) * (7/100)))


if currency_origin == list_1['usd']  or currency_origin == list_1['euro'] or currency_origin == list_1['cod'] or currency_origin == list_1['yen'] or currency_origin == list_1['sol'] and currency_destination == list_1['cod']:
    print("your origin currency and you destination currency is true")
else:
    print("your divisa is false")
if currency_destination == list_1['cod'] and currency_origin == list_1['usd']:
    print("este es su nuevo valor en pesos colombianos", cod_usd, ", este es el porcentaje descontado por su intermercion, tener en cuentas que este porcentaje es superior a 10% asi que se decontaran:", porcentaje_divisa_usd)
if currency_destination == list_1['cod'] and currency_origin == list_1['yen']:
    print("este es su nuevo valor en pesos colombianos", cod_yen, ", este es el porcentaje descontado por su intermercion, :", porcentaje_divisa_yen)
if currency_destination == list_1['cod'] and currency_origin == list_1['euro']:
    print("este es su nuevo valor en pesos colombianos", cod_euro, ", este es el porcentaje descontado por su intermercion, tener en cuentas que este porcentaje es superior a 10% asi que se decontaran:", porcentaje_divisa_euro)
if currency_destination == list_1['cod'] and currency_origin == list_1['sol']:
    print("este es su nuevo valor en pesos colombianos", cod_sol, ", este es el porcentaje descontado por su intermercion:", porcentaje_divisa_sol)