class Numero:
    CLASSEB = list (range(1,16))
    CLASSEI = list (range(16,31))
    CLASSEN = list (range(31,46))
    CLASSEG = list (range(46,61))
    CLASSEO = list (range(61,76))

    def __init__(self, numero, classe): 
        self.numero = numero
        self.classe = classe       
      
    def valido(self):
        if (self.classe == 'B'):
          return self.numero in Numero.CLASSEB
        if (self.classe == 'I'):
          return self.numero in Numero.CLASSEI
        if (self.classe == 'N'):
          return self.numero in Numero.CLASSEN
        if (self.classe == 'G'):
          return self.numero in Numero.CLASSEG
        if (self.classe == 'O'):
          return self.numero in Numero.CLASSEO     
     
   
    def mudancas_possiveis(self):
        numeros = self.numero
        list_classe = ['B','I','N','G','O']
        for i in range(5):
            if (self.classe == list_classe[i]) and (self.valido() == False):
                if numeros in self.CLASSEB:
                    return (Numero(numeros, 'B'))
                elif numeros in self.CLASSEI:
                   return (Numero(numeros, 'I'))
                elif numeros in self.CLASSEN:
                    return (Numero(numeros, 'N'))
                elif numeros in self.CLASSEG:
                    return (Numero(numeros, 'G'))
                elif numeros in self.CLASSEO:
                    return (Numero(numeros, 'O'))
                 
    
    
    def __str__(self):
        return '[{}, {}, {}]'.format(self.numero, self.classe, self.valido())

    def __repr__(self):
        return str(self)
     

def main():
    while True:
      try:
        #entradas = input()
        cartela = list(map(int, input().split()))
        cartela.insert(12, '*')
    
        numeros = []
    
        for i in range(0, len(cartela), 5):
          numeros.append(Numero(cartela[i], 'B'))
    
        for i in range(1, len(cartela), 5):
          numeros.append(Numero(cartela[i], 'I'))
    
        for i in range(2, len(cartela), 5):
          numeros.append(Numero(cartela[i], 'N'))
    
        for i in range(3, len(cartela), 5):
          numeros.append(Numero(cartela[i], 'G'))
    
        for i in range(4, len(cartela), 5):
          numeros.append(Numero(cartela[i], 'O'))
    
         
        quantidade_trocaveis = 0
        for i in range(len(numeros)):
          trocado = numeros[i].mudancas_possiveis()
          if trocado != None:
            quantidade_trocaveis += 1
          

        quantidade_falso = 0
        for i in range(len(numeros)):
          if not numeros[i].valido():
            quantidade_falso += 1
       
        def tipo_tabela(quantidade_falso):
          if quantidade_falso == 0:
            return "OK"
          
          if quantidade_trocaveis/2 < 1 or quantidade_falso > 0:
            return "DESCARTAVEL"
          else:
            return "RECICLAVEL"
          
    
        print(tipo_tabela(quantidade_falso - 1))
      except EOFError:
        break
    

main()