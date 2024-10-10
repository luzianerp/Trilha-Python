 #Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo

n = int(input("Digite um número: "))

# Verificação se o número é positivo ou negativo
if n >= 0:  # considera zero como positivo
    print(n, "é positivo")
else:
    print(n, "é negativo")

print("Fim.")
