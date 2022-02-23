# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# print("Número digitado:",chute, sep='') # exibição dos dados

import random

def jogar():

    numero_secreto = random.randrange(1,101) # numero_secreto = round(random.random() * 100) # 0.0 - 1.0
    total_de_tentativas = 0
    pontos = 1000 # total

    print('******************')
    print("Bem vindo ao jogo!")
    print('******************\n')

    print('Níveis de dificuldade!\n')
    print('(1) Fácil (2) Médio (3) Difícil\n',numero_secreto)
    nivel = int(input('Nível: '))
    if(nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    print('')

    # while(rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1): # range(start, stop, [step])

        # print(f"Tentativa {rodada} de {total_de_tentativas}!")
        print("Tentativa {} de {}!".format(rodada, total_de_tentativas)) # String interpolation

        chute_str = input("Digite um número entre 0 e 100: ") # input de dados
        chute = int(chute_str) # typecast

        if chute < 1 or chute > 100: # verificar o valor inputado e pular a rodada
            print('Você deve inserir um valor entre 0 e 100. Rodada perdida OTÁRIO!!')
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if maior:
                print('Você errou! O seu chute foi maior do que o número secreto.')
            elif menor:
                print('Você errou! O seu chute foi menor do que o número secreto.')
            # calcular a pontuação após cada rodada errada
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('Fim do jogo')

if(__name__ == '__main__'):
    jogar()



# syntax sugar - simplifica algo que seria trabalhoso
'''numero1 = 10
numero2 = "20"
produto = numero1 * numero2
print(produto)'''

# formatação de strings
# https://docs.python.org/3/library/string.html#formatexamples
'''print('R${} por cabeça'.format(45.99))
print('R${:.2f} por cabeça'.format(45))
print('R${:10.2f} por cabeça'.format(45543))
print('R${:09.2f} por cabeça'.format(45543))
print('Exibindo valores em ordens diferentes, como: {1} e {0}'.format(45, 33))
print('Data {:02d}/{:02d}/{:4d}'.format(15,4,1999))

f-strings ou formatted string literals
nome = 'Mathues'
print(f'Meu nome é {nome}')
print(f'Meu nome é {nome.lower()}')'''

'''
float division
>>>  2 / 2
1.0
O operador / sempre traz um float, mesmo se não for necessário,
por isso ele também é chamado de float division:

integer division
>>>  3 // 2
1
O operador // também é chamado integer division e sempre devolve o valor inteiro (sem arredondar).
'''