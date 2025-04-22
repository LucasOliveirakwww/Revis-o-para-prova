#Algorítmo que leia um salário mínimo e o salário de um usuário e calcule quantos salários mínimos esse usuário ganha
salariomin = float(input("Digite o equivalente a um salário mínimo: "))
receb = float(input("Digite seu salário: "))
quant = receb/salariomin
print(f"Você recebe {quant:.2f} salários mínimos")