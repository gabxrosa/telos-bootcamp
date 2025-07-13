'''Problema: Gerador de Tabuada

Descrição: Crie um programa que gera a tabuada de um número fornecido pelo usuário.

O programa deve:

1. Pedir ao usuário um número inteiro.
2. Exibir a tabuada do número de 1 a 10 usando um laço for.
3. Adicionar a funcionalidade de parar o programa caso o usuário digite
um número negativo (usando while e break).
4. Ignorar o cálculo da tabuada para o número 0 (usando continue).

Saída esperada:

Entrada: 5.

Tabuada do 5:
5x1 = 5
5x2 = 10
'''

while True:
    numero = int(input("Digite um número para ver a tabuada."))
    if numero < 0:
        print("Programa encerrado.")
        break
    if numero == 0:
        print("Número zero ignorado.")
        continue
    print(f"Tabuada do número {numero}:")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
        
