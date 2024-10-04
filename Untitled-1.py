def suma_numeros_pares(N):
    suma = 0
    numero_par = 0

    for i in range(N):
        suma += numero_par
        numero_par += 2  # Los números pares aumentan de 2 en 2
    
    return suma

# Ejemplo de uso:
N = int(input("Ingresa el valor de N: "))
resultado = suma_numeros_pares(N)
print(f"La suma de los primeros {N} números pares es: {resultado}")
