def alterar_case_letras(frase):
    indice = 0
    frase_saida = [];
    while indice < len(frase):
        if (not(frase[indice].isspace())):
           if (frase[indice].islower()):
            frase_saida.append(frase[indice].upper())
           elif (frase[indice].isupper()):
            frase_saida.append(frase[indice].lower())
        else:
            frase_saida.append(" ")
        indice = indice + 1
    frase_saida = "".join(frase_saida)
    return frase_saida

frase_entrada = input("Entre com a frase: ")
frase_final = alterar_case_letras(frase_entrada)
print(frase_final)

