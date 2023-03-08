

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
    'usd': 1,
    'euro': 1,
    'cod': 5000,
    'yen': 150,
    'sol': 4
}

porcentaje_divisa = ((list_dolar['cod'] * how_moch) * (1/100))

dolar_1 = ((how_moch * list_dolar['cod']) - ((list_dolar['cod'] * how_moch) * (1/100)))

dolar_2 = ((how_moch * list_dolar['euro']) - ((list_dolar['euro'] * how_moch) * (1/100)))

dolar_3 = ((how_moch * list_dolar['yen']) - ((list_dolar['yen'] * how_moch) * (1/100)))

dolar_4 = ((how_moch * list_dolar['sol']) - ((list_dolar['sol'] * how_moch) * (1/100)))

list_euro = {
    'usd': 1,
    'euro': 1,
    'cod': 5000,
    'yen': 150,
    'sol': 4
}








if currency_origin == list_1['usd']  or currency_origin == list_1['euro'] or currency_origin == list_1['cod'] or currency_origin == list_1['yen'] or currency_origin == list_1['sol'] and currency_destination == list_1['usd']  or currency_destination == list_1['euro'] or currency_destination == list_1['cod'] or currency_destination == list_1['yen'] or currency_destination == list_1['sol']:
    print("your origin currency and you destination currency is true")
else:
    print("your divisa is false")
if currency_destination == list_1['cod']:
    print("este es su nuevo valos en pesos colombianos", dolar_1, ", este es el porcentaje a descontar por su camio de moneda", porcentaje_divisa)
if currency_destination == list_1['euro']:
    print("este es su nuevo valos en pesos euros", dolar_2)
if currency_destination == list_1['yen']:
    print("este es su nuevo valos en pesos yenes", dolar_3)
if currency_destination == list_1['sol']:
    print("este es su nuevo valos en pesos soles", dolar_4)




