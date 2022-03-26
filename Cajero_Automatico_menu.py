from random import randrange
saldo = randrange (0, 500000)
print("****Bienvenido(a) al Cajero Automatico***")

while True:
    print("\nOperaciones disponibles")
    print("\n1 Saldo")
    print("2. Retiro")
    print("3. Deposito")
    print("0. Salir")

    opcion = int(input("Elija la operacion a realizar entre 0 y 3.  "))
    if opcion in range(4):
        if opcion == 1:
            print("Su saldo es: ", saldo)
        elif opcion == 2:
            monto = int(input("Indique el monto a retirar "))
            if monto > saldo:
                print("Saldo insuficiente")
            else:
                saldo = saldo - monto
                print("Operacion Exitosa")
                print("Su saldo Actual es: ", saldo)
        elif opcion == 3:
            monto = int(input("Indique el monto a depositar "))
            saldo = saldo + monto
            print("Su saldo actuial es: ", saldo)
        else:
            print("Hata Luego")
            break
    else:
        print("La opcion seleccionada no esta disponible ")
