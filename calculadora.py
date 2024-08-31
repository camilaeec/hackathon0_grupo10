import math

def calculadora():
    while True:
        print("\n--- Calculadora Básica ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("C. Salir")
        
        opcion = input("Selecciona una opción (1-4 o C para salir): ")

        if opcion == '1':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")


























calculadora()
