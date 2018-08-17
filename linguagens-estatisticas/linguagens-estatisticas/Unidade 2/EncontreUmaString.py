def conta_quantas_vezes_string_maior_contem_string_menor (string_maior, string_menor):
    indice_string_menor = 0
    contador = 0
    for i in range(0, len(string_maior) - 1):
        if (string_maior[i] == string_menor[indice_string_menor]):
            for j in range(i + 1, len(string_menor)):
                indice_string_menor = indice_string_menor + 1
                if (string_maior[j] != string_menor[indice_string_menor]):
                    break
                elif (string_maior[j] == string_menor[indice_string_menor] and indice_string_menor == (len(string_menor) - 1)):
                    contador = contador + 1
            i = j
    return contador

palavra_maior = input("Entre com a palavra maior: ")
palavra_menor = input("Entre com a palavra menor: ")
while (len(palavra_maior) < len(palavra_menor)):
    print("As palavras informadas não são válidas. Informe novamente.")
    palavra_maior = input("Entre com a palavra maior: ")
    palavra_menor = input("Entre com a palavra menor: ")

quantidade = conta_quantas_vezes_string_maior_contem_string_menor(palavra_maior, palavra_menor)
print("A palavra menor apareceu ", quantidade, " vezes na palavra maior.")
