tabuada = int(input('Qual tabuada quer começar:'))
s1 = int(input('Qual numero quer terminar:'))
for i in range(1, s1 + 1, 1):
    print('{} X {} = {}'.format(tabuada, i, tabuada * i))
