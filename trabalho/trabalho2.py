#Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.


#Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;

#Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;

#Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;



print("Bem vindo a loja de açai do Lucca Souza")
print('------cardapio------')
print('|tamanho|cupuaçu(CP)| açai(AC)') 
print('| P | R$  9.00 | R$ 11.00 |')
print('| M | R$  14.00 | R$ 16.00 |')
print('| G | R$  18.00 | R$ 20.00 |')
# apresentaçao

carrinho = 0 # declaraçao de variavel

while True:
    #escolha do sabor
    sabor = input("escreva seu sabor CP/AC: ") 
    sabor = sabor.upper()
    if sabor == 'CP' or sabor == 'AC':
        print(f"você escolheu {sabor}")
        #validaçao
    elif sabor != 'CP' and sabor != 'AC':
        print('sabor invalido')
        continue
    #escolha de tamanho

    tamanho = input("escreva o tamanho P/M/G: ") 
    tamanho = tamanho.upper()
    if tamanho == 'P' or tamanho == 'M' or tamanho == 'G':
        print(f"você escolheu o tamanho: {tamanho}")
        #validaçao
    elif tamanho != 'CP' and tamanho != 'AC':
        print('tamanho invalido')
        continue
    # confirmaçao de valor
    if sabor == 'CP':
        if tamanho == 'P':
            preco = 9.00    
        elif tamanho == 'M':
            preco = 14.00    
            
        elif tamanho == 'G':
            preco = 18.00    
    if sabor == 'AC':
        if tamanho == 'P':
            preco = 11.00    
            
        elif tamanho == 'M':
            preco = 16.00    
        elif tamanho == 'G':
            preco = 20.00    
            
    carrinho = (carrinho + preco)
# continuar programa
        
    continuar= input("voce quer comprar mais ? s/n")
    if continuar == 's':
        continue
    #finalizador de progama
    elif continuar == 'n':
        
        print(f'total de R${carrinho}')
        break












