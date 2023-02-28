
text_1 = "es momento de determinar el salario de los empleados de los poryectos A, B y C"
print(text_1)

text_2 = "nombre del empleado:"
print(text_2)
name = "andres salguero"
print(name)
text_3 = "documento del empleado:"
print(text_3)
numero_documento = 1000537353
print(numero_documento)
text_4 = "proyecto al que pertenece el empleado:"
print(text_4)
unicos_proyectos = 1 and 2 and 3
proyecto_1 = 3

lista_proyectos = {
    'P_A': 20000,
    'P_B': 10000,
    'P_C': 5000
}

salario_A = 30 * (lista_proyectos ["P_A"] * 8)

salario_B = 30 * (lista_proyectos ['P_B'] * 8)

salario_C = (30 * (lista_proyectos ['P_C'] * 8)) + (((lista_proyectos ['P_C'] * (6/100)) + lista_proyectos ['P_C']) * 3)

if proyecto_1 == unicos_proyectos:
    print("ut hace parte de un proyecto")
else:
    print("ut no camella aqui mas bien abrace del parche")

if proyecto_1 == 1:
    print("ut pertenece al proyecto A, por lo tanto su sueldo es de:", salario_A)

if proyecto_1 == 2:
    print("ut pertenece al proyecto B, por lo tanto su sueldo es de:", salario_B)

if proyecto_1 == 3:
    print("ut pertenece al proyecto C, por lo tanto su sueldo es de:", salario_C)