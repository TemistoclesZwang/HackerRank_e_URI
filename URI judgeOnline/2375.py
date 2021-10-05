def cabe_ou_nao_cabe(d, h, l, p):
  if (d > h) or (d > l) or (d > p):
    return 'N'
  return 'S'


diametro = int(input())
h, l, p = map(int, input().split())

print(cabe_ou_nao_cabe(diametro, h, l, p))