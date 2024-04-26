def factorial(num):
    resultado = 1
    if num < 0:
        print("Numero negativos NO validos.")
    else:
        for i in range(num, 0, -1):
            resultado *= i
        return resultado

num = int(input())
print(factorial(num))


