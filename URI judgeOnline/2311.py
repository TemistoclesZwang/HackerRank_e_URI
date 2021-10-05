class Competidor:
  nome = ''
  grau_dificuldade = 0.0
  notas = []

  def calcular_nota(self):
    self.notas.remove(max(self.notas))
    self.notas.remove(min(self.notas))

    resultado = 0
    for i in range(len(self.notas)):
      resultado += self.notas[i]
    
    return resultado * self.grau_dificuldade


competidores = []
numero_competidores = int(input())

for i in range(numero_competidores):
  c = Competidor()
  c.nome = input()
  c.grau_dificuldade = float(input())
  c.notas = list(map(float, input().split()))
  competidores.append(c)


for i in range(numero_competidores):
  c = competidores[i]
  print('{} {:.2f}'.format(c.nome, c.calcular_nota()))