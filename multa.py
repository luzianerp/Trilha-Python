#Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.

def multa():
    peso = float(input('Digite o peso: '))
  

    if peso <= 100 :
        print("Sem Multa")
    else: peso >100
    excesso = peso - 100
    multa = excesso * 5  # Supondo que a multa é R$ 5 por quilo excedente
    print(f" A Multa é R$ {multa:.2f}")
multa()
   
