def menu_inicial():
    while True:
        op = input('======== MENU INICIAL ========\n1 - Começar\n2 - Sair\n>>> Digite sua opção: ')
        match op:
            case '1':
                piramide, opcao = pedir_altura()
                match opcao:
                    case "altura":
                        printar_pela_altura(piramide)
                        preco(piramide)
                    case "base":
                        printar_pela_base(piramide)
                        preco(piramide)
            case '2':
                print('\nRaleu mofi')
                break
        continuar = input('\n>>> Deseja testar novamente?(s/n): ').lower()
        print('')
        if continuar != 's':
            print('Tamo junto')            
            break

def pedir_altura():
    while True:
        
        pergunta = input('\n>>> Você gostaria de definir a pirâmida pelo tamanho da base ou pela altura? (base/altura): ').lower()
        
        match pergunta:
            
            case "base":
                while True:
                    print('\n(Digite "c" para cancelar)')
                    tamanho_base = input('>>> Digite o tamanho da base (tem que ser um número ímpar): ').lower()
                    if tamanho_base == "c":
                        break
                    else:
                        try:
                            base = int(tamanho_base)
                            if base % 2 != 0:
                                return base, pergunta
                            else:
                                print("Digite um número ímpar")
                        except ValueError:
                            print("por favor digite um valor, Ex: 1, 4, 5, 7, 8, 01, 12")

            case "altura":
                while True:
                    print('\n(Digite "c" para cancelar)')
                    tamanho_altura = input('Digite a altura da pirâmide: ').lower()
                    if tamanho_altura == "c":
                        break
                    else:
                        try:
                            altura = int(tamanho_altura)
                            return altura, pergunta
                        except ValueError:
                            print("por favor digite um valor, Ex: 1, 4, 5, 7, 8, 01, 12")

            case _:
                print("Resposta inválida")

def printar_pela_base(base):
    contador = 0
    for i in range(base + 2):
        if i % 2 != 0:
            print(" " * ((base // 2) - contador) + ("*" * i) + (" " * ((base // 2) - contador)))
            contador += 1

def printar_pela_altura(altura):
    contador = 1
    for i in range(altura * 2):
        if i % 2 != 0:
            print(" " * (altura - contador) + ("*" * i) + (" " * (altura - contador)))
            contador += 1

def preco(tamanho):
    preco = tamanho * 26.3
    print(f'\nA sua pirâmide ficou em R${preco:.2f}')

menu_inicial()