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
