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
