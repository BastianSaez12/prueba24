#bienvenido a mi calculadora basica por Bastian Saez :)

print("Bienvenido usuario")

while True:
    resultado = int(input("que operacion desea hacer? Suma = 1, Resta = 2, Divison = 3, Multiplicar = 4 y Salir = 5: "))
    if resultado == 1:
        n1 = int(input(print(f"ingrese el primer digito: ")))
        n2 = int(input(print(f"ingrese el segundo digito: ")))
        print(f"la suma es un total de: {n1 + n2}")
    elif resultado == 2:
        n1 = int(input(print(f"ingrese el primer digito: ")))
        n2 = int(input(print(f"ingrese el segundo digito: ")))
        print(f"la resta es un total de: {n1 - n2}")
    elif resultado == 3:
        n1 = int(input(print(f"ingrese el primer digito: ")))
        n2 = int(input(print(f"ingrese el segundo digito: ")))
        print(f"la suma es un total de: {n1 / n2}")
    elif resultado == 4:
        n1 = int(input(print(f"ingrese el primer digito: ")))
        n2 = int(input(print(f"ingrese el segundo digito: ")))
        print(f"la suma es un total de: {n1 * n2}")
    elif resultado == 5:
        print("Saliendo... vuelva pronto")
        break
    else:
        print("Opcion invalida, intente otra vez")

