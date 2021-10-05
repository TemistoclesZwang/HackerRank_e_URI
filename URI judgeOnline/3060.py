v = int(input())
p = int(input())

if v % p == 0:
  valor_titulo = v // p
  for i in range(p):
    print(valor_titulo)
else:
  resto = v % p
  parcela = v // p
  for i in range(resto):
    print(parcela + 1)
  
  for i in range(p - resto):
    print(parcela)