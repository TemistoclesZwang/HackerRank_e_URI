def determinar_lua(lua1, lua2):
  if lua1 <= lua2:
    if lua2 <= 2:
      return 'nova'
    if lua2 <= 96:
      return 'crescente'
    return 'cheia'
  else:
    if lua2 >= 3 and lua2 <= 96:
      return 'minguante'
    if lua2 >= 97 and lua2 <= 100:
      return 'cheia'
    return 'nova'


dois_dias_atras, dia_anterior = map(int, input().split())

print(determinar_lua(dois_dias_atras, dia_anterior))