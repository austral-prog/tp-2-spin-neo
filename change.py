def change():
    expense = 23.75
    money = 100
    vuelto_entero = (money - expense) //1
    vuelto_decimal = ((money - expense) - vuelto_entero)*100
    vuelto_entero_INT = int(vuelto_entero)
    vuelto_decimal_INT = int(vuelto_decimal)
    print("Ingresar gasto:")
    print (f"{expense}")
    print("Dinero recibido")
    print(money)
    print("")
    print ("Vuelto")
    print("")
    print("Pesos:")
    print (f"{vuelto_entero_INT}")
    print("Centavos:")
    print(f"{vuelto_decimal_INT}")
change()