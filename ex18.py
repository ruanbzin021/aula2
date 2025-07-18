tamanho = float(input("Tamanho do arquivo (MB): "))
velocidade = float(input("Velocidade da internet (Mbps): "))

tempo = tamanho / (velocidade * 0.125) / 60

print(f"Tempo aproximado de download: {tempo:.2f} minutos")