'''para quando todos os elementos da entrada estão na mesma linha'''
# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que
# o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

# Entrada
# A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

# Saída
# Apresente a duração do jogo conforme exemplo abaixo.


def main():
    entrada = input().split()  # Isola cada elemento
    # escolhe um elemento que foi isolado e coloca na variável
    inicio = (int(entrada[0]))
    fim = int(entrada[1])
    chamar_defs(entrada, inicio, fim)


def chamar_defs(entrada, inicio, fim):
    if inicio > fim:
        inicio_maior(entrada, inicio, fim)
    elif fim > inicio:
        fim_maior(entrada, inicio, fim)
    elif inicio == fim:
        inicio_igual_fim(entrada, inicio, fim)


def inicio_maior(entrada, inicio, fim):
    calc = (24 - inicio) + fim
    print('O JOGO DUROU {} HORA(S)'.format(calc))


def fim_maior(entrada, inicio, fim):
    calc = (fim - inicio)
    print('O JOGO DUROU {} HORA(S)'.format(calc))

def inicio_igual_fim(entrada, inicio, fim):
    print('O JOGO DUROU 24 HORA(S)')


main()

#testar tempo função
import time

inicio = time.time()
def main() #função que vai ser testada
fim = time.time()
print(fim - inicio)