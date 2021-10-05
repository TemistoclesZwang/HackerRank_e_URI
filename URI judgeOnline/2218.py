n_instancias = int(input())

resultados = []
for i in range(n_instancias):
  n = int(input())
  resultados.append(int((n * (n + 1)) / 2) + 1)

for i in range(len(resultados)):
  print(resultados[i])



'''
10
1
2
3
4
5
6
7
8
9
10

saida

2
4
7
11
16
22
29
37
46
56

'''