import math
import time

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print('=-=-=-='*2)
print('CALCULADORA DE NUMEROS PRIMOS:')
print('=-=-=-='*2)

def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Digite um número: "))
if primo(n):
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")

print('Programa Finalizado! Volte Sempre!')
