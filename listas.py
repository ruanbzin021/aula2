vendas = [100, 50, 130, 80, 120, 200]
print(vendas[0])

total_vendas = sum(vendas) # sum soma os itens da lista
print(total_vendas)

quantidade = len(vendas) # len conta quantos elementos tem na lista
print(quantidade)

valor_max = max(vendas) # max mostra o valor maximo da lista
valor_min = min(vendas) # min mostra o valor minimo da lista
print(valor_max, valor_min)

posicao = vendas.index(130) # index localiza a posição de um item da lista
print(posicao)
print(vendas[2:])

produtos = ["iphone", "ipad", "airpod"]
novo_produto = input("Digite aqui o produto: ")
novo_produto = novo_produto.lower()

if novo_produto in produtos:
  print("Produto ja cadastrado!")
  
else:
  print("Produto cadastrado")
  produtos.append(novo_produto)
  
print(produtos)

precos =[4000, 8000, 2000]
precos[0] = precos[0] * 1.1 # Edita um item da lista
print(precos)

print("iphone" in produtos)

produtos.append("macbook") # .append() Adiciona um item na lista
precos.append(10000)
print(produtos)
print(precos)

produtos.remove("macbook") # Remove item da lista
precos.pop(-1) # Tambem remove item da lista
print(produtos, precos)

produtos.insert(1, "airpod") # .insert inserir um item na lista (1 representa a posição que o item vai ficar)
print(produtos)

print(produtos.count("airpod")) # .count serve para contar valores repetidos na lista

produtos.sort() # .sort() serve para deixar os itens em ordem crescente
print(produtos)

produtos.sort(reverse=True) # .sort(reverse=True) serve para deixar os itens em ordem decrescente
print(produtos)




produto_usuario = input("Digite um produto: ")
print(produto_usuario in produtos)






