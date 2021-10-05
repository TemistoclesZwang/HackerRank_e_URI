def split_partes(s, partes):
  return list(map(''.join, zip(*[iter(s)]*partes)))

def lista_bin_to_octal(lista_bin):
  lista_decimal = []
  lista_str = []

  for i in range(len(lista_bin)): 
    lista_decimal.append(int(lista_bin[i], 2))

  for i in range(len(lista_decimal)): 
    lista_str.append(str(lista_decimal[i]))

  return '.'.join(lista_str)

def ip_bit_string(ip):
  octetos = ip.split('.')
  ips_bin = []
  for i in range(len(octetos)):
    ips_bin.append("{0:08b}".format(int(octetos[i])).replace('0b', ''))
  return ''.join(ips_bin)

def mascara_bit_string(mascara):
  try:
    bits_um = int(mascara)
    bits_zero = 32 - bits_um
    bit_list = []
    for i in range(bits_um):
      bit_list.append('1')
    
    for i in range(bits_zero):
      bit_list.append('0')
    
    return ''.join(bit_list)
  except:
    octetos = mascara.split('.')
    mascaras_bin = []
    for i in range(len(octetos)):
      mascaras_bin.append("{0:08b}".format(int(octetos[i])).replace('0b', ''))
    return ''.join(mascaras_bin)


while True:
  try:
    entradas = input()
    try:
      ent = entradas.split()
      ip = ent[0]
      mascara = ''
      mascara = ent[1]
    except:
      ent = entradas.split('/')
      ip = ent[0]
      mascara = ''
      mascara = ent[1]

    bit_str = mascara_bit_string(mascara)
    bits_rede = bit_str.count('1')
    bits_maquinas = bit_str.count('0')

    quantidade_enderecos_maquinas = pow(2, bits_maquinas) - 2

    ip_rede_bin = ip_bit_string(ip)
    list_ip_rede_bin = list(ip_rede_bin)

    for i in range(len(ip_rede_bin)):
      if i >= bits_rede:
        list_ip_rede_bin[i] = '0'

    ip_rede_bin = ''.join(list_ip_rede_bin)

    ############################################

    list_ip_broadcast_bin = list(ip_rede_bin)

    for i in range(len(ip_rede_bin)):
      if i >= bits_rede:
        list_ip_broadcast_bin[i] = '1'

    ip_broadcast_bin = ''.join(list_ip_broadcast_bin)

    ocatal_broadcast_split = split_partes(ip_broadcast_bin, 8)
    ocatal_rede_split = split_partes(ip_rede_bin, 8)

    print('Endereco de rede: {}'.format(lista_bin_to_octal(ocatal_rede_split)))
    print('Endereco de broadcast: {}'.format(lista_bin_to_octal(ocatal_broadcast_split)))
    print('Numero de maquinas: {}\n'.format(quantidade_enderecos_maquinas))
  except EOFError:
    break