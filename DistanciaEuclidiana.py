import math

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
