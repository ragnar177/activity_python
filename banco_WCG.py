"""
#no grafico
inicio
1. ingresar sus datos prsonales
2. ingrese moneda origen
3. si esta es existente segir con el proceso
4. ingresar moneda destino 
5. si esta es existente segir con el proceso
6. mostrar el pocentaje de intercambio para confirmar el cambio 
7. si si lo desea realizar confirmar, si no cancelar

"""

#caso number 1

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
list_dolar = {
    'usd': 5000,
    'euro': 1,
    'cod': 5000,
    'yen': 150,
    'sol': 4
}

dolar_1 = ((how_moch * list_dolar['cod']) - ((list_dolar['cod'] * how_moch) * (1/100)))

dolar_2 = ((how_moch * list_dolar['euro']) - ((list_dolar['euro'] * how_moch) * (1/100)))

dolar_3 = ((how_moch * list_dolar['yen']) - ((list_dolar['yen'] * how_moch) * (1/100)))

dolar_4 = ((how_moch * list_dolar['sol']) - ((list_dolar['sol'] * how_moch) * (1/100)))




if currency_origin == list_1['usd']  or currency_origin == list_1['euro'] or currency_origin == list_1['cod'] or currency_origin == list_1['yen'] or currency_origin == list_1['sol'] and currency_destination == list_1['usd']  or currency_destination == list_1['euro'] or currency_destination == list_1['cod'] or currency_destination == list_1['yen'] or currency_destination == list_1['sol']:
    print("your origin currency and you destination currency is true")
else:
    print("your divisa is false")
if currency_destination == list_1['cod']:
    print("este es su nuevo valos en pesos colombianos", dolar_1)
if currency_destination == list_1['euro']:
    print("este es su nuevo valos en pesos euros", dolar_2)
if currency_destination == list_1['yen']:
    print("este es su nuevo valos en pesos yenes", dolar_3)
if currency_destination == list_1['sol']:
    print("este es su nuevo valos en pesos soles", dolar_4)




