print('\tArmazena um numero de n bits\n')
n = int(input('\tDigite a quantidade de bits n: '))
import random

n -= 1
nn = random.randrange(2**n,2**(n+1))
lista = [nn]
arq1 = input('Nome do arquivo para armazenar o número: ')
arq1 = open(arq1, 'w')
arq1.writelines(["%s\n" % item for item in lista])
arq1.close()

print('\nNumero:',nn,'\n quantidade de bits: ',nn.bit_length())
input ('\n        Processamento Terminado. Pressione ENTER. ')
