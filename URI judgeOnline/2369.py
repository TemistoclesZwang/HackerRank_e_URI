consumo = int(input())

franquia1 = 1
franquia2 = 2
franquia3 = 5

intervalo1 = 0
intervalo2 = 0
intervalo3 = 0

if consumo >= 101:
  intervalo3 = (((consumo + 1) - 101) * franquia3)
  intervalo2 = ((101 - 31) * franquia2)
  intervalo1 = (31 - 11) * franquia1
else:
  if consumo >= 31:
    intervalo2 = ((consumo + 1) - 31) * franquia2
    intervalo1 = (31 - 11) * franquia1
  else:
    if consumo >= 11:
      intervalo1 = ((consumo + 1) - 11) * franquia1

print(intervalo1 + intervalo2 + intervalo3 + 7)