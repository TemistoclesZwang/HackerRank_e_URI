A, B, C = map(float, input().split())

if (A < (B + C)) and (B < (A + C)) and (C < (A + B)) :
  print ('Perimetro = {}'.format(A+B+C))
else:
  area = ((A + B) / 2) * C
  print ('Area = {}'.format(area))

if media > = 7.0:
    print('Aluno aprovado')

elif media < 5.0:
    print('Aluno reprovado')