def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambio
                swapped = True
        if not swapped:
            break  
    return arr

# Solicitar al usuario 10 números
nums = []
print("Ingrese 10 números a ordenar:")
for _ in range(10):
    num = int(input("Ingrese un número: "))
    nums.append(num)

sorted_nums = bubble_sort(nums)
print("Lista ordenada:", sorted_nums)