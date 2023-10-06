
num_experimentos = int(input("Ingrese el número de experimentos que ha realizado: "))

# Inicializar listas para cada experimento (A, B, C, ...)
listas_experimentos = []

# Crear una lista para cada experimento y almacenarla en listas_experimentos
for i in range(num_experimentos):
    input_str = input(f"Ingrese los valores de las mediciones para el experimento {chr(ord('A') + i)} separados por espacios: ")
    datos_experimento = [int(num) for num in input_str.split()]
    listas_experimentos.append(datos_experimento)

for i in range(num_experimentos):
    print("Los datos del expermento", chr(ord('A') + i), "son:", listas_experimentos[i])

#Añamos los valores de los parametros
k=len(listas_experimentos[0])
N=k*



