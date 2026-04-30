#Integrantes da Challenge/CP

#Tárik Moussa Alma - RM: 571411
#Giovanni Azevedo - RM: 569750
#Fabricio Aquiles Sales da Silva - RM: 570985
#Carlos Eduardo - RM: 569574
#Ítalo Neto - RM: 572912

#Função pedida no exercício
print("======================================== SISTEMA DE INVESTIGAÇÃO CRIMINAL =============================")
print("\nVocê será interrogado sobre o caso Art Alma.")
print("Responda com sinceridade, pois nossos profissionais não deixam nada passar.\n")
def fazer_pergunta(numero):
    while True:
        if numero == 1:
            pergunta = input("Você telefonou para o Art antes, depois ou entre o tempo do assassinato? (s/n): ")
        elif numero == 2:
            pergunta = input("Você esteve pelas proxímidades da praia do local do crime? (s/n): ")
        elif numero == 3:
            pergunta = input("Você mora perto ou aos arredores da vítima Art? (s/n): ")
        elif numero == 4:
            pergunta = input("Você tinha dívidas, emprestou ou circulava dinheiro com o Art? (s/n): ")
        elif numero == 5:
            pergunta = input("Art era um bom comerciante. Você já trabalhou com ou usufruía dos produtos dele? (s/n): ")
        else:
            return 0

        pergunta = pergunta.lower()

        if pergunta == "s":
            return 1
        elif pergunta == "n":
            return 0
        else:
            print("Resposta Incorreta!!  Dígite apenas s/n. :)")

#Função pedida no ex
def classificar_investigado(total_sim):
    if total_sim == 5:
        return "As evidências são claras... Você é o Assassino!!!"
    elif total_sim >= 3:
        return "Após a análise de recursos semióticos, você foi intítulado como Cúmplice."
    elif total_sim == 2:
        return "Por pouco... Você é Suspeito, mas se prepare para mais perguntas.."
    else:
        return "Você é Inocente. Mas estamos de olho. "


#Mainzada
total_positivo = 0
contador = 1

while contador <= 5:
    total_positivo += fazer_pergunta(contador)
    contador += 1

print("\nTotal de respostas sim para mérito de classificação: ", total_positivo)
print("Classificação: ", classificar_investigado(total_positivo))
print("Após bruta analíse das suas respostas. Pela quantidade, ausência ou presença de sim, chegamos nessa conclusão.")


#README
#Ttópico de entrega do exercício do CP. Explicação de onde foram usadas repetição, condicionais e função.
#As funções aparecem nas linhas 13 e 38. o Objetivo de cada uma atende ao seu nome; a da linha 13 mostra o menu do sistema e imprimi as perguntas, usando uma estrutura de repetição while True, para que a resposta siga e absorva o que ela pede, no caso " s/n ", caso contrário, faz um retorno e imprimi a mensagem de erro, com formato incorreto de mensagem.
#A função da linha 38 serve para classificar o usuario de acorco com quantos sim foram respondidos na def 13, e essas impressões são armazenaas e reultilizadas para saber se realmente atendem àquela circunstância, pelo return.
#As condicioonais if e else nas duas def, são usadas junto de uma váriavel que a gente preescreveu e, segue o seu caminho de acordo com a lógica implementada.

# =================================================================== Parte 1 =====================================================
