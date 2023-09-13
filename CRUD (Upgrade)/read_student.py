import xml.etree.ElementTree as ET



file = ET.parse('Students.xml')
root = file.getroot()


def showAllStudents():

    print('###############################')
    i = 0
    for contact in root.findall('.//contact'):
        print(f'Contato: 0{i+1}')
        print(f'Nome do estudante: {root[i][1].text.capitalize()}')
        print(f'Endereço: {root[i][2].text}')
        print(f'Telefone: {root[i][3].text}')
        print(f'E-mail: {root[i][4].text}')
        print(f'Idade: {root[i][5].text}')
        print('###############################')
        i =+ 1


def showStudent(id):

    i = 0
    for contact in root.findall('.//contact'):

        if id-1 == i:

            print('###############################')
            print(f'Contato: 0{i+1}')
            print(f'Nome do estudante: {root[i][1].text.capitalize()}')
            print(f'Endereço: {root[i][2].text}')
            print(f'Telefone: {root[i][3].text}')
            print(f'E-mail: {root[i][4].text}')
            print(f'Idade: {root[i][5].text}')
            print('###############################')
            
        i =+ 1



showAllStudents()
#showStudent(1)