valor_hora = float(input("Quanto vc ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas por dia? "))
salario_total = horas_trabalhadas * valor_hora
print(f"O total do seu salário no mês é: R$ {salario_total:.2f}")
