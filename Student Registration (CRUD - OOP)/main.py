import os
import student as ST



class main:


    def __init__(self):

        os.system('clear')

        self.mainPage()


    def pagination(self, selected):

        os.system('clear')

        if selected:

            match int(selected):
                case 1:
                    self.registerStudentPage()
                case 2:
                    ST.student.showAllStudents(self)
                case 3:
                    self.searchStudentPage()
                case 4:
                    self.updateStudentPage()
                case 5:
                    self.deleteStudentPage()
                case _:
                    self.mainPage()

            self.__init__() if input('Choose other action? (Y/N) ').upper() == 'Y' else os.system('exit')

        else:

            self.__init__()


    def mainPage(self):

        print('####################################################')
        print('Welcome to Student Registration  1.0')
        print('####################################################\n')
        print('Possible Actions:')
        print('1 - Register Student')
        print('2 - Show Students')
        print('3 - Search Student')
        print('4 - Update Student')
        print('5 - Delete Student')

        try: 

            self.pagination(int(input('\nEnter option number: ')))

        except:

            os.system('clear')
            self.mainPage()


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



if __name__ == '__main__':
    
    App = main()
    exec.App