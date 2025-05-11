
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
##Tela de início
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

intro='Selecione o programa.'
start='1 - Valores reais\n2 - Nota de alunos\n3 - Média condicional'
linha='.・。.・゜✭・.・✫・゜・。.'

print(linha)
print(intro)
start=int(input(start+'\n'+linha+'\n'))

linha2='*✭˚･ﾟ✧*･ﾟ*✭˚･ﾟ✧*･ﾟ*'

## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
## 1 - valores reais
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

if start == 1:
    print(linha2)
    saida=input('Insira o código de saida que será usado\n(pode ser texto)\n')
    print(linha2)
    lap = 0
    points = 0
    blib = 0
    while True:
        valor=input('Selecione o valor')
        if valor == saida:
            break
        else:
            valor = float(valor)
        lap = lap + 1
        points = points + valor
        if valor > 20:
            blib = blib + 1
    print(f'Valores digitados:\n«────« {lap} »────»')
    print(f'Soma dos valores:\n«────« {points} »────»')
    print(f'Média dos valores:\n«────« {points/lap} »────»')
    print(f'Valores excedentes de 20:\n«────« {blib} »────»')

## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
## 2 - Nota de alunos
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

if start == 2:
    print(linha2)
    saida=input('Insira o código de saida que será usado\n(pode ser texto)\n')
    print(linha2)
    media=5
    lap = 0
    apr = 0
    rpr = 0
    points = 0
    while True:
        valor=input(f'Insira a nota {lap+1}')
        if valor == saida:
            break
        else:
            valor = float(valor)
        lap = lap + 1
        points = points + valor
        if valor < media:
            rpr = rpr + 1
        else:
            apr = apr + 1
    print(f'Notas digitadas:\n«────« {lap} »────»')
    print(f'Alunos aprovados:\n«────« {apr} »────»')
    print(f'Alunos não aprovados:\n«────« {rpr} »────»')

## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
## 3 - Média condicional
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

if start == 3:
    print(linha2)
    saida=input('Insira o código de saida que será usado\n(pode ser texto)\n')
    print(linha2)
    lappar = 0
    lapimpar = 0
    pointspar = 0
    pointsimpar = 0
    while True:
        valor=input('Selecione o valor')
        if valor == saida:
            break
        else:
            valor = int(valor)

        if valor % 2 == 0:

            lappar = lappar + 1
            pointspar = pointspar + valor

        elif valor % 2 == 1:

            lapimpar = lapimpar + 1
            pointsimpar = pointsimpar + valor

        else:
            print('mano que')
    mediapar = pointspar/lappar
    mediaimpar = pointsimpar/lapimpar
    print(f'Média dos números pares:\n«────« {mediapar} »────»')
    print(f'Média dos números ímpares:\n«────« {mediaimpar} »────»')

## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
##             Fim
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

print('\n\n\n「 ✦ Obrigado por usar o meu programa! ✦ 」')