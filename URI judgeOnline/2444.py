volume_inicial, n_trocas = map(int, input().split())
alteracoes = list(map(int, input().split()))

volume_final = volume_inicial

for i in range(len(alteracoes)):
  if alteracoes[i] >= 0:
    incremento = volume_final + alteracoes[i]
    if incremento > 100:
      volume_final = 100
    else:
      volume_final += alteracoes[i]
  else:
    decrescimo = volume_final - abs(alteracoes[i])
    if decrescimo < 0:
      volume_final = 0
    else:
      volume_final -= abs(alteracoes[i])
 
print(volume_final)