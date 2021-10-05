#é necessário zerar o led antes de analisar a próxima instância
#esta somando todos os leds
#preciso somar os led de cada instância
instancia = int(input())

lista = []

led = 0


for numero in range(instancia): 
   entradas = list(map(int, input("Enter a multiple value: ")))

   for numero in entradas:

      if numero == 2 or numero == 3 or numero == 5:
         led += 5

      elif numero == 9 or numero == 0 or numero == 6:
         led += 6

      elif numero == 1:
         led += 2

      elif numero == 4:
         led += 4

      elif numero == 7:
         led += 3

      elif numero == 8:
         led += 7

#lista.append(led)

print(led)


