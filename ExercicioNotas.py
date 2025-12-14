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
