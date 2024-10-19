import os.path
from random import randint
import json

def lerArquivo():
    # lendo um arquivo JSON
    with open("pontos.json", "r") as f:
        dados = json.load(f)
    return dados
def escreverArquivo(pfacil, pmedio, pdificil):
    pontos = {"pfacil":pfacil, "pmedio": pmedio, "pdificil": pdificil}
    # escrevendo o objeto em um arquivo JSON
    with open("pontos.json", "w") as ficheiro:
        json.dump(pontos, ficheiro)
def opcao(vida, numero_secreto):
    ponto = 0
    while(vida > 0):
        try:
            numero = int(input("\nQual Número estou pensando?\n"))
            if numero == numero_secreto:
                ponto += 100
                numero_secreto = randint(0,10)
                print(f"Parabens! Você acertou, Acomulou {ponto} Pontos\nContinua Jogando para acumular mais ponto.")
            else:
                vida -= 1
                print(f"Ops {numero_secreto}! Você Errou, ainda tens {vida} Tentativas." if vida != 0 else "Ops! Você Perdeu, Não foi dessa.")  
                print("O Número chutado é Menor que o Número Secreto" if numero_secreto > numero else "O Número chutado e Maior que o número Secreto")
        except:
            print("Digite um Número.")
    return ponto
def pontuacao(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2    
def niveis(nivel, numero_secreto):
    #Lendo o arquivo json
    dados = lerArquivo()
    if nivel == "1":
        print("NIVEL: FÁCIL")
        vida = 10
        x = opcao(vida, numero_secreto)
        ponto = pontuacao(x,dados["pfacil"])
        #Gravando no arquivo json
        escreverArquivo( ponto, dados["pmedio"], dados["pdificil"])
    elif nivel == "2":
        print("NIVEL: MÉDIO")
        vida = 5
        x = opcao(vida, numero_secreto)
        ponto= pontuacao(x,dados["pmedio"])
        #Gravando no arquivo json
        escreverArquivo( dados["pfacil"], ponto, dados["pdificil"])
    else: 
        print("NIVEL: DIFÍCIL")
        vida =3
        x = opcao(vida, numero_secreto) 
        ponto = pontuacao(x, dados["pdificil"]) 
        #Gravando no arquivo json
        escreverArquivo( dados["pfacil"], dados["pmedio"], ponto)     
def instrucao():
    mensagem = """
        AS INSTRUNÇÕES SÃO AS SEGUINTES:

        - Primeiro deves escolher um dos Niveis.
        - Tens de adivinha o numero secreto, que está no intervalo de 0 à 10.
        - A cada acerto tens uma pontuação de 100 Pontos.
        - A cada Erro tens menos uma Vida, e uma pista.
                        VAMOS COMEÇAR?"""
    print(mensagem)
def menu():
    while(True):
        # lendo um arquivo JSON
        dados = lerArquivo()
        op = input("\nESCOLHA UMA DAS OPÇÕES:\n1 - Fácil (10 Tentativas)\n2 - Médio (5 Tentativas)\n3 - Difícil (3 Tentativas)\n4 - Ajuda\n5 - Pontuação\n6 - Sair\n ")
        if op == "1":
            niveis(op, numero_secreto)
        elif op == "2":
            niveis(op, numero_secreto)
        elif op == "3":
            niveis(op, numero_secreto)
        elif op == "4":
            instrucao()
        elif op == "5":
            print("Maior Pontuação")
            print(f"Fácil: {dados['pfacil']}")
            print(f"Médio: {dados['pmedio']}")
            print(f"Difícil: {dados['pdificil']}")
        elif op == "6":
            exit("Aplicação Terminada")
        else:
            print("Operação Inválida")

#------------------------------------INICIO DO APP------------------------------------
print("\n           BEM - VINDO AO JOGO DE ADIVINHAÇÃO")  
numero_secreto = randint(1,10)
vida = 0
if os.path.isfile('pontos.json'):
    menu()
else:
    # escrevendo o objeto em um arquivo JSON
    escreverArquivo(pfacil = 0,pmedio = 0,pdificil = 0)
    menu()