#Parte 2 do CP2.

#Integrantes da Challenge/CP
#Tárik Moussa Alma - RM: 571411
#Giovanni Azevedo - RM: 569750
#Fabricio Aquiles Sales da Silva - RM: 570985
#Carlos Eduardo - RM: 569574
#Ítalo Neto - RM: 572912

sistema_escolhido = "Kali Linux"

#Função para exibir opções
def mostrar_menu():
    print('1. Windows Server 2022 ')
    print('2. Ubuntu Server ')
    print('3. Red Hat Enterprise Linux (RHEL) ')
    print(f'4. {sistema_escolhido} ')
    print('0. Encerrar votação\n ')

#validas os vots
def validar_voto(numVoto):
    return 0 <= numVoto <= 4

#contados do voto pela regra do return numVoto
votos1 = votos2 = votos3 = votos4 = 0



