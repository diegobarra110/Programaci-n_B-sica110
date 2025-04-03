def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    num = int(input("Introduce un número: "))
    
    if num < 0:
        print("Error, pruebe con un número positivo")
    else:
        print(f"El factorial de {num} es {factorial(num)}")

if __name__ == "__main__":
    main()
