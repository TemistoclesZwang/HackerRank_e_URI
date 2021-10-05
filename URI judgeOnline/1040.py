n1, n2, n3, n4 = [float(x) for x in input().split()]

media = round(((2 * n1) + (3 * n2) + (4 * n3) + (1 * n4)) / (2 + 3 + 4 + 1), 1)

print('Media: {:.1f}'.format(media))

if media >= 5.0 and media <= 6.9:
  print('Aluno em exame.')
  nota_exame = round(float(input()), 1)
  print('Nota do exame: {}'.format(nota_exame))        ### AFK 1min
  media_recalque = (media + nota_exame) / 2
  if media_recalque < 5:
    print('Aluno reprovado.')
  else:
    print('Aluno aprovado.')
  print('Media final: {}'.format(media_recalque))

if media > 7.0:
  print('Aluno aprovado.')
elif media < 5.0:
  print('Aluno reprovado.')