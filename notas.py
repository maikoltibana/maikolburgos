
estudiantes = [
    {"Nombre" : "Andres", "Notas": [3.0, 4.5, 4.0]},
    {"Nombre" : "Maria", "Notas": [4.0, 5.0, 3.5]},
    {"Nombre" : "Fabio", "Notas": [3.6, 4.2, 3.5]},
]
print("--- Datos cargados ---")
print(f"Total de estudiantes: {len(estudiantes)}")

def calcular_promedio(lista_notas):
        if len(lista_notas) == 0:
            return 0

    suma = 0
    for nota in lista_notas:
        suma += nota

    promedio = suma / len(lista_notas)


print("Prueba promedio Maria", calcular_promedio(estudiantes[1]["Notas"]))