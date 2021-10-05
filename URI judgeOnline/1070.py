x = int(input(''))

resto = x % 2


def sequencia(x):

    if resto == 0:

        y = x + 1
        print('{}'.format(y))

        for n in range(5):
            y += 2
            print('{}'.format(y))

    else:
        print('{}'.format(x))
        for n in range(5):
         x += 2
         print('{}'.format(x))


sequencia(x)
