def eh_valido(a, b, c):
  if (a + b <= c) or (a + c <= b) or (b + c <= a): 
    return False
  return True

valores = list(map(int, input().split()))
valores.sort()

triangulo = False
for i in range(len(valores) - 1, 0, -1):
  loops = 0
  elem_index = i - 1
  while (loops < elem_index):
    if eh_valido(valores[loops], valores[elem_index], valores[i]):
      triangulo = True
      break
    else:
      loops = loops + 1

print('S' if triangulo else 'N')