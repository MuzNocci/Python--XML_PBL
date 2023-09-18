import os
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


    def newIDStudent(self):

        try:

            file = ET.parse('Students.xml')
            root = file.getroot()

            newId = 0
            for contact in root.findall('contact'):
                id = int(contact.find('id').text)
                if id > newId:
                    newId = id
            return newId + 1
        
        except:

            return 1


    def counterStudent(self):

        try:
            file = ET.parse('Students.xml')
            root = file.getroot()

            counter = 1
            for contact in root.findall('.//contact'):
                counter += 1

            return counter
        
        except:

            return 1
        

    def showAllStudents(self):

        try:

            file = ET.parse('Students.xml')
            root = file.getroot()

            print('####################################################')
            for contact in root.findall('.//contact'):
                print(f'Id: {contact.find('id').text}')
                print(f'Name: {contact.find('name').text}')
                print(f'Address: {contact.find('address').text}')
                print(f'Phone: {contact.find('phone').text}')
                print(f'E-mail: {contact.find('email').text}')
                print(f'Age: {contact.find('age').text}')
                print('####################################################')

        except:

            print('There are no registered students .')


    def showStudent(self, opt, text):

        os.system('clear')

        try:
            file = ET.parse('Students.xml')
            root = file.getroot()

            match int(opt):
                case 1: self.option = 0
                case 2: self.option = 1
                case 3: self.option = 4

            i = 0
            founded = 0
            for contact in root.findall('.//contact'):

                if self.option == 1:

                    if str(text).lower() in root[i][1].text.lower():
                        print('####################################################')
                        print(f'Id: {root[i][0].text}')
                        print(f'Name: {root[i][1].text}')
                        print(f'Address: {root[i][2].text}')
                        print(f'Phone: {root[i][3].text}')
                        print(f'E-mail: {root[i][4].text}')
                        print(f'Age: {root[i][5].text}')
                        print('####################################################')
                        founded += 1

                    i += 1

                else: 

                    if root[i][self.option].text == str(text):
                        print('####################################################')
                        print(f'Id: {root[i][0].text}')
                        print(f'Name: {root[i][1].text}')
                        print(f'Address: {root[i][2].text}')
                        print(f'Phone: {root[i][3].text}')
                        print(f'E-mail: {root[i][4].text}')
                        print(f'Age: {root[i][5].text}')
                        print('####################################################')
                        founded += 1

                    i += 1

            if founded == 0:
                print('There are no registered student with the data provided.')

        except:

            print('There are no registered students.')


    def updateStudent(self, id):

        file = ET.parse('Students.xml')
        root = file.getroot()

        for item in root.findall('.//contact'):
            if item.attrib['id'] == id:
                for items in item:
                    if items.tag != 'id':
                        items.text = input(f'Student {items.tag}: ')

        file.write('Students.xml')

        print('\nStudent updated.\n')


    def deleteStudent(self, id):
        
        file = ET.parse('Students.xml')
        root = file.getroot()

        for item in root.findall('.//contact'):
            if item.attrib['id'] == id:
                root.remove(item)

        file.write('Students.xml')

        print('Student deleted.\n')