# Conversión de temperaturas
# Descripción: Convertir grados Celsius a Fahrenheit o viceversa. El usuario debe ingresar el
# tipo de conversión y la temperatura.

temperatura = float(input("Ingrese la temperatura: "))
tipo_conversión = input("Ingrese el tipo de conversión (C/F): ")

if tipo_conversión == "C":
    temperatura_fahrenheit = (temperatura * 9/5) + 32
    print(f"{temperatura} grados Celsius son {temperatura_fahrenheit} grados Fahrenheit")
else:
    temperatura_celsius = (temperatura - 32) * 5/9
    print(f"{temperatura} grados Fahrenheit son {temperatura_celsius} grados Celsius")