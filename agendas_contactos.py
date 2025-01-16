
# el programa es una agenda para guardar contactos, se puede añadir, buscar, mostrar y eliminar contactos
agenda={} #clave=nombre,valor=numero

def mostrar_contactos():
    print("\nNombre".ljust(20), "Numero de Contacto")
    print("-"*35)

    for nombre,numero in agenda.items():
        print(f'{nombre.ljust(20)} {numero}')

while True:
    print("\nOPCIONES:")
    print("1. Añador nuevo contacto")
    print("2. Buscar contactos")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar Contacto")
    print("5. Salir")
    opcion=int(input("Ingrese una opcion(1-5): "))

    if opcion ==1:
        nombre=input("Ingrese el nombre del contacto: ")
        numero=input("Ingrese el numero de contacto: ")
        if nombre in agenda:
            print("El contacto ya existe, intente con otro nombre")
            continue
        agenda[nombre]=numero
        print('El contacto ha sido añadido exitosamente')
    elif opcion ==2:
        nombre_buscar=input("Ingrese el nombre del contacto a buscar: ")
        if nombre_buscar in agenda:
            print(f'Su numero es {agenda[nombre_buscar]}')
        else:
            print("Contacto no encontrado")
    elif opcion ==3:
        if not agenda: #diccionario vacio
            print("No hay contactos guardados")
        else:
            mostrar_contactos()
    elif opcion ==4:
        nombre_eliminar=input("Ingrese el nombre del contacto a eliminar: ")
        if nombre_eliminar in agenda:
            agenda.pop(nombre_eliminar)
            print('El contacto a sifo eliminado exitosamente')
        else:
            print("Contacto no encontrado")
    elif opcion ==5:
        print("¡Hasta Luego!")
        break
    else: # ni 1,2,3,4,5...
        print("Opcion no valida")

if __name__ == "__main__":
    mostrar_contactos()