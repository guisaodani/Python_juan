#este programa consiste en simular los funcionamiento de movimientos bancarios, como consultar saldo, depositar y retirar dinero

def mostrar_saldo(saldo):
    print(f"Su saldo actual es: {saldo:.2f}")

def depositar():
    monto=float(input("Ingrese el monto a depositar: "))
    if monto <0:
        print("Cantidad no es valida")
        return 0
    else:
        return monto
    
def retirar(saldo):
    monto=float(input("Ingrese el monto a retirar: "))
    if monto > saldo:
        print("Fondos insuficientes")
        return 0
    elif monto < 0:
        print('la cantidad debe ser mayor a cero 0')
        return 0
    else:
        return monto

def menu_principal():
    saldo=0
    en_ejecucion=True
    while en_ejecucion:
        print("\nPROGRAMA BANCARIO")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        opcion=float(input("Ingrese una opcion(1-4): "))
        if opcion==1:
            mostrar_saldo(saldo)
        elif opcion==2:
            saldo+=depositar()
        elif opcion ==3:
            saldo-=retirar(saldo)
        elif opcion == 4:
            en_ejecucion=False
            print('Hasta Luego')
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    menu_principal()