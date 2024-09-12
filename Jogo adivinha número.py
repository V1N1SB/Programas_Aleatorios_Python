import random

# 1º - Preciso definir a dificuldade e gerar a lista aleatório (sem repetir números)
# 2º - Printar na tela em forma de "_" todos os espaços vazios e conforme acertando vai preenchendo
# 3º - Criar um sistema de dicas onde a pessoa tem direito a 3 dicas, e essas dicas vão subtraindo da pontuação final dele
# 4º - Quando for jogar, o programa tem q comprar o número chutado com os números da lista, e se ele tiver perto de algum dizer q está perto
# Ex1: "Tem um número secreto acima desse", "Tem mais de um número secreto acima desse", "Tem um número secreto abaixo desse", "Não tem nenhum número secreto perto desse"
# O sistema de "proximidade" deve funcionar de forma equivalente a quantidade de números, ou seja, quanto maior a quantidade de números maior o raio de proximidade
# 5º - Quando o jogo acabar, sendo o usuário desistindo ou ganhando, o jogo vai mostrar os pontos adiquiridos, e perguntando se ele deseja jogar novamente
# EM DESENVOLVIMENTO 6º - Fazer com crie um arquivo com um "Placar" de pessoas que jogaram, assim criando um ranking de quem foi melhor ou pior, fazer com que continue salvo
def menu_inicial():
    while True:
        op = input('======== MENU INICIAL ========\n1 - Começar o jogo\n2 - Ajuda\n3 - Créditos\n4 - Sair\nDigite sua opção: ')

        match op:
            case '1':
                lista_numeros_aleatorios, dificuldade = dificuldade_e_lista()
                lista_jogo = lista_do_jogo(lista_numeros_aleatorios)
                Jogo(lista_numeros_aleatorios, dificuldade, lista_jogo)
            case '2':
                while True:
                    op2 = input('\n1 - Dificuldade\n2 - Como Jogar\n3 - Dicas\n4 - Voltar\nDigite sua opção: ')
                    match op2:
                        case '1':
                            print('\nFácil == Vão ser gerados 5 números aleatórios de 1 a 25\n'
                                  'Médio == Vão ser gerados 7 números aleatórios de 1 a 50\n'
                                  'Difícil == Vão ser gerados 10 números aleatórios de 1 a 100')
                        case '2':
                            print('\nVocê deve escolher uma dificuldade entre "Fácil", "Médio" e "Difícil".\nApós escolher,'
                                  ' será gerado uma certa quantidade de números para você tentar adivinhar,\nassim que você digitar'
                                  ' um número o sensor de proximidade dirá se está "Perto", "Muito Perto", "Chegando Perto", "Longe", "Muito Longe".\n'
                                  'Assim que você adivinhar todos os números ou desistir, o jogo encerrará e dirá para você os seus pontos recebidos')
                        case '3':
                            print('\nVocê terá direito a 3 dicas por jogo\n'
                                  'Lista de demonstração [2, 5, 7, 12, 13, 15, 20]\n'
                                  'Primeira dica: Irá te mostrar o maior e o menor número da sua lista, nesse exemplo ele mostraria o 2 sendo o menor e o 20 sendo o maior\n'
                                  'Segunda dica:  A segunda dica dirá pra você, de todos os números da lista, quantos deles são Pares, Impares e Primos, nesse exemplo ele mostraria 3 números pares, 4 números impares e 4 números primos\n'
                                  'Terceira dica: A terceira dica vai te mostrar a posição das informações adiquiridas da segunda dica, por exemplo\n'
                                  '["P & Pr", "I & Pr", "I & Pr", "P", "I & Pr", "I", "P"]\n'
                                  'Mostrando exatamente que tipo de número tem em cada casa')
                        case '4':
                            break
                        case _:
                            print('Opção inválida')
            case '3':
                print("\nJogo Feito por Vinicius Piroca de Foice\n"
                      "Jogo Dirigido por Vinicius Cabeça de Cogumelo\n"
                      "Sla mano, foi feito por mim mesmo, Vinicius cabeça de tangerina cheia de gomo\n")
            case '4':
                break

def dificuldade_e_lista():
    lista = []
    while True:
        modo = input('Qual a dificuldade que você deseja jogar? (Fácil(1), Médio(2), Difícil(3) Voltar(4)): ')
        match modo:
            case '1':
                while len(lista) < 5:
                    numero_aleatorio = random.randint(1,25)
                    if numero_aleatorio not in lista:
                        lista.append(numero_aleatorio)
                        lista.sort()
                return lista, 'Facil'
            case '2':
                while len(lista) < 7:
                    numero_aleatorio = random.randint(1,50)
                    if numero_aleatorio not in lista:
                        lista.append(numero_aleatorio)
                        lista.sort()
                return lista, 'Medio'
            case '3':
                while len(lista) < 10:
                    numero_aleatorio = random.randint(1,100)
                    if numero_aleatorio not in lista:
                        lista.append(numero_aleatorio)
                        lista.sort()
                return lista, 'Dificil'
            case '4':
                print('')
                menu_inicial()
            case _:
                print('Selecione uma das opções, 1 = Fácil, 2 = Médio, 3 = Difícil')

def lista_do_jogo(lista):
    lista_branca = []
    for i in lista:
        lista_branca.append("_")
    return lista_branca

def dicas(lista, dica, lista_jogo):
    match dica:
    # Minha ideia pra primeira dica é fazer com que o usuário tenha um campo menor pra adivinhar os números
    # ao invés de ser de 1 a 25, seria por exemplo de 4 a 17, já quem n tem nenhum número maior que 17 e nenhum menor que 4
        case 1:
            maior, menor = max(lista), min(lista)
            print(f'E a sua dica é:\nO maior número da lista é {maior} e o menor número da lista é {menor}')

    # Minha ideia pra essa segunda dica seria dizer pro usuário de todos os números da lista, quantos são pares e ímpares, e se tem algum número primo
        case 2:
            par = 0
            impar = 0
            primo = 0
            for i in lista:
                if i % 2 == 0:
                    par += 1
                else:
                    impar += 1
                #Não faço ideia do porque isso funcionou, mas não vou mexer mais nisso
                e_primo_ou_num_e = True
                for i2 in range(2, int(i ** 0.5) + 1):
                    if i % i2 == 0:
                        e_primo_ou_num_e = False
                        break
                if e_primo_ou_num_e:
                    primo += 1
            print(f'\nNa lista temos extamente {par} números pares, {impar} números impares e {primo} números primos')

    # Minha ideia aqui é ser a dica mais poderosa, então ele vai dizer exatamente a posição dos números impares, pares e primos
    # Pretendo substituir os "_" por letras como "Pr" para primo, "P" para primo e "I" para impar ps: Só Deus sabe como eu vou fazer isso
        case 3:
            for i in lista:
                if i % 2 == 0:
                    posicao_par = lista.index(i)
                    if lista_jogo[posicao_par] == '_':
                        lista_jogo[posicao_par] = "P"
                else:
                    posicao_impar = lista.index(i)
                    if lista_jogo[posicao_impar] == '_':
                        lista_jogo[posicao_impar] = "I"

                e_primo_ou_num_e = True
                for i2 in range(2, int(i ** 0.5) + 1):
                    if i % i2 == 0:
                        e_primo_ou_num_e = False
                        break
                if e_primo_ou_num_e:
                    posicao_primo = lista.index(i)
                    if lista_jogo[posicao_primo] == '_':
                        lista_jogo[posicao_primo] = "Pr"
                    elif lista_jogo[posicao_primo] == "P" or lista_jogo[posicao_primo] == "I":
                        lista_jogo[posicao_primo] += " & Pr"
            print('\nLegenda:\nP = Par\nI = Impar\nPr = Primo')
            print(lista_jogo)
        case _:
            print('\nTodas as dicas já foram utilizadas')

def distancia_e_acertos(lista, chute):
    distancia = []
    for i in lista:
        distancia.append(abs(i - chute))
    menor = min(distancia)
    print(f'Seu chute foi: {chute}\nE o seu chute foi:')
    if menor == 0:
        print('Certo, boa dms')
        lista.remove(chute)
        return chute

    elif menor <= 3:
        print('Muito Perto, tem um número secreto a pelo menos 3 números de distancia')

    elif menor <= 5:
        print('Perto, tem um número secreto a pelo menos 5 números de distancia')

    elif menor <= 7:
        print('Meio longe, tem um número secreto a pelo menos 7 números de distancia')

    elif menor <= 13:
        print('Longe, tem um número secreto a pelo menos 13 números de distancia')

    elif menor <= 17:
        print('Muito longe, tem um número secreto a pelo menos 17 números de distancia')

    elif menor > 17:
        print('Longe dms fio, esquece, não tem nenhum número secreto a pelo menos 17 números de distancia')


def Jogo(lista, dificuldade, lista_jogo):
    acertos = []
    lista_copia = lista[:]

    pontos = 0
    erros = 0
    dica = 1

    while True:
        if len(lista) < 1:
            if pontos < 1:
                pontos = 0
            pontos -= erros
            print(f"\nPaaarabéns, vc ganhou. Você conquistou {pontos} pontos\n")
            break

        print(f'\n----------------------------------\nAcertos: {pontos//2}\nErros: {erros}')

        print(f'\n {lista_jogo}\n----------------------------------')

        match dificuldade:
            case 'Facil':
                chute = (input('Se desejar usar alguma dica, digite "dica"\nSe desejar desistir, digite "desistir"\nChute um número de 1 a 25: ')).lower()
                print('')
                if chute == 'dica':
                    dicas(lista, dica, lista_jogo)
                    dica += 1
                    continue
                elif chute == 'desistir':
                    print(f'Você teve um total de {pontos} mas infelizmente não ganhou')
                    break
            case 'Medio':
                chute = (input('Se desejar usar alguma dica, digite "dica"\nSe desejar desistir, digite "desistir"\nChute um número de 1 a 50: '))
                print('')
                if chute == 'dica':
                    dicas(lista, dica, lista_jogo)
                    dica += 1
                    continue
                elif chute == 'desistir':
                    print(f'Você teve um total de {pontos} mas infelizmente não ganhou')
                    break
            case 'Dificil':
                chute = (input('Se desejar usar alguma dica, digite "dica"\nSe desejar desistir, digite "desistir"\nChute um número de 1 a 100: '))
                print('')
                if chute == 'dica':
                    dicas(lista, dica, lista_jogo)
                    dica += 1
                    continue
                elif chute == 'desistir':
                    print(f'Você teve um total de {pontos} mas infelizmente não ganhou')
                    break

        try:
            chute = int(chute)
        except ValueError:
            print('Digite um número, por favor')
            continue

        distancia_e_acertos(lista, chute)

        if chute in lista_copia:
            if chute in acertos:
                print('Esse número já foi besta')

            else:
                acertos.append(chute)
                index = lista_copia.index(chute)
                lista_jogo[index] = chute
                pontos += 2

        else:
            erros += 1

menu_inicial()