#Fazer algorítmo para ler A, B, C e em seguida imprimir na tela a soma e mostrar se é menor que C
EntradaA = int(input("Insira o valor de A: "))
EntradaB = int(input("Insira o valor de B: "))
EntradaC = int(input("Insira o valor de C: "))
soma = EntradaA + EntradaB
saida = print(soma)
if EntradaC < soma:
    print(f"{EntradaC} é menor que {soma}")




