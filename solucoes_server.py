#Parte 2 do CP2.

#Integrantes da Challenge/CP
#Tárik Moussa Alma - RM: 571411
#Giovanni Azevedo - RM: 569750
#Fabricio Aquiles Sales da Silva - RM: 570985
#Carlos Eduardo Tsucamoto Chiarelli- RM: 569574
#Ítalo Neto - RM: 572912

sistema_escolhido = "Kali Linux"

#Função para exibir opções
def mostrar_menu():
    print("==============================================  Menu de Votação ==================================")
    print('\n1. Windows Server 2022 ')
    print('2. Ubuntu Server ')
    print('3. Red Hat Enterprise Linux (RHEL) ')
    print(f'4. {sistema_escolhido} ')
    print('0. Encerrar votação\n ')

#validas os vots
def validar_voto(numVoto):
    return 0 <= numVoto <= 4

#contados do voto pela regra do return numVoto
votos1 = votos2 = votos3 = votos4 = 0

#loop de votacao
while True:
    mostrar_menu()
    try:
        voto = int(input("Digite seu voto: "))
    except:
        print("Entrada inválida!! Digite um número. ;)")
        continue
    # Validação
    if not validar_voto(voto):
        print("Voto inválido!! Tente novamente. ;)")
        continue
    #encerrar votacao
    if voto == 0:
        break

    #contabilizar votos
    if voto == 1:
        votos1 += 1
    elif voto == 2:
        votos2 += 1
    elif voto == 3:
        votos3 += 1
    elif voto == 4:
        votos4 += 1

#res
total = votos1 + votos2 + votos3 + votos4

print("\n============================= RESULTADO FINAL ==========================")
print(f"Windows Server 2022: {votos1} votos")
print(f"Ubuntu Server: {votos2} votos")
print(f"RHEL: {votos3} votos")
print(f"{sistema_escolhido}: {votos4} votos")
print(f"Total de votos: {total}")


#O while mantém o programa em execução, repetindo a coleta de votos até que digitem 0,/
#que é a condição usada para encerrar o loop com o break.



