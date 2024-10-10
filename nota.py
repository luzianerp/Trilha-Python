
#Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a
# nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se
# está em exame, de acordo com as informações abaixo:
# Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;

# Leitura das notas
av1 = float(input('Digite a nota da avaliação 1: '))
av2 = float(input('Digite a nota da avaliação 2: '))
avopt = float(input('Digite a nota da avaliação optativa (ou -1 se não fez): '))

# Cálculo da média considerando a avaliação optativa
if avopt != -1:  # Se o estudante fez a avaliação optativa
    # Substitui a menor nota pelas optativas
    if av1 < av2:
        media = (avopt + av2) / 2
    else:
        media = (av1 + avopt) / 2
else:  # Se não fez a avaliação optativa
    media = (av1 + av2) / 2

# Mensagem de resultado
print("A média do semestre é: ")

# Verificação de aprovação
if media >= 6.0:
    print("Aprovado")
elif media < 3.0:
    print("Reprovado")
else:  # média >= 3.0 e < 6.0
    print("Exame")

print("Fim.")
