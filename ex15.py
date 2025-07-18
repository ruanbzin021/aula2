valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

salario_bruto = valor_hora * horas_trabalhadas

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = imposto_renda + inss + sindicato
salario_liquido = salario_bruto - descontos

print("\nResumo do cálculo:")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto Imposto de Renda (11%): R$ {imposto_renda:.2f}")
print(f"Desconto INSS (8%): R$ {inss:.2f}")
print(f"Desconto Sindicato (5%): R$ {sindicato:.2f}")
print(f"Total de Descontos: R$ {descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")