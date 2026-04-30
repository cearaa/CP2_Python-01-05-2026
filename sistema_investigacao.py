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
            pergunta = input("Você telefonou para o Art antes, depois ou entre o tempo do assassinato? (s/n): ? ")
        elif numero == 2:
            pergunta = input("Você esteve pelas proxímidades da praia do local do crime? (s/n): ")
        elif numero == 3:
            pergunta = input("Você mora perto ou aos arredores da vítima Art? (s/n): ")
        elif numero == 4:
            pergunta = input("Você tinha dívidas, emprestou ou circulava dinheiro com o Art? (s/n): ")
        elif numero == 5:
            pergunta = input("Art era um bom comerciante. Você já trabalhou com ou usurfruia dos produtos dele? (s/n): ")
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
        return "As evideências são claras... Você é o Assassino!!!"
    elif total_sim >= 3:
        return "Após a análise de recursos sêmióticos, você foi entitulado como Cumplíce."
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