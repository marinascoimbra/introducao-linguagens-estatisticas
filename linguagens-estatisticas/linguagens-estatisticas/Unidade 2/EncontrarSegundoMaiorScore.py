# Encontre o Segundo Melhor Score
def verifica_maior_numero(lista):
    maiorValor = 0;
    indice = 1;
    contagemLista = len(lista);
    while (indice < contagemLista):
        if (lista[indice] > lista[indice-1]):
            maiorValor = lista[indice];
        indice = indice + 1;
    return maiorValor;
        


x = input("Entre com uma lista de números inteiros:");
listaX = list(x);
maiorValorInicial = verifica_maior_numero(listaX);
listaX.remove(maiorValorInicial);
segundoMaiorValor = verifica_maior_numero(listaX);
print("O segundo maior valor é: ", segundoMaiorValor);  

