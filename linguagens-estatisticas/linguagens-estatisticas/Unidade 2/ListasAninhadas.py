# Encontra o aluno com a segunda maior nota

def encontra_maior_valor(lista):
    quantidade_elementos_lista = len(lista)
    lista_maior_valor = lista[0]
    indice = 0
    while indice < quantidade_elementos_lista - 1:
        if lista[indice + 1][1] > lista_maior_valor[1]:
            lista_maior_valor = lista[indice + 1]
        elif lista[indice + 1][1] == lista_maior_valor[1]:
            lista_maior_valor.append(lista[indice + 1])
        indice = indice + 1
    return lista_maior_valor


lista_informacoes_alunos = []
lista_aluno = []
quantidade_alunos = int(input("Informe a quantidade de alunos: "))
indiceAlunos = 0

while indiceAlunos <= quantidade_alunos - 1:
    nome_aluno = input("Informe o nome do aluno: ")
    lista_aluno.insert(0, nome_aluno)
    nota_aluno = int(input("Informe a nota do aluno: "))
    lista_aluno.insert(1, nota_aluno)
    lista_informacoes_alunos.append(lista_aluno)
    lista_aluno = []
    indiceAlunos = indiceAlunos + 1

informacos_aluno_maior_nota = []
informacoes_aluno_segunda_maior_nota = []

informacos_aluno_maior_nota = encontra_maior_valor(lista_informacoes_alunos)
lista_informacoes_alunos.remove(informacos_aluno_maior_nota)
informacoes_aluno_segunda_maior_nota = encontra_maior_valor(lista_informacoes_alunos)

print("O(s) aluno(s) com a segunda maior nota foi(foram):\n")
indiceImprimir = 0
while indiceImprimir < len(informacoes_aluno_segunda_maior_nota) - 1:
    print(informacoes_aluno_segunda_maior_nota[indiceImprimir] + '\n')
    indiceImprimir = indiceImprimir + 1
