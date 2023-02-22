articulos = {  
    "zapatos": 350000,
    "tenis": 280000,
    "camisetas": 175000,
    "jeans": 200000
}
#precio total y promedio de ventas 
resultado = articulos ["zapatos"] + articulos ["tenis"] + articulos["camisetas"] + articulos ["jeans"]
promedio = resultado / 4
print(articulos)
print("precio total", resultado)
print("el promedio de las ventas es de:", promedio)

#aumento del '6.2%' de los jeasn, nuevo precio:
aumento = 6.2
suma = articulos ["jeans"] * (aumento / 100)
resultado1 = articulos ["jeans"] + suma
print("aumento del '6.2%' de los jeasn, nuevo precio:", resultado1)

#descuento del '0.8%' para los zapatos, nuevo precio: 347200.0
aumento = 0.8
resta = articulos ["zapatos"] * (aumento / 100)
resultado2 = articulos ["zapatos"] - resta
print("descuento del '0.8%' para los zapatos, nuevo precio:", resultado2)