from collections import deque
#Adição dessa função "deque" serve como uma "Fila em cache", serve pra ajudar a manipular o começo e o final da lista de forma mais eficiente (o pai ta voando slc)

# essa ideia pode parecer muito difícil na minha cabeça, mas na realidade pode ser q seja mesmo, mass eu quero fazer um jogo da velha infinito e com um bot, ou seja apartir de sla quantas jogadas, vou decidir ainda, ele vai começar a apagar as jogadas, deixando só as mais recentes, isso pra nunca dar velha

# 1º passo dessa coisa, fazer o tabaleiro, não me parece difícil
# 2º passo desse treco, entender como eu vou fazer pra realizar uma jogada, lista de 3x3 pra fazer o tabaleiro não deve ser tão difícil criar essa jogadas
# 3º passo desse estresse, criar uma função pra alternar as jogadas entre mim e o BOT, ou entre mim e o outro player
# 4º passo dessa saco, criar a o bot, posso fazer ele em várias dificuldades, sendo fácil: ele só colcando em qualquer lugar alatório bem besta; Médio: sendo ele já com uma certa lógica colocando as coisas, (vou usar provavelmente minimax); E o Difícil: vai ser o caba q vai ter a maior porcentagem de acerto nessa jossa, ele vai ser bão pakas e só tenho a dizer isso, porém n posso fazer ele impossível, mas com certeza não vai ser fácil ganhar

#Atulmente vou inicializar ele aqui memo, dps eu mudo
modo_infinito_padrao = False

def menu_inicial(infinito):
    #Não tem muito oq explicar aqui, é só um menu
    while True:
        op = input('\n|<=><=><=><=><=><=> JOGO DAS VEIA <=><=><=><=><=><=>|\n\n1 == Começar o jogo\n2 == Ajuda\n3 == Configurações\n4 == Créditos\n5 == Fechar\n>>> Digite sua opção: ')
        match op:
            case '1':
               dificuldade(infinito)
            case '2':
                while True:
                    op2 = input('\n|<=><=><=><=> MENU DE AJUDA <=><=><=><=>|\n\n1 -- Como jogar\n2 -- Dificuldades\n3 -- Voltar\n>>> Digite sua opção: ')
                    match op2:
                        case '1':
                            print('\nAqui explico como q joga saco')
                        case '2':
                            print('\no fácil é fácil, o difícil é difícil e o médio é o meio termo, saca?')
                        case '3':
                            break
                        case _:
                            print('Opção Inválida')

            case '3':
                infinito = input('Você deseja ativar o modo infinito por padrão? (s/n): ').lower()
                if infinito != 'n':
                    infinito = True
                
            case '4':
                print('\nDiretor de Imagem -> Vinicin\nProgramador Principal -> Vicinin\nAjudante -> Nivicin\nEquime de marketin -> Cinivisi')

            case '5':
                print('Porque cara D:')
                break

            case _:
                print('Opção Inválida')

def tabu():
    # nesse caso pra fazer esse tabuleiro eu preciso criar uma lista assim
    # 0|0|0
    # 0|0|0
    # 0|0|0

    # 0|0|0  0|0|0  0|0|0
    tabuleiro = [[' ' for i in range(3)]for i in range(3)]
    return tabuleiro

def dificuldade(infinito):
    #Outro menu, só n tem muito oq explicar aqui
    while True:
        #Não sei se vai ser temporário, mas atulamente eu vou fazer esse sistema de "status" pra saber se ta ou n ligado o modo infinito
        if infinito:
            status = 'ligado'
        else:
            status = 'desligado'
        op = input(f'\n|<=><=><=><=> ESCOLHA O MODO DE JOGO <=><=><=><=>|\n1 - Jogar contra BOT\n2 - Jogar contra outro player\n3 - Ativar/Desativar modo infinito (atualmente {status})\n4 - Voltar\n>>> Digite sua opção: ')
        match op:
            case '1':    
                op3 = input('\n|<=><=><=><=> ESCOLHA A DIFICULDADE <=><=><=><=>|\n1 - Fácil\n2 - Médio\n3 - Difícil\n>>> Digite sua opção: ')
                match op3:
                    case '1':
                        print('ainda n temo bot n fi')
                    case '2':
                        print('ainda n temo bot n fi')
                    case '3':
                        print('ainda n temo bot n fi')
                    case _:
                        print('Opção inválida')
            case '2':
                #Aqui é onde roda o jogo, o tal do jogo
                jogador1 = input('\n>>> Quem é o jogador 1?: ').capitalize()
                jogador2 = input('\n>>> Quem é o jogador 2?: ').capitalize()
                jogo(jogador1, jogador2, infinito)
                break
            
            case '3':
                if infinito: infinito = False
                else: infinito = True

            case '4':
                menu_inicial(modo_infinito_padrao)
                
            case _:
                print('Opção Inválida')

def jogada(tabuleiro, jogando_agr):
    #Aqui decide por no em while True, porque é mais fácil caso o cara escreva errado é só dar um continue
    while True:
        #Aqui inicializando algumas variaveis, coisa leve
        coluna = 0
        linha = 0
        
        #Aqui é onde eu pego a coordenada de onde ele quer jogar, e fiz um if pra corrigir o erro do usuário dar enter sem digitar
        op = input(f'>>> Vez do jogador {jogando_agr}. Onde você deseja jogar: ').lower()
        if len(op) > 0:
            caracteres = list(op)
            
            #!!!!!!!!!!!!! Nota pro vinicius do futuro, achar um jeito de verificar independete da ordem !!!!!!!!!!!!!!!!!
            #Esse aqui é o que faz a mágica acontecer, eu divido as letras dos número e procuro aqui a coordenada corespondente
            match caracteres[0]:
                case 'a':
                    coluna = 0
                case 'b':
                    coluna = 1
                case 'c':
                    coluna = 2
                case _:
                    print('\n-----------Você tem q digitar a letra primeiro e depois o número EX: A1, B3, C2-----------\n')
                    continue
                    
            match caracteres[1]:
                case '1':
                    linha = 0
                case '2':
                    linha = 1
                case '3':
                    linha = 2
                case _:
                    print('\n-----------Você tem q digitar a letra primeiro e depois o número EX: A1, B3, C2-----------\n')
                    continue
                    
            #Alternador maluco q eu pensei pra trocar de jogador 1 pra jogador 2, coisa boa dimaize
            if tabuleiro[linha][coluna] == ' ':
                if jogando_agr == 1:
                    tabuleiro[linha][coluna] = 'X'
                    jogando_agr += 1
                elif jogando_agr == 2:
                    tabuleiro[linha][coluna] = 'O'
                    jogando_agr -= 1
                return tabuleiro, jogando_agr
            else:
                print('\n-----------Já tem uma jogada nesse espaço-----------\n')
        else:
            print('\n-----------Você precisa digitar alguma coisa-----------\n')

def jogada_infinito(tabuleiro, jogando_agr, jogadas_feitas):
    coluna = 0
    linha = 0

    #Numero de jogadas q os doido podem fazer antes de começar a apagar
    jogadas_maximas = 5

    #Apagar a jogada mais antiga quando exceder o limite
    if len(jogadas_feitas) > jogadas_maximas:
        apagado_separado = list(jogadas_feitas.popleft())

        match apagado_separado[0]:
            case 'a':
                coluna = 0
            case 'b':
                coluna = 1
            case 'c':
                coluna = 2

        match apagado_separado[1]:
            case '1':
                linha = 0
            case '2':
                linha = 1
            case '3':
                linha = 2

        tabuleiro[linha][coluna] = ' '

    jogadas_maximas_comecar_avisar = 4
    
    if len(jogadas_feitas) > jogadas_maximas_comecar_avisar:
        proximo_a_sair = list(jogadas_feitas[0])
        
        match proximo_a_sair[0]:
            case 'a':
                coluna = 0
            case 'b':
                coluna = 1
            case 'c':
                coluna = 2

        match proximo_a_sair[1]:
            case '1':
                linha = 0
            case '2':
                linha = 1
            case '3':
                linha = 2
            
        tabuleiro[linha][coluna] = f'\033[1m\033[9m{tabuleiro[linha][coluna]}\033[0m'

    while True:

        op = input(f'>>> Vez do jogador {jogando_agr}. Onde você deseja jogar: ').lower()

        if len(op) > 0:
            caracteres = list(op)

            match caracteres[0]:
                case 'a':
                    coluna = 0
                case 'b':
                    coluna = 1
                case 'c':
                    coluna = 2
                case _:
                    print('\n-----------Você tem que digitar a letra primeiro e depois o número EX: A1, B3, C2-----------\n')
                    continue

            match caracteres[1]:
                case '1':
                    linha = 0
                case '2':
                    linha = 1
                case '3':
                    linha = 2
                case _:
                    print('\n-----------Você tem que digitar a letra primeiro e depois o número EX: A1, B3, C2-----------\n')
                    continue

            if tabuleiro[linha][coluna] == ' ':
                if jogando_agr == 1:
                    tabuleiro[linha][coluna] = 'X'
                    jogando_agr += 1
                elif jogando_agr == 2:
                    tabuleiro[linha][coluna] = 'O'
                    jogando_agr -= 1

                jogadas_feitas.append(op)
                return tabuleiro, jogando_agr
            else:
                print('\n-----------Já tem uma jogada nesse espaço-----------\n')
        else:
            print('\n-----------Você precisa digitar alguma coisa-----------\n')

def checar_vitoria(tabuleiro):
    # tem 4 tipso de vitórias, coluna(|), linha(-), diagonal(\) e diagonal invertida(/)
    # Checa as vitórias em linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != ' ':
            return True, tabuleiro[i][0]
    
    # Checa as vitórias em colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != ' ':
            return True, tabuleiro[0][i]
    
    # Checa as vitórias em diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
            return True, tabuleiro[0][0]
    elif tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
            return True, tabuleiro[0][2]
    
    # Se n ganhou em nada, parabéns, vc retornou um false
    return False, 'nada'

def jogo(jogador1, jogador2, infinito):
    # Inicializo algumas variáveis importantes
    tabuleiro = tabu()
    jogando_agr = 1
    jogadas_feitas = deque()
    
    if not infinito:
        # Jogo normal com até 9 jogadas
        for i in range(9):
            # Exibe o tabuleiro
            print(f'\n|<=><=> TABULEIRO <=><=>|')
            print('|=><=><=>|A|B|C|<=><=><=|')
            for i in range(3):
                print(f'|{i + 1}| ==    {tabuleiro[i][0]}|{tabuleiro[i][1]}|{tabuleiro[i][2]}    == |{i + 1}|')
            print('|=======================|')
            
            # Realiza a jogada
            tabuleiro, jogando_agr = jogada(tabuleiro, jogando_agr)
            
            # Verifica o status do jogo
            status, ganhador = checar_vitoria(tabuleiro)
            
            # Se houver um ganhador, termina o jogo
            if status:
                if ganhador == 'X':
                    ganhador = jogador1
                elif ganhador == 'O':
                    ganhador = jogador2
                print(f'\nParabéns, o(a) {ganhador} ganhou :D\n')
                
                for i in range(3):
                    print(f'{tabuleiro[i][0]}|{tabuleiro[i][1]}|{tabuleiro[i][2]}')
                return
    else:
        # Jogo infinito
        while True:
            # Exibe o tabuleiro
            print(f'\n|<=><=> TABULEIRO <=><=>|')
            print('|=><=><=>|A|B|C|<=><=><=|')
            for i in range(3):
                print(f'|{i + 1}| ==    {tabuleiro[i][0]}|{tabuleiro[i][1]}|{tabuleiro[i][2]}    == |{i + 1}|')
            print('|=======================|')
            
            # Realiza a jogada no modo infinito
            tabuleiro, jogando_agr = jogada_infinito(tabuleiro, jogando_agr, jogadas_feitas)
            
            # Verifica o status do jogo
            status, ganhador = checar_vitoria(tabuleiro)
            
            # Se houver um ganhador, termina o jogo
            if status:
                if ganhador == 'X':
                    ganhador = jogador1
                elif ganhador == 'O':
                    ganhador = jogador2
                print(f'\nParabéns, o(a) {ganhador} ganhou :D\n')
                
                for i in range(3):
                    print(f'{tabuleiro[i][0]}|{tabuleiro[i][1]}|{tabuleiro[i][2]}')
                return

    # Caso chegue até aqui, o jogo empatou
    print('\nO jogo terminou empatado\n')
    for i in range(3):
        print(f'{tabuleiro[i][0]}|{tabuleiro[i][1]}|{tabuleiro[i][2]}')

menu_inicial(modo_infinito_padrao)

#NOTAS: Atualmene o jogo funciona como um jogo da velha normal, poréeeem, preciso fazer de um jeito q não exista empate
#Sei que é uma ideia meio maluca, mas toda vez q ele chegue ali na sua quarta jogada, o a sua primeira jogada tem q desaparecer
#'Aaah mas como vc vai fazer isso' atualmente tenho algumas ideias mas tenho q botar pra testar, mas por agora temos um jogo da velha funcional
#E depois de tornar ele 'infinito', vou começar a trabalhar nos bots (parte q eu devo passar a maior parte do tempo)