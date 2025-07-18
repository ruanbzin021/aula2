area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_necessarios = (area / 6) * 1.1  # Adiciona 10% de folga
latas = int(litros_necessarios // 18 + (1 if litros_necessarios % 18 > 0 else 0))
galoes = int(litros_necessarios // 3.6 + (1 if litros_necessarios % 3.6 > 0 else 0))
preco_latas = latas * 80
preco_galoes = galoes * 25

# Mistura de latas e galões
latas_mistas = int(litros_necessarios // 18)
litros_restantes = litros_necessarios - (latas_mistas * 18)
galoes_mistos = int(litros_restantes // 3.6 + (1 if litros_restantes % 3.6 > 0 else 0))
preco_misto = (latas_mistas * 80) + (galoes_mistos * 25)

print(f"Apenas latas: {latas} latas, Preço: R$ {preco_latas:.2f}")
print(f"Apenas galões: {galoes} galões, Preço: R$ {preco_galoes:.2f}")
print(f"Mix: {latas_mistas} latas e {galoes_mistos} galões, Preço: R$ {preco_misto:.2f}")