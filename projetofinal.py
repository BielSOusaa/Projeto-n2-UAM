lista = []

#listas

def exibir(): 
    TamanhoLista = len(lista)
    print("--------------------------------------")
    for i in range(0, TamanhoLista):
        print(f" Nome: {lista[i][0]} / Email:{lista[i][1]}")
    print("-------------------------------------")




def encontrar(elemento):
    retorno = 0
    TamanhoLista = len(lista)

    for i in range(0, TamanhoLista):
        if elemento in lista[i]:
            print("---------------------------------------")
            print(f" Nome: {lista[i][0]}. \n Email:{lista[i][1]}")
            print("-------------------------------------")
            retorno = elemento
    return (retorno)



def Alterar(elemento):
    TamanhoLista = len(lista)

    for i in range(0, TamanhoLista):
        if elemento in lista[i]:
            print("---------------------------------------")
            print("  Dados que seram alterados: ")
            print(f" Nome: {lista[i][0]} \n Email:{lista[i][1]}")
            print("-------------------------------------")

            NomeNovo = str(input(f"Informe o nome do novo:"))
            lista[i][0] = NomeNovo
            print("-------------------------------")
            print("  Nome alterado!   ")
            print("-------------------------------")
            return
        else:

            print("    Email não encontrado!      ")

            return
def apagar(elemento):
    TamanhoLista = len(lista)

    for i in range(0, TamanhoLista):
        if elemento in lista[i]:
            print("-------------------------------------")
            print("  Dados que seram deletados: ")
            print(f" Nome: {lista[i][0]} \n Email:{lista[i][1]}")
            print("-------------------------------------")
            confirma = str(input("Confirme o delete com S ou N:")).upper()
            if confirma == 'S':
                del (lista[i])
                print("-------------------------------")
                print(" Dados deletados com sucesso! ")
                print("-------------------------------")
                return
            elif confirma == 'N':
                print("------------------------------")
                print("     Operação cancelada!      ")
                print("------------------------------")
                return
        else:
            print("-------------------------------")
            print("    Email não encontrado!      ")
            print("-------------------------------")
            return



def EmOrdemAlfa():
    TamanhoLista = len(lista)
    listaAlfa = lista.copy()
    listaAlfa.sort()
    print("--------------------------------------")
    for i in range(0, TamanhoLista):
        print(f" Nome: {listaAlfa[i][0]} / Email:{listaAlfa[i][1]}")
    print("-------------------------------------")
