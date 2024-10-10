#Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas paredes
#  (considere que não será descontada a área ocupada por portas e janelas). Cada caixa  de azulejos possui 1,5 m²;


comprimento = float(input("Digite o comprimento da cozinha (em metros): "))
largura = float(input("Digite a largura da cozinha (em metros): "))
altura = float(input("Digite a altura da cozinha (em metros): "))


area_paredes = 2 * (comprimento * altura) + 2 * (largura * altura)

area_por_caixa = 1.5

caixas_necessarias = area_paredes / area_por_caixa

print("Você precisará de caixas de azulejos.")
