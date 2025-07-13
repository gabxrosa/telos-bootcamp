####Criando um sistema de Avaliação de Desempenho

#Objetivo: classificar o desempenho geral de um funcionário com base na eficiência e colaboração


#Solicitando as métricas/pontuações de eficiência e colaboração do usuário

eficiencia = int(input("Digite a pontuação de eficiência (0 a 100):"))
colaboracao = int(input("Digite a pontuação de colaboração (0 a 100):"))

#Sistema de avaliação

if eficiencia >= 80:
    if colaboracao >= 70:
        classificacao = "Excelente"
    else:
        classificacao = "Bom"
elif 80 > eficiencia >= 50:
    if colaboracao >= 70:
        classificacao = "Satisfatório"
    else:
        classificacao = "Regular"
else:
    classificacao = "Insuficiente"

#Imprimir a classificação do usuário
print(f"A classificação de desempenho do usuários é: {classificacao}")
