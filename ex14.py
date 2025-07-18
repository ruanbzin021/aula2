peso = float(input("Digite o peso dos peixes em quilos: "))

limite = 

multa_por_quilo = 4.0

if peso > limite:
    excesso = peso - limite
    multa = excesso * multa_por_quilo
    print(f"Você excedeu o limite de {limite}kg em {excesso:.2f}kg.")
    print(f"Valor da multa a pagar: R$ {multa:.2f}")
else:
    excesso = 0
    multa = 0
    print("Nenhum excesso. Não há multa a pagar.")

print(f"Excesso: {excesso:.2f}kg")
print(f"Multa: R$ {multa:.2f}")