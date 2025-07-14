faturamento = 1000
custo = 700
lucro = faturamento - custo

numero = 15.57 #arredondar numero
print(round(numero))

print(f"Faturamento: {faturamento}\nCusto: {custo}\nLucro: {lucro}")

#print("Faturamento: " + str(faturamento) + "\nCusto: " + str(custo) + "\nLucro: " + str(lucro))

email = "EMAIL_falso@gmail.com"

print(email.lower()) #.lower() serve para diminuir os textos

print(email.find("@")) #.find() serve para procurar o elemento no texto. -1, se não encontrar o elemento. Se encontrar: a posição do elemento

posicao = email.find("@")
servidor = email[posicao:]
#servidor = email[posicao+1:]
print(servidor)

# tamanho de um texto
tamanho = len(email)
print(tamanho)

# trocar um pedaço do texto
servidor_trocado = email.replace("gmail.com", "hotmail.com")
print(servidor_trocado)

nome = "ruan barros"
print(nome.capitalize()) # Ruan barros - Só a primeira letra fica maiuscula

print(nome.title()) # Ruan Barros - Todas as letras inicias ficam maiusculas

# especiais - formatação numerica

margem = lucro / faturamento

print(f"Faturamento: R${faturamento:,.2f}\nCusto: {custo}\nLucro: {lucro}")

print(f"Margem: {margem:.1%}")














