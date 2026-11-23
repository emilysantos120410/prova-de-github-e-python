c = []

for i in range(5):
    num = int(input(f'digite a quantidade de chamados do dia {i+1}°: '))
    c.append(num)

    if num < 0:
        print('Não permitido numeros negativos, tente novamente')
        num = int(input(f'digite a quantidade de chamados do dia {i + 1}°: '))

print(f'segunda-feira: {1} chamados')
print(f'terça-feira: {2} chamados')
print(f'quarta-feira: {3} chamados')
print(f'quinta-feira: {4} chamados')
print(f'sexta-feira: {5} chamados')

print(f'total de chamados da semana: {sum(c)}')
d = (sum(c))/5
print(f'media diaria de chamados da semana: {d}')
print(f'dia com maior quantidade: {(c.index(max(c))+1)}° dia')
print(f'dias com chamados acima da média: {(c.index(d<c))}')