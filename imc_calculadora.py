#Coletando dados dos usuário
nome = str(input("Informe seu nome: "))
peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura em metros: "))

#IMC
imc = peso / altura ** 2

#Exibindo resultado
print(nome, 'tem', altura, 'de altura,',)
print ('pesa', peso, 'quilos e seu imc é',)
print(f"{imc:.2f}")

#Classificando o IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 24.9:
    print("Você está no peso ideal.")
elif imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
