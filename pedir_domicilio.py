lista = {
    "pizza x1": 50000,
    "hamburguesa x3": 30000,
    "gaseosa x1": 8500
}

print(lista)


total = lista ["pizza x1"] + lista ["hamburguesa x3"] + lista ["gaseosa x1"]
print("valor total del pedido", total)

propina = total * (5/100)
suma = total + propina
print("propina", propina)
print("total de la cuenta", suma)