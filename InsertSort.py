def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]        # Elemento actual a insertar
        j = i - 1

        # Mueve los elementos mayores que 'key' una posición hacia adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Inserta 'key' en la posición correcta
    return arr
