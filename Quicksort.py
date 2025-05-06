def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Pedir 10 números al usuario sin validaciones
numeros = [int(input(f"Ingrese el número {i+1}/10: ")) for i in range(10)]

# Ordenar e imprimir
ordenados = quicksort(numeros)
print("Lista ordenada:", ordenados)