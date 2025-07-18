area = float(input("Digite o tamanho da área em metros quadrados: "))
litros_necessarios = area / 3  # 1 litro para cada 3 metros quadrados
latas_necessarias = -(-litros_necessarios // 18)  # Arredonda para cima usando divisão inteira
preco_total = latas_necessarias * 80  # Cada lata custa R$ 80,00

print(f"Latas necessárias: {latas_necessarias:.0f}")
print(f"Preço total: R$ {preco_total:.2f}")