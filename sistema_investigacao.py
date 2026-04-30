#Integrantes da Challenge/CP
#Tárik Moussa Alma - RM: 571411
#Giovanni Azevedo - RM: 569750
#Fabricio Aquiles Sales da Silva - RM: 570985
#Carlos Eduardo - RM: 569574
#Ítalo Neto - RM: 572912

def fazer_pergunta(numero):
    while True:
        if numero == 1:
            perfunta = input("Você telefonou para a vítima antes, depois ou entre o tempo do assassinato? (s/n): ? ")
        elif numero == 2:
            perfunta = input("Você esteve pelas proxímidades do local do crime? (s/n): ")
        elif numero == 3:
            pergunta = input("Você mora perto da vítima André Monet? (s/n): ")
        elif numero == 4:
            pergunta = input("Você tinha dívidas com a vítima? (s/n): ")
        elif numero == 5:
