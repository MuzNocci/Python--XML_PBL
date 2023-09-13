import xml.etree.ElementTree as ET



class student:


    def createStudent(self, id, fullname, address, phone, email, age):

        try:

            file = ET.parse('Students.xml')
            root = file.getroot()

            newrecord = ET.Element("contact", id = id)
            ET.SubElement(newrecord, "id", name = "id").text = id
            ET.SubElement(newrecord, "name", name = "name").text = fullname
            ET.SubElement(newrecord, "address", name = "address").text = address
            ET.SubElement(newrecord, "phone", name = "phone").text = phone
            ET.SubElement(newrecord, "email", name = "email").text = email
            ET.SubElement(newrecord, "age", name ="age").text = age

            root.append(newrecord)

            file.write("Students.xml")
            print('New student registered.')

        except:

            record = ET.Element('contacts')

            newrecord = ET.SubElement(record, "contact", id = id)
            ET.SubElement(newrecord, "id", name = "id").text = id
            ET.SubElement(newrecord, "name", name = "name").text = fullname
            ET.SubElement(newrecord, "address", name = "address").text = address
            ET.SubElement(newrecord, "phone", name = "phone").text = phone
            ET.SubElement(newrecord, "email", name = "email").text = email
            ET.SubElement(newrecord, "age", name = "age").text = age

            ET.ElementTree(record).write("Students.xml")
            print('New student registered.')


    def counterStudent(self):

        file = ET.parse('Students.xml')
        root = file.getroot()

        counter = 0
        for contact in root.findall('.//contact'):
            counter += 1

        return counter
        

    def showAllStudents(self):

        try:

            file = ET.parse('Students.xml')
            root = file.getroot()

            print('###############################')
            for i in range(student.counterStudent(self)):
                print(f'Contato: 0{i+1}')
                print(f'Nome do estudante: {root[i][1].text.capitalize()}')
                print(f'Endereço: {root[i][2].text}')
                print(f'Telefone: {root[i][3].text}')
                print(f'E-mail: {root[i][4].text}')
                print(f'Idade: {root[i][5].text}')
                print('###############################')

        except:

            print('There are no registered students .')


    def showStudent(self, id):

        file = ET.parse('Students.xml')
        root = file.getroot()

        i = 0
        for contact in root.findall('.//contact'):

            if id-1 == i:

                print('###############################')
                print(f'Contato: 0{id}')
                print(f'Nome do estudante: {root[i][1].text.capitalize()}')
                print(f'Endereço: {root[i][2].text}')
                print(f'Telefone: {root[i][3].text}')
                print(f'E-mail: {root[i][4].text}')
                print(f'Idade: {root[i][5].text}')
                print('###############################')
                
            i =+ 1
            