gastos = []

def menu_principal():
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE GASTOS ---")
        print("1. Registrar Gasto")
        print("2. Ver Resumen Total")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            mostrar_resumen()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, reintente.")
def registrar_gasto():
    print("\n--- Registro de Nuevo Gasto ---")
    placa = input("Placa del vehículo: ")
    concepto = input("Concepto (Ej: Gasolina, Peaje): ")
    try:
        valor = float(input("Valor: "))
        
        nuevo_gasto = {
            "Placa": placa,
            "Concepto": concepto,
            "Valor": valor
        }
        

        gastos.append(nuevo_gasto)
        print("Gasto registrado con éxito.")
    except ValueError:
        print("Error: El valor debe ser un número.")

def mostrar_resumen():
    if not gastos:
        print("\nNo hay gastos registrados aún.")
        return

    total_acumulado = 0
    print("\n--- Resumen de Gastos ---")
    
    for gasto in gastos:
        total_acumulado += gasto["Valor"]
        print(f"Vehículo: {gasto['Placa']} | {gasto['Concepto']}: ${gasto['Valor']}")
    
    print("-" * 30)
    print(f"GASTO TOTAL ACUMULADO: ${total_acumulado}")

if __name__ == "__main__":
    menu_principal()
