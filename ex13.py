altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (homem/mulher): ").lower()

if sexo == 'homem':
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem de altura {altura:.2f}m é: {peso_ideal:.2f} kg")
elif sexo == 'mulher':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher de altura {altura:.2f}m é: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido. Use 'homem' ou 'mulher'.")