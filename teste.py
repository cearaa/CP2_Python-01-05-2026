# Parte 2 do CP2 - Exercício 1 e 2

# Integrantes da Challenge/CP
# Tárik Moussa Alma - RM: 571411
# Giovanni Azevedo - RM: 569750
# Fabricio Aquiles Sales da Silva - RM: 570985
# Carlos Eduardo Tsucamoto Chiarelli - RM: 569574

opcao1 = "Windows Server 2022"
opcao2 = "Ubuntu Server"
opcao3 = "Red Hat Enterprise Linux (RHEL)"
opcao4 = "Kali Linux"

#Defs respectivas ao exercício
def mostrar_menu():
    print("==============================================  Menu de Votação ==================================")
    print(f'\n1. {opcao1} ')
    print(f'2. {opcao2} ')
    print(f'3. {opcao3} ')
    print(f'4. {opcao4} ')
    print('0. Encerrar votação\n ')

def validar_voto(numVoto):
    if numVoto >= 0 and numVoto <= 4:
        return True
    else:
        return False

def calcular_percentual(votos, total):
    if total == 0:
        return 0.0
    return (votos / total) * 100

def mostrar_resultado(nome, votos, total):
    percentual = calcular_percentual(votos, total)
    print(f"{nome}: {votos} votos - {percentual:.2f}%")

def analisar_vencedor(v1, v2, v3, v4):
    total_votos = v1 + v2 + v3 + v4
    if total_votos == 0:
        return "sem votos"
    
    
    maior = v1
    if v2 > maior:
        maior = v2
    if v3 > maior:
        maior = v3
    if v4 > maior:
        maior = v4
        
    
    empates = 0
    if v1 == maior: empates += 1
    if v2 == maior: empates += 1
    if v3 == maior: empates += 1
    if v4 == maior: empates += 1
    
    if empates >= 2:
        return "disputa equilibrada"
    
    if maior == v1:
        segundo = v2
        if v3 > segundo: segundo = v3
        if v4 > segundo: segundo = v4
    elif maior == v2:
        segundo = v1
        if v3 > segundo: segundo = v3
        if v4 > segundo: segundo = v4
    elif maior == v3:
        segundo = v1
        if v2 > segundo: segundo = v2
        if v4 > segundo: segundo = v4
    else:
        segundo = v1
        if v2 > segundo: segundo = v2
        if v3 > segundo: segundo = v3
        
    
    diferenca = maior - segundo
    percentual_diff = calcular_percentual(diferenca, total_votos)
    
    
    if percentual_diff < 10:
        return "disputa equilibrada"
    else:
        return "vantagem clara"


votos1 = 0
votos2 = 0
votos3 = 0
votos4 = 0

mostrar_menu()
voto = int(input("Digite seu voto: "))

while voto != 0:
    if validar_voto(voto):
        if voto == 1:
            votos1 += 1
        elif voto == 2:
            votos2 += 1
        elif voto == 3:
            votos3 += 1
        elif voto == 4:
            votos4 += 1
    else:
        print("ERRO DE SISTEMA:Número inválido, digite um número de 0 a 4.")
    
    mostrar_menu()
    voto = int(input("Digite seu voto: "))

total = votos1 + votos2 + votos3 + votos4

print("\n============================= RESULTADO FINAL ==========================")
mostrar_resultado(opcao1, votos1, total)
mostrar_resultado(opcao2, votos2, total)
mostrar_resultado(opcao3, votos3, total)
mostrar_resultado(opcao4, votos4, total)
print("------------------------------------------------------------------------")
print(f"Total de votos: {total}")


status = analisar_vencedor(votos1, votos2, votos3, votos4)
print(f"Tivemos bons competidores e a disputa foi: {status}")
print("========================================================================")