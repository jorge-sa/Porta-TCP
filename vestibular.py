#função que identifica letras incompativeis
def detectarLetras(array):
    #Letras permitidas
    alts = "ABCDE"
    cont = True
    for n in array:
        if n not in alts:
            cont = False
    return(cont)

#função de calculo da nota
def calcularNota(g,r):
    nota = 0
    for x in range(len(g)):
        if g[x] == r[x]:
            nota += 1
    return(nota)
        
while True:

    #Número de Questões
    while True:
        try:
            n = int(input("Insira o número de questões: "))
            break
        except:
            print("Erro: Insira um número!")

    if (1 <= n <= 80):
        #Gabarito
        gab = input("Insira o gabarito: ")

        #Respostas do Candidato
        resp = input("Insira as Resposta do Candidato: ")

        #Número de acertos
        certo = 0

        if (len(gab) == len(resp) == n):

            if (gab == gab.upper()) and (resp == resp.upper()):

                if detectarLetras(gab) and detectarLetras(resp):
                    
                    print("A nota do candidato foi " + str(calcularNota(gab,resp)))
                    break

                else:

                    print("Erro: Letras devem ser A, B, C, D ou E!")
                    
            else:
                
                print("Erro: Todas as Letras devem ser Maiúsculas!")
            
        else:
            
            print("Erro: Inconsistência Numérica! Gabarito ou Respostas não correspondem ao número de questões!")
        
    elif (n < 1):
        
        print("Erro: Nenhuma Questão!")
        
    else:
        
        print("Erro: Questões Demais!")

    
