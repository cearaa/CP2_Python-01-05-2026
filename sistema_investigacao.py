#Integrantes da Challenge/CP
#Tárik Moussa Alma - RM: 571411
#Giovanni Azevedo - RM: 569750
#Fabricio Aquiles Sales da Silva - RM: 570985
#Carlos Eduardo - RM: 569574
#Ítalo Neto - RM: 572912

#Função pedida no exercício
def fazer_pergunta(numero):
    while True:
        if numero == 1:
            pergunta = input("Você telefonou para a vítima Art antes, depois ou entre o tempo do assassinato? (s/n): ? ")
        elif numero == 2:
            pergunta = input("Você esteve pelas proxímidades da praia do local do crime? (s/n): ")
        elif numero == 3:
            pergunta = input("Você mora perto da vítima André Monet? (s/n): ")
        elif numero == 4:
            pergunta = input("Você tinha dívidas com a vítima? (s/n): ")
        elif numero == 5:
            pergunta = input("Você já trabalhou de comerciante com a vítima? (s/n): ")
        else:
            return 0

        pergunta = pergunta.lower()

        if pergunta == "s":
            return 1
        elif pergunta == "n":
            return 0
        else:
            print("Resposta Incorreta!!  Dígite apenas s/n. :)")


def classificar_investigado(total_sim):
    if total_sim == 5:
        return "Após a análise de recursos sêmióticos, você foi entitulado como: Assassino!!"
    elif total_sim >= 3:
        return "Com vista grossa, te declaramos como Cumplíce, fique esperto.."
    elif total_sim == 2:
        return "Por pouco... Você é Suspeito, mas se prepare para mais perguntas.."
    else:
        return "Você é Inocente. Mas estamos de olho. "





