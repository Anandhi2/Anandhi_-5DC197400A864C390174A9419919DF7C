#write a function called linear search product(lsp) that takes the list...

def lsp(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = lsp(products, target)
print(result)