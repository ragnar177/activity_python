#Definimos el valor de cada categoria:
list_cate= {
    "individual": 2500,
    "doble": 4600,
    "familiar": 5200,
}

#Creamos una lista comparativa:
list_cate_1= {
    "individual": "individual",
    "doble": "doble",
    "familiar": "familiar",
}

#Ingreso de datos
print("bienvenido al hotel WC")
print("ingrese categoria deseada")
categoria = str (input())
print("ingrese cantidad de dias que desea hospedarse")
dias = int(input())

#Operaciones para saber el valor con el IVA agregado
price1 = ((dias * list_cate["individual"]) + ((dias * list_cate["individual"]) * (16/100)))
price2 = ((dias * list_cate["doble"])  + ((dias * list_cate["doble"]) * (16/100)))
price3 = ((dias * list_cate["familiar"]) + ((dias * list_cate["familiar"]) * (16/100)))

#Operacion de descuento
descuento1 = (price1 - ((dias * list_cate["individual"]) * (5/100)))
descuento2 = (price2 - ((dias * list_cate["doble"]) * (9/100)))
descuento3 = (price3 - ((dias * list_cate["familiar"]) * (15/100)))

#Se muestra el total, en caso de que sus datos anteriores sean inexistentes se mostrara otro mensaje 
if categoria == list_cate_1["individual"] or categoria == list_cate_1["doble"] or categoria == list_cate_1["familiar"]:
    print("disfrute su estadia")
else:
    print("estadia inexistente porfavir verifique la categoria deseada")
if list_cate_1["individual"] == categoria: 
    print("has elegido la categoria individual, por lo tanto tu valor a pagar es de:", descuento1)
if list_cate_1["doble"] == categoria: 
    print("has elegido la categoria doble, por lo tanto tu valor a pagar es de:", descuento2)
if list_cate_1["familiar"] == categoria: 
    print("has elegido la categoria familiar, por lo tanto tu valor a pagar es de:", descuento3)
