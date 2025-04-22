#Fazer algorítmo para receber um número e imprimir se é par/ímpar, positivo/negativo
entrada = int(input ("Digite um número:"))
if entrada > 0 and entrada % 2 == 0:
    print(f"O número {entrada} é positivo e par")
elif entrada < 0 and entrada % 2 == 0:
    print(f"O número {entrada} é negativo e par")
elif entrada < 0 and entrada % 2 != 0:
    print(f"O número {entrada} é negativo e ímpar")
else:
    print(f"O número {entrada} é positivo e ímpar")

