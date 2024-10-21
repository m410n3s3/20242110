def script():
    vC = [1 , 3.4 , "A" , " IFSC " ]
    print (vC)
    input("Pressione enter para continuar")
    print("Inserção de 50 na posição 0")
    vC.insert(0,50)
    print(vC)
    input("Pressione enter para continuar")
    print("Inserção de B na posição 3")
    vC.insert(3,"B")
    print(vC)
    input("Inserção no final do vetor de 11")
    vC.append(11)
    vC.append("A")
    print (vC)
    return vC

def script1(vetA):
    print ("vetor recebido ",vetA)
    print ("remoção do valor ",vet[2])
    vetA.remove(3.4)
    print ("Escolha a remoção do A ")
    escolha = input("Pressione 1 para remover a primeira ocorrencia, outra tecla para todas ")
    if (escolha == "1"):
        vetA.remove("A")
    else:
        while "A" in vetA:
            vetA.remove("A")
        print("vetor final ", vetA)
    print(vetA)

def script2(vetB):
    vetB_copia = vetB.copy()
    print("vetor recebido ",vetB)
    print("remoção por del")
    posicao_inicial = 1
    posicao_final = 3
    del vetB[posicao_inicial:posicao_final]
    print (f"vetor com posição [{posicao_inicial}:{posicao_final}] removida ", vetB)
    print ("remoção de pop ")

def script3():
    valores = list(range(1,11))
    anos = list(range(2020,2060,10))
    lista_concatenada = valores+anos
    print(valores)
    valores.extend(anos)
    print(valores)
    print(lista_concatenada)

def script4():
    mercado = ["ouro", "bitcoin", "titulos" ]
    print(mercado)
    mercado.sort()
    print(mercado)
    moedas = ["ouro","bitcoin", "titulos", "Dólar", "Real"]
    moedas_original = moedas.copy()
    moedas.sort(key=str.casefold)
    print(moedas)


if __name__ == "__main__":
    # vet = script()
    # script1(vet)
    # script2(vet)
    # script3()
    script4()