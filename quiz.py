"""
##### Hands-on: Criando um Sistema de Perguntas e Respostas #####
"""

import unicodedata
import re

# Função para remover acentos

def limpar_texto(texto):
    #Remove acentos
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
        )
    #Remove pontuação e símbolos, mantendo apenas Letras, números e espaços
    texto = re.sub(r'[^\w\s]','',texto)
    #Remove espaços e padroniza para minúsculo
    return texto.strip().lower()

# Passo 1: Criar um dicionário com perguntas e respostas

quiz = {
    "Qual é a capital do Brasil?": "Brasília",
    "Quantos dias tem uma semana?": "7",
    "Qual é o menor número primo?": "2",
    "Qual é o nome do planeta que vivemos?": "Terra",
    "Quanto é 5 + 3?": "8",
    "Qual é o nome do nosso satélite natural?": "Lua",
    "Que cor se forma ao misturar azul e amarelo?": "Verde",
    "Qual animal é conhecido como o rei da selva?": "Leão",
    "Que instrumento mede a temperatura?": "Termômetro",
    "Qual é o contrário de quente?": "Frio"
    }

# Passo 2: Criar a lógica do quiz

acertos = 0

print("=============================================")
print("      🎯 Desafio de Conhecimentos Gerais     ")
print("=============================================")
print("Responda 10 perguntas sobre conhecimentos ")
print("gerais e veja quantas você acerta!")
print("Boa sorte! 🍀")
print("---------------------------------------------\n")

for pergunta,resposta in quiz.items():
    resposta_usuario = input (pergunta + " ")

    if limpar_texto(resposta_usuario) == limpar_texto(resposta):
        print("✅ Resposta correta!")
        acertos += 1
    else:
        print(f"❌ Resposta incorreta! A resposta correta é:{resposta}")

percentual = (acertos/len(quiz))*100
print(f"Seu aproveitamento foi de {percentual:.1f}%")
print(f"Você acertou {acertos} de {len(quiz)} perguntas.")

    
