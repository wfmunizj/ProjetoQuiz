import time
global pontos

pontos = 0
gabarito = ['E', 'C', 'A', 'C', 'E', 'C', 'C', 'C', 'A', 'B']
resposta = []
retorno = [  'RESPOSTA INCORRETA a RESPOSTA CERTA é:\nA peste negra é trasmitida somente por gotículas no ar e/ou picadas de pulgas infectadas.',
           '\nRESPOSTA INCORRETA a RESPOSTA CERTA é:\nA Pandemia de Peste negra ocorreu por volta de 1346-1353.',
           '\nRESPOSTA INCORRETA a RESPOSTA CERTA é:\nA peste negra é um vírus trasmitido pela pulga dos ratos.',
           '\nRESPOSTA INCORRETA a RESPOSTA CERTA é:\nA gripe espanhola não foi uma EPIDEMIA e sim uma PANDEMIA que se espalhou pelo globo.',
           '\nRESPOSTA INCORRETA a RESPOSTA CERTA é:\nAs manchas vermelhas são um sintoma da catapora.',
           '\nRESPOSTA INCORRETA a RESPOSTA CERTA é:\nTodas as vacinas são feitas à partir do próprio vírus.',
           '\nRESPOSTA INCORRETA a RESPOSTA CERTA é:\nA gripe suína teve origem no México.',
           '\nRESPOSTA INCORRETA a RESPOSTA CERTA é:\nO subtipo H1N4 é inexistente até o momento.',
           '\nRESPOSTA INCORRETA a RESPOSTA CERTA é:\nA Gripe suína teve sua origem no ano de 2009',
           '\nRESPOSTA INCORRETA a RESPOSTA CERTA é:\nAté o presente momento é suspeito que o Pangolin transmitiu o COVID-19 para os seres humanos.']

#PESTE NEGRA
def correcao_1():
    global pontos 
    for i in range(1):
        if gabarito[0] == resposta[0]:
            print('Parabéns, você acertou e ganhou 3 pontos')
            pontos += 3
        else:
            pontos -= 2
            print("\nVocê errou e perdeu 2 pontos\n")
            time.sleep(3)
            print (retorno[0])
            break

def correcao_1_1():
    global pontos 
    for i in range(1):
        if gabarito[1] == resposta[1]:
            print('Parabéns, você acertou e ganhou 3 pontos')
            pontos += 3
        else:
            pontos -= 2
            print("\nVocê errou e perdeu 2 pontos\n")
            time.sleep(3)
            print (retorno[1])

def correcao_1_2():
    global pontos 
    for i in range(1):
        if gabarito[2] == resposta[2]:
            print('Parabéns, você acertou e ganhou 3 pontos')
            pontos += 3
        else:
            pontos -= 2
            print("\nVocê errou e perdeu 2 pontos\n")
            time.sleep(3)
            print (retorno[2])

#GRIPE ESPANHOLA
def correcao_2():
    global pontos 
    for i in range(1):
        if gabarito[3] == resposta[3]:
            print('Parabéns, você acertou e ganhou 9 pontos')
            pontos += 9
        else:
            pontos -= 7
            print("Você errou e perdeu 7 pontos")
            time.sleep(3)
            print (retorno[3])

def correcao_2_1():
    global pontos 
    for i in range(1):
        if gabarito[4] == resposta[4]:
            print('Parabéns, você acertou e ganhou 9 pontos')
            pontos += 9
        else:
            pontos -= 7
            print("Você errou e perdeu 7 pontos")
            time.sleep(3)
            print (retorno[4])

def correcao_2_2():
    global pontos 
    for i in range(1):
        if gabarito[5] == resposta[5]:
            print('Parabéns, você acertou e ganhou 9 pontos')
            pontos += 9
        else:
            pontos -= 7
            print("Você errou e perdeu 7 pontos")
            time.sleep(3)
            print (retorno[5])

#GRIPE SUÍNA
def correcao_3():
    global pontos 
    for i in range(1):
        if gabarito[6] == resposta[6]:
            print('Parabéns, você acertou e ganhou 12 pontos')
            pontos += 12
        else:
            pontos -= 9
            print("Você errou e perdeu 9 pontos")
            time.sleep(3)
            print (retorno[6])

def correcao_3_1():
    global pontos 
    for i in range(1):
        if gabarito[7] == resposta[7]:
            print('Parabéns, você acertou e ganhou 12 pontos')
            pontos += 12
        else:
            pontos -= 9
            print("Você errou e perdeu 9 pontos")
            time.sleep(3)
            print (retorno[7])

def correcao_3_2():
    global pontos 
    for i in range(1):
        if gabarito[8] == resposta[8]:
            print('Parabéns, você acertou e ganhou 12 pontos')
            pontos += 12
        else:
            pontos -= 9
            print("Você errou e perdeu 9 pontos")
            time.sleep(3)
            print (retorno[8])

#COVID-19
def correcao_4():
    global pontos 
    for i in range(1):
        if gabarito[9] == resposta[9]:
            print('Parabéns, você acertou e ganhou 8 pontos')
            pontos += 8
        else:
            pontos -= 6
            print("Você errou e perdeu 6 pontos")
            time.sleep(3)
            print (retorno[9])

#PERGUTAS PESTE NEGRA
def pergunta_1():
    print("\nPESTE NEGRA\n")
    print("1-Quais são os meios de transmissão da Peste negra?\n")
    print("a) Através da tosse e espirros\n"
          "b) Através da transmissão sanguínea\n"
          "c) Através de animais\n"
          "d) Sexualmente transmissível\n"
          "e) Através da tosse e por pulgas infectadas")
          
    resposta_1 = input("\nResposta:").upper()
    resposta.append(resposta_1)

def pergunta_2():
    print("\nPESTE NEGRA\n")
    print("2-Qual período ocorreu a pandemia da Peste Negra?\n")
    print("a) 1939-1945\n"
          "b) 1278-1281\n"
          "c) 1346-1353\n"
          "d) 1665-1666\n"
          "e) 1889-1890")
    resposta_2 = input("\nResposta:").upper()
    resposta.append(resposta_2)

def pergunta_3():
    print("\nPESTE NEGRA\n")
    print("3- A peste negra é:\n")
    print("a) Um vírus\n"
          "b) Uma bactéria\n"
          "c) Um fungo\n"
          "d) Uma doença hereditária\n"
          "e) Um parasita")
    resposta_3 = input("\nResposta:").upper()
    resposta.append(resposta_3)

#PERGUNTAS GRIPE ESPANHOLA
def pergunta_4():
    print("\nGRIPE ESPANHOLA\n")
    print("4- Sobre a gripe Espanhola marque a alternativa incorreta:\n")
    print("a) A Gripe Espanhola foi uma pandemia que atingiu diversas partes do mundo entre 1918 e 1920, matando milhões de pessoas e sendo muito transmissível.\n"
          "b) A Gripe Espanhola foi o primeiro vírus do tipo influenza a se manifestar no ser humano, por conta disso é muito grave.\n"
          "c) A Gripe Espanhola foi uma epidemia, que se alastrou por todas as partes do globo.\n"
          "d) Devido à primeira guerra a taxa de transmissão da Gripe Espanhola aumentou drásticamente.\n"
          "e) A Gripe Espanhola foi um vírus influenza do tipo A.")
    resposta_4 = input("\nResposta:").upper()
    resposta.append(resposta_4)

def pergunta_5():
    print("\nGRIPE ESPANHOLA\n")
    print("5- A Gripe Espanhola é uma doença que apresenta sintomas muito semelhantes aos da gripe comum, qual desses não é um sintoma em comum?\n")
    print("a) Tosse.\n"
          "b) Febre acima de 38º.\n"
          "c) Dores musculares.\n"
          "d) Dores de cabeça.\n"
          "e) Manchas vermelhas pelo corpo.")
    resposta_5 = input("\nResposta:").upper()
    resposta.append(resposta_5)

def pergunta_6():
    print("\nGRIPE ESPANHOLA\n")
    print("6- A vacina da Gripe Espanhola assim como a de outras vacinas é feita à partir de:\n")
    print("a) Proteinas que matam o vírus.\n"
          "b) Estimulantes para os glóbulos vermelhos.\n"
          "c) À partir do próprio vírus.\n"
          "d) À partir da injeção no cavalo, retirando seus anticorpos.\n"
          "e) Criada em laboratório a partir de outro vírus.")
    resposta_6 = input("\nResposta:").upper()
    resposta.append(resposta_6)

#PERGUNTAS GRIPE SUÍNA
def pergunta_7():
    print("\nGRIPE SUÍNA\n")
    print("7- A gripe Suína teve origem em qual pais?\n")
    print("a) África\n"
          "b) Estados Unidos\n"
          "c) México\n"
          "d) Itália\n"
          "e) China")
    resposta_7 = input("\nResposta:").upper()
    resposta.append(resposta_7)

def pergunta_8():
    print("\nGRIPE SUÍNA\n")
    print("8- O único subtipo da gripe suína inexistente é o:\n")
    print("a) H1N2\n"
          "b) H3N2\n"
          "c) H1N4\n"
          "d) H1N1\n"
          "e) H2N3")
    resposta_8 = input("\nResposta:").upper()
    resposta.append(resposta_8)

def pergunta_9():
    print("\nGRIPE SUÍNA\n")
    print("9- A gripe suína surgiu no ano de:\n")
    print("a) 2009\n"
          "b) 2002\n"
          "c) 2003\n"
          "d) 2010\n"
          "e) 2000")
    resposta_9 = input("\nResposta:").upper()
    resposta.append(resposta_9)

#PERGUNTA COVID-19
def pergunta_10():
    print("\nGRIPE SUÍNA\n")
    print("10- O animal que transmitiu o COVID-19 para os humanos foi:\n")
    print("a) Peixe.\n"
          "b) Pangolim.\n"
          "c) Galinha.\n"
          "d) Morcego.\n"
          "e) Cobra.")
    resposta_10 = input("\nResposta:").upper()
    resposta.append(resposta_10)

#MAIN FUNCTION
def main():
    pergunta_1()
    correcao_1()
    print('\nPontuação atual:', pontos,"pontos")

    pergunta_2()
    correcao_1_1()
    print('\nPontuação atual:', pontos,"pontos")

    pergunta_3()
    correcao_1_2()
    print('\nPontuação atual:', pontos,"pontos")

    pergunta_4()
    correcao_2()
    print('\nPontuação atual:', pontos,"pontos")

    pergunta_5()
    correcao_2_1()
    print('\nPontuação atual:', pontos,"pontos")

    pergunta_6()
    correcao_2_2()
    print('\nPontuação atual:', pontos,"pontos")

    pergunta_7()
    correcao_3()
    print('\nPontuação atual:', pontos,"pontos")

    pergunta_8()
    correcao_3_1()
    print('\nPontuação atual:', pontos,"pontos")

    pergunta_9()
    correcao_3_2()
    print('\nPontuação atual:', pontos,"pontos")

    pergunta_10()
    correcao_4()
    print('\nPontuação atual:', pontos,"pontos")

    print("\nSua pontuação total é de:",pontos,"pontos")

main()

if pontos <= 20:
    print("\nVocê precisa estudar mais.")
elif pontos > 20 and pontos <= 40:
    print("\nEstá indo bem, mas pode melhorar.")
if pontos > 40 and pontos <= 60:
    print("\nEstá quase se tornando um gênio, continue assim.")
elif pontos > 60 and pontos <= 79: 
    print("\nVOCÊ ESTÁ QUASE LÁ, FOI POR POUCO!")
if pontos == 80: 
    print("\nVOCÊ ATINGIU A PONTUAÇÃO MÁXIMA, PARABÉNS!!!")