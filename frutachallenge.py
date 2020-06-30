while True:
    print("manzana = 1, pina = 2, fresa = 3, 0= salir")
    fruta = int(input("ingrese la fruta que desea (0 salir):"))
    cantidad = int(input("ingrese la cantidad que desea:"))
    total = 0
    if fruta == 0:
        break
    elif fruta == 1:
        total = cantidad*1.0
    elif fruta == 2:
        total = cantidad*3.0
    elif fruta == 3:
        total = cantidad * (2 / 5)
         
    print(f"total: ${total}")

