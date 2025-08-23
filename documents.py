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

print("=-=-=-=-=")
print("EXERCICIO DAS NOTAS")
print("=-=-=-=-=")
contP = 0
contN = 0
contE = 0
contB = 0
contR = 0
contI = 0
passou1 = 0
passou2 = 0
passou3 = 0
maior_nota = float('-inf')
menor_nota = float('inf')
nome_maior_nota = ""
nome_menor_nota = ""

print('Bem Vindo ao Sistema de Avaliação!!')
opção = input('Quer continuar? S/N:').upper()

while opção == 'S':
    nome = input('Informe o seu nome:')
    nota = float(input('Informe sua nota:'))
    while nota < 0 or nota > 10:
        nota = float(input('Informe sua nota entre 0 e 10:'))

    if nota > maior_nota:
        maior_nota = nota
        nome_maior_nota = nome
    if nota < menor_nota:
        menor_nota = nota
        nome_menor_nota = nome

    if nota < 5.0:
        contI = contI + 1
    elif nota >= 5.0 and nota <= 6.9:
         contR = contR + 1
    elif nota >= 7.0 and nota <= 8.9:
        contB = contB + 1
    elif nota >= 9.0 and nota <= 10.0:
        contE = contE + 1

    contN = contN + nota
    contP = contP + 1
    opção = input('Quer continuar? S/N:').upper()

print('Total de participantes:', contP)
media = contN / contP
print('A média das notas é:', media)
percE = (contE / contP) * 100
percB = (contB / contP) * 100
percR = (contR / contP) * 100
percI = (contI / contP) * 100
print('Percentual excelente é {:.2f}%'.format(percE))
print('Percentual bom é {:.2f}%'.format(percB))
print('Percentual regular é {:.2f}%'.format(percR))
print('Percentual insatisfatório é {:.2f}%'.format(percI))
print('{} teve maior nota: {:.2f}'.format(nome_maior_nota, maior_nota))
print('{} teve menor nota: {:.2f}'.format(nome_menor_nota, menor_nota))
acima_media = ((contE + contB + contR)/contP)*100
print('{}% das notas estão acima da média'.format(acima_media))

print("=-=-=-=-=")
print("CALCULAR AREA DE FIGURAS")
print("=-=-=-=-=")

def area_quadrado():
    lado = float(input("Digite o valor do lado do quadrado: "))
    return lado ** 2

def area_retangulo():
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    return base * altura

def area_triangulo():
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    return (base * altura) / 2

def area_circulo():
    raio = float(input("Digite o raio do círculo: "))
    return math.pi * raio ** 2

def area_trapezio():
    base_maior = float(input("Digite a base maior do trapézio: "))
    base_menor = float(input("Digite a base menor do trapézio: "))
    altura = float(input("Digite a altura do trapézio: "))
    return ((base_maior + base_menor) * altura) / 2

def menu():
    print("\n=== Calculadora de Áreas ===")
    print("1. Quadrado")
    print("2. Retângulo")
    print("3. Triângulo")
    print("4. Círculo")
    print("5. Trapézio")
    print("0. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção (0-5): ")

        if escolha == '1':
            area = area_quadrado()
            print(f"Área do quadrado: {area:.2f}")
        elif escolha == '2':
            area = area_retangulo()
            print(f"Área do retângulo: {area:.2f}")
        elif escolha == '3':
            area = area_triangulo()
            print(f"Área do triângulo: {area:.2f}")
        elif escolha == '4':
            area = area_circulo()
            print(f"Área do círculo: {area:.2f}")
        elif escolha == '5':
            area = area_trapezio()
            print(f"Área do trapézio: {area:.2f}")
        elif escolha == '0':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if _name_ == "_main_":
    main()

print("=-=-=-=-=")
print("USO DE DICIONARIOS")
print("=-=-=-=-=")

'''
DICIONÁRIOS são Estruturas de Dados Heterogêneas
capazes de armazenar mais de um tipo de dado dinamicamente
'''
#Usar dicionários em Python é simples:
dicionário = {"nome":"joão","nota":"10"}
print(dicionário)
#Para mudar as informações de dentro:
dicionário["nome"] = "Arthur"
print(dicionário)
#Acessando informações dentro do dicionário:
Cep = {"Rua":"Clinton","Bairro":"Sengés","Número":"452"}
#você pode optar pelo método get:
print(Cep.get("Rua"))
#Você pode também optar por este método:
nametag = "Rua"
if nametag in Cep:
    casa = Cep[nametag]
    print(casa)
#Para verificar se um item existe e mostrar na tela:
for item in dicionário:
    if dicionário[item] == "Arthur":
        print("Arthur está no dicionário")
    for chave in dicionário:
        print(f"{chave}:{dicionário[chave]}")   
#Você também pode optar por utilizar a função values() e items():
lista = {"Alimento":"Arroz","Preço":"2,5"}
for item in lista.values():
    if item == "Arroz":
        print("Arroz está na lista")
        for valor in lista.items():
            print(f"{valor}")

print("=-=-=-=-=")
print("TESTES COM LOOP")
print("=-=-=-=-=")

while True:
   try:
      x = int(input("Informe valor:"))
      print("Você digitou:",x)
   
   except ValueError:
       print("inválido")

print("=-=-=-=-=")
print("EXERCICIO DISTANCIA EUCLIDIANA")
print("=-=-=-=-=")

def gerar_matriz():
    matrizA = []
    matrizB = []
    for i in range(10):
        listaA = []
        for j in range(10):
            listaA.append(random.randint(0, 1))
        matrizA.append(listaA)
    for m in range(10):
        listaB = []
        for n in range(10):
            listaB.append(random.randint(0, 1))
        matrizB.append(listaB)
    return matrizA, matrizB

matrizA, matrizB = gerar_matriz()

print('MatrizA:')
for i in matrizA:
    print(i)

print('MatrizB:')
for m in matrizB:
    print(m)

#Calcular para matrizA:
noroeste = 0
norte = 0
oeste = 0
for i in range(10):
    for j in range(1, 10):
        if matrizA[i][j - 1] == 0 and matrizA[i][j] == 1:
            oeste += 1
for i in range(1, 10):
    for j in range(1, 10):
        if matrizA[i - 1][j - 1] == 0 and matrizA[i][j] == 1:
            noroeste += 1
for i in range(1, 10):
    for j in range(10):
        if matrizA[i - 1][j] == 0 and matrizA[i][j] == 1:
            norte += 1

#Calcular para matrizB:
noroeste2 = 0
norte2 = 0
oeste2 = 0
for m in range(10):
    for n in range(1, 10):
        if matrizB[m][n - 1] == 0 and matrizB[m][n] == 1:
            oeste2 += 1
for m in range(1, 10):
    for n in range(1, 10):
        if matrizB[m - 1][n - 1] == 0 and matrizB[m][n] == 1:
            noroeste2 += 1
for m in range(1, 10):
    for n in range(10):
        if matrizB[m - 1][n] == 0 and matrizB[m][n] == 1:
            norte2 += 1

#Calcular distancia euclidiana:
distancia_euclidiana = math.sqrt((oeste - oeste2)*2 + (noroeste - noroeste2)2 + (norte - norte2)*2)

#Imprimir Resultados:

print('Para a matrizA:')
print('Transicoes oeste:',oeste)
print('Transicoes noroeste:',noroeste)
print('Transicoes norte:',norte)

print('Para a matrizB:')
print('Transicoes oeste2:',oeste2)
print('Transicoes noroeste2:',noroeste2)
print('Transicoes norte2:',norte2)

print(f"Distância Euclidiana: {distancia_euclidiana}")

print("=-=-=-=-=")
print("EXERCICIO DETETIVE")
print("=-=-=-=-=")

matriz = []
M = int(input('Informe tamanho para linha:'))
N = int(input('Informe tamanho para Coluna:'))

for i in range(M):
    lista = []
    for j in range(N):
        lista.append(0)
    matriz.append(lista)

A = int(input('Informe localização do agente em relação a linha (0 a {}):'.format(M-1)))
while A < 0 or A >= M:
    A = int(input('Localização inválida. Informe localização do agente em relação a linha (0 a {}):'.format(M-1)))

B = int(input('Informe localização do agente em relação a coluna (0 a {}):'.format(N-1)))
while B < 0 or B >= N:
    B = int(input('Localização inválida. Informe localização do agente em relação a coluna (0 a {}):'.format(N-1)))

C = int(input('Informe localização do procurado em relação a linha (0 a {}):'.format(M-1)))
while C < 0 or C >= M or (A == C and B == int(input('Informe localização do procurado em relação a coluna (0 a {}):'.format(N-1))) == B):
    if A == C and B == int(input('Localização do procurado em relação a coluna (0 a {}):'.format(N-1))) == B:
        print("A localização do procurado não pode ser igual a do agente")
    else:
        print("Localização inválida")
    C = int(input('Informe localização do procurado em relação a linha (0 a {}):'.format(M-1)))

D = int(input('Informe localização do procurado em relação a coluna (0 a {}):'.format(N-1)))
while D < 0 or D >= N or (A == C and B == D):
    if A == C and B == D:
        print("A localização do procurado não pode ser igual a do agente")
    else:
        print("Localização inválida")
    D = int(input('Informe localização do procurado em relação a coluna (0 a {}):'.format(N-1)))

matriz[A][B] = 1
matriz[C][D] = 2

print("Matriz:")
for linha in matriz:
    print(linha)

distancia = max(abs(A-C), abs(B-D))
print("A distância entre o agente e o procurado é:", distancia)
