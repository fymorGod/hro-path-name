from os import listdir
from pprint import pprint
from validate_docbr import CPF

path = 'P:/02-Publica/Pastas de Exames/Matriz/RETINOGRAFIA'
cpf = CPF()
#p = 'S:/fyteste'
files = [f for f in listdir(path)]

#str = 'ABRANTESDINALVA SOARES RRA19640311000'

for i in files:
    str = i
    dados = listdir(str)

    str = str.split(' ')
    pprint(str)

    ini = len(str[-1])-11
    # pprint(str[-1][ini:len(str[-1])])
    # cpfUser = str[-1][ini:len(str[-1])]
    # cpfUser = cpf.validate(cpfUser)
    # pprint(cpfUser)


    {nome:"",id:"",imagens:['','',]}
