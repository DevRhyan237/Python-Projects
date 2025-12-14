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
