Valor = 0
print("Bienvenido al conversor de grados")
val = int(float(input("1.Fahrenheit a grados centígrados o 2.grados centígrados a Fahrenheit -Introducir solo el numero de la opcion-")))

while True:
    if val == 1:
         print("Ha escogido la primera opción")
         fahrenheit = float(input("Introduzca sus grados Fahrenheit: "))
         celsius = (fahrenheit - 32) / 1.8
         print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados centígrados.")
    elif val == 2:
         print("Ha escogido la segunda opción")
         celsius = float(input("Introduzca sus grados centígrados: "))
         fahrenheit = (celsius * 1.8) + 32
         print(f"{celsius} grados centígrados son {fahrenheit:.2f} grados Fahrenheit.")
    else:
         print("La medida no es valida")
         break