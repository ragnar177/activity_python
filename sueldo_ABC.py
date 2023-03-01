
text_1 = "es momento de determinar el salario de los empleados de los poryectos A, B y C"
print(text_1)
text_2 = "nombre del empleado:"
print(text_2)
name = input()
text_3 = "documento del empleado:"
print(text_3)
numero_documento = input()
text_4 = "proyecto al que pertenece el empleado:"
print(text_4)
unicos_proyectos = 1
unicos_proyectos1 = 3
proyecto_1 = 1

lista_proyectos = {
    'P_A': 20000,
    'P_B': 10000,
    'P_C': 5000
}

salario_A = 30 * (lista_proyectos ["P_A"] * 8)

salario_B = 30 * (lista_proyectos ['P_B'] * 8)

salario_C = (30 * (lista_proyectos ['P_C'] * 8)) + (((lista_proyectos ['P_C'] * (6/100)) + lista_proyectos ['P_C']) * 3)

if proyecto_1 >= unicos_proyectos and proyecto_1 <= unicos_proyectos1:
    print("ut hace parte de un proyecto")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
else:
    print(name, "ut no camella aqui mas bien abrace del parche")

if proyecto_1 == 1:
    print("ut pertenece al proyecto A, por lo tanto su salario es mayor a 1'500.000:", salario_A)

if proyecto_1 == 2:
    print("ut pertenece al proyecto B, por lo tanto su salario es mayor a 1'500.000:", salario_B)

if proyecto_1 == 3:
    print("ut pertenece al proyecto C, por lo tanto su salario es menor a 1'500.000:", salario_C)