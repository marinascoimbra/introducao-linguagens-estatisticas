def media_notas(notas):
    contador_notas = 0
    indice_notas = 0
    numerador_notas = 0
    while contador_notas < 3:
        nota = int(notas[indice_notas])
        numerador_notas = numerador_notas + nota
        indice_notas = indice_notas + 2
        contador_notas = contador_notas + 1
    return numerador_notas / contador_notas


quantidade_estudantes = int(input("Informe a quantidade de estudantes: "))
indice = 0;
notas_alunos = {}

while indice <= quantidade_estudantes - 1:
    nome_aluno = input("Informe o nome do aluno: ")
    notas_alunos[nome_aluno] = input("Informe as 3 notas: ")
    indice = indice + 1

aluno_pesquisa = input("Informe o nome do aluno que deseja saber a média de notas: ")
media = media_notas(notas_alunos[aluno_pesquisa])
print(round(media,2))