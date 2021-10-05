def horas_gastas(inicio, fim):
  if inicio + fim > 24:
    return (inicio + fim) - 24
  
  if abs(inicio) > abs(fim):
    return abs(inicio) - abs(fim)
  else:
    return abs(fim) - abs(inicio)

def primeira_passada(inicio, fim):
  if inicio + fim > 24:
    return (inicio + fim) - 24
  
  if inicio < fim:
    return fim + inicio
  return inicio + fim

def segunda_passada(inicio, fim):
  if fim >= 0:
    if inicio + fim > 24:
      return (inicio + fim) - 24
    return inicio + fim
  else:
    if abs(inicio) - abs(fim) < 0:
      return 24 - abs(abs(inicio) - abs(fim))
    return abs(inicio) - abs(fim)

saida, tempo_gasto, fuso = map(int, input().split())

print(segunda_passada(primeira_passada(saida, tempo_gasto), fuso))