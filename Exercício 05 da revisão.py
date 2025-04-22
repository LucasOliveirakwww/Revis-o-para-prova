#Algorítmo que calcule IMC
peso = float(input("Digite seu peso (utilize . para vírgula): "))
altura = float(input("Digite sua altura (utilize . para vírgula): "))
IMC = peso/(altura)**2
if IMC < 18.6:
    print("Você está abaixo do peso")
elif IMC > 18.6 and IMC < 24.9:
    print("Peso ideal (parabéns)")
elif IMC > 25.0 and IMC < 29.9:
    print("Levemente acima do peso")
elif IMC > 30.0 and IMC < 34.9:
    print("Obesidade Grau I")
elif IMC > 35.0 and IMC < 39.9:
    print("Obesidade Grau II (Severa)")
else:
    print("Obesidade Grau III (mórbida)")
