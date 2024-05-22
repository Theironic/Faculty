# mensagem de boas vindas
print("bem vindo a copiadora do Lucca Souza")
prdts = print("DIG - digitalização \nICO - impressão colorida\nIPB - impressão preto e branco\nFOT - foto copia")

while True: # escolha de serviço menu
    escolha = input("qual serviço voce quer ?")
    if escolha == 'DIG' or escolha == 'ICO' or escolha == 'IPB' or escolha == 'FOT':
            
        break
    elif  escolha != 'DIG' or escolha != 'ICO' or escolha != 'IPB' or escolha != 'FOT':
        print('escolha invalida, entre com um serviço valido')
        continue

def escolha_service(): #func. escolher serviço
    global escolha
    if escolha == 'DIG':
        escolha = 1.10
        
    elif escolha == 'ICO':
        escolha = 1.0
    elif escolha == 'IPB':
        escolha = 0.40
    elif escolha == 'FOT':
        escolha = 0.20
    
    return escolha
escolha_service()

while True: # escolha o tamanho
    try:
        page = int(input("qual é a quantidade de paginas que voce quer ?"))
        if page >= 200000:
            print('não é aceito pedidos nessa quantidade de páginas')
        else:
            break
    except:
        print('valor invalido')
        continue

def num_page():#numeros de paginas
    global page
    global desconto
    global escolha
    global valor_total
    valor_total = escolha * page
    #calcula o desconto
    if page < 20:
        print("voce nao tem desconto")
        desconto = 0
    elif page >= 20 and page < 200:
        desconto = valor_total * 15 / 100
    elif page >= 200 and page < 2000:
        desconto = valor_total * 20 / 100
    elif page >= 2000 and page < 20000:
        desconto = valor_total * 25 / 100
    
num_page()

print("deseja mais algum serviço ?")
print("1 - encardenaçao simpes - 15.00\n 2 - encardenaçao capa dura - 40.00\n0 - nao desejo mais nada - ")
while True: # serviço extra escolha
    try:
        extra = int(input("qual é sua escolha ?"))
        if extra >= 3 :
            print("escreva valores entre 1/2/0")
        else:
            break

    except:
        print('escreva um numero')

def servico_extra(): #func. serviço extra
    global extra
    while True:
        # decisao de preço
        if extra == 1: 
            extra = 15
            break
        elif extra == 2:
            extra = 45
            break
        elif extra== 0:
            extra = 0
            break
    return extra
servico_extra()
# calculo final
print(f'valor total de R${(valor_total - desconto ) + extra} com o valor extra de R${extra} adicionado')
