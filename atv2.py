

matriz = []
for i in range(3):
    linha = []
    for j in range(4):
        elemento = int(input(f'unidades vendidas em cada período ({i+1},{j+1}): '))
        if elemento < 0:
            print('Não permitido numeros negativos, tente novamente')
            elemento = int(input(f'unidades vendidas em cada período ({i + 1},{j + 1}): '))
        linha.append(elemento)
    matriz.append(linha)


print('\n Matriz Inserida:')
for linha in matriz:
    print(linha)

tc = sum(matriz[0])
ta = sum(matriz[1])
tb = sum(matriz[2])
print(f'total de vendas das camisetas: {tc}')
print(f'total de vendas das canecas: {ta}')
print(f'total de vendas dos bonés: {tb}')

v1 = (matriz[0,0] + matriz[1,0] + matriz[2,0])
v2 = (matriz[0,1] + matriz[1,1] + matriz[2,1])
v3 = (matriz[0,2] + matriz[1,2] + matriz[2,2])
v4 = (matriz[0,3] + matriz[1,3] + matriz[2,3])
print(f'total de vendas qui manha: {v1}')
print(f'total de vendas qui tarde: {v2}')
print(f'total de vendas sex manha: {v3}')
print(f'total de vendas sex tarde: {v4}')

print(f'total de produtos vendidos: {sum(matriz)}')

if tc > ta:
    print('camisetas vendeu mais')
elif ta > tb:
    print('canecas vendeu mais')
elif tb > tc:
    print('bones vendeu mais')