#Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maior conforme o valor da compra.


# Se valor for menor que 2500 o desconto será de 0%;
# Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;
# Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;
# Se valor for igual ou maior que 10000 o desconto será de 11%;



# inicio de programa questao 1
print("Bem vindo a loja de Lucca souza")
#declaraçao de variaveis
valor = float(input("digite o valor do produto:"))
qntd = int(input("digite a quantidade do produto:"))
total = valor * qntd

if total < 2500: #condicionais de desconto
    descont = "você não tem direito a desconto"
    print(f"o valor sem desconto do produto é: R${total}")
    print(f"desconto: {descont}")

elif total >= 2500 and total< 6000:
    descont = total - (total * 4 / 100) 
    print(f"o valor sem desconto do produto é: R${total}")
    print(f"desconto: R${descont}")

elif total >= 6000 and total< 10000:
    descont = total - (total * 7 / 100)
    print(f"o valor sem desconto do produto é: R${total}")
    print(f"desconto: R${descont}")

elif total >= 10000:
    descont = total - (total * 11 / 100)
    print(f"o valor sem desconto do produto é: R${total}")
    print(f"desconto: R${descont}")
else:
    print("erro generico")
#fim do programa
