# essa ideia pode parecer muito difícil na minha cabeça, mas na realidade pode ser q seja mesmo, mass eu quero fazer um jogo da velha infinito e com um bot, ou seja apartir de sla quantas jogadas, vou decidir ainda, ele vai começar a apagar as jogadas, deixando só as mais recentes, isso pra nunca dar velha

# 1º passo dessa coisa, fazer o tabaleiro, não me parece difícil
# 2º passo desse treco, entender como eu vou fazer pra realizar uma jogada, lista de 3x3 pra fazer o tabaleiro não deve ser tão difícil criar essa jogadas
# 3º passo desse estresse, criar uma função pra alternar as jogadas entre mim e o BOT, ou entre mim e o outro player
# 4º passo dessa saco, criar a o bot, posso fazer ele em várias dificuldades, sendo fácil: ele só colcando em qualquer lugar alatório bem besta; Médio: sendo ele já com uma certa lógica colocando as coisas, (vou usar provavelmente minimax); E o Difícil: vai ser o caba q vai ter a maior porcentagem de acerto nessa jossa, ele vai ser bão pakas e só tenho a dizer isso, porém n posso fazer ele impossível, mas com certeza não vai ser fácil ganhar

def menu_inicial():
    #Não tem muito oq explicar aqui, é só um menu
    while True:
        op = input('\n|<=><=><=><=><=><=> JOGO DAS VEIA <=><=><=><=><=><=>|\n\n1 == Começar o jogo\n2 == Ajuda\n3 == Créditos\n4 == Fechar\n>>> Digite sua opção: ')
        match op:
            case '1':
               dificuldade()
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
                print('\nDiretor de Imagem -> Vinicin\nProgramador Principal -> Vicinin\nAjudante -> Nivicin\nEquime de marketin -> Cinivisi')

            case '4':
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

def dificuldade():
    #Outro menu, só n tem muito oq explicar aqui
    while True:
        op = input('\n|<=><=><=><=> ESCOLHA O MODO DE JOGO <=><=><=><=>|\n1 - Jogar contra BOT\n2 - Jogar contra outro player\n3 - Voltar\n>>> Digite sua opção: ')
        match op:
            case '1':
                op2 = input('\n|<=><=><=><=> ESCOLHA A DIFICULDADE <=><=><=><=>|\n1 - Fácil\n2 - Médio\n3 - Difícil\n>>> Digite sua opção: ')
                match op2:
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
                jogo(jogador1, jogador2)
                break
            case '3':
                menu_inicial()
            case _:
                print('Opção Inválida')

def jogada(tabuleiro, jogando_agr):
    #Aqui decide por no em while True, porque é mais fácil caso o cara escreva errado é só dar um continue
    while True:
        #Aqui inicializando algumas variaveis, coisa leve
        coluna = 0
        linha = 0
        
        #Aqui é onde eu pego a coordenada de onde ele quer jogar, e fiz um if pra corrigir o erro do usuário dar enter sem digitar
        op = input('>>> Onde você deseja jogar: ').lower()
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

def jogo(jogador1, jogador2):
    #Aqui inicializo algumas variavis importantes
    tabuleiro = tabu()
    jogando_agr = 1
    
    #Aqui é o jogo rolando, ele vai rodar 9 vezes pq além disso empata neerr
    for i in range(9):
        
        #Essa parte aqui é só um print, que por sinal poderia mt bem ser uma função pq mds, q print grande
        print(f'\n|<=><=> TABULEIRO <=><=>|')
        print('|=><=><=>|A|B|C|<=><=><=|')
        for i in range(3):
            print(f'|{i + 1}| ==    {tabuleiro[i][0]}|{tabuleiro[i][1]}|{tabuleiro[i][2]}    == |{i + 1}|')
        print('|=======================|')
        
        #Esse aqui é o jogo em si sendo rodado, bem menor q o print IUAHSDIUHASDA
        tabuleiro, jogando_agr = jogada(tabuleiro, jogando_agr)
        status, ganhador = checar_vitoria(tabuleiro)
        
        #Esse daqui vai sempre testar pra ver se o status é True, se for true ele para tudo e vê quem ganhou 
        if status:
            if ganhador == 'X':
                ganhador = jogador1
            elif ganhador == 'O':
                ganhador = jogador2
            print(f'\nParabéns, o(a) {ganhador} ganhou :D\n')
            
            for i in range(3):
                print(f'{tabuleiro[i][0]}|{tabuleiro[i][1]}|{tabuleiro[i][2]}')
            return
    
    #Aqui é caso o for acabe e n chegue no return que tem na parte de ganhar, ele vem pra essa telinha de empate e printa só o tabuleiro
    print('\nO jogo terminou empatado\n')
    print(f'{tabuleiro[i][0]}|{tabuleiro[i][1]}|{tabuleiro[i][2]}')

menu_inicial()

#NOTAS: Atualmene o jogo funciona como um jogo da velha normal, poréeeem, preciso fazer de um jeito q não exista empate
#Sei que é uma ideia meio maluca, mas toda vez q ele chegue ali na sua quarta jogada, o a sua primeira jogada tem q desaparecer
#'Aaah mas como vc vai fazer isso' atualmente tenho algumas ideias mas tenho q botar pra testar, mas por agora temos um jogo da velha funcional
#E depois de tornar ele 'infinito', vou começar a trabalhar nos bots (parte q eu devo passar a maior parte do tempo)