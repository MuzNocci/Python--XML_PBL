import student as ST



class page:


    def mainPage(self):

        print('Possible Actions:')
        print('1 - Register Student')
        print('2 - Show Students')
        print('3 - Search Student')
        print('4 - Update Student')
        print('5 - Delete Student')

        self.pagination(int(input('\nEnter option number: ')))


    def registerStudentPage(self):

        print('Enter student details:\n')
        self.id = str(ST.student.newIDStudent(self))
        self.name = input('Student name: ')
        self.address = input('Student address (city / state): ')
        self.phone = input('Student phone: ')
        self.email = input('Student e-mail: ')
        self.age = input('Student age: ')

        ST.student.createStudent(self, self.id, self.name, self.address, self.phone, self.email, self.age)


    def searchStudentPage(self):

        print('Would you like to search for:\n')
        print('1 - ID')
        print('2 - Name')
        print('3 - E-mail')

        option = input('\nEnter option number: ')
        ST.student.showStudent(self, option, input('Enter text to search: '))


    def updateStudentPage(self):
        print('Update Student:\n')
        ST.student.updateStudent(self, input('Enter the ID to be updated: '))
        

    def deleteStudentPage(self):

        print('Delete Student:\n')
        ST.student.deleteStudent(self, input('Enter the ID to be deleted: '))