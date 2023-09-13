import os
import student as ST


class main:


    def __init__(self):

        os.system('clear')

        print('############################################')
        print('Welcome to Student Registration  1.0')
        print('############################################')

        self.mainPage()


    def pagination(self, selected):

        os.system('clear')

        match selected:

            case 1:
                self.registerStudent()
            case 2:
                ST.student.showAllStudents(self)
            case '':
                self.mainPage()


        self.__init__() if input('Choose other action? (Y/N) ').upper() == 'Y' else os.system('exit')


    def mainPage(self):

        print('Possible Actions:')
        print('1 - Register Student')
        print('2 - Show Students')
        print('3 - Search Student')

        self.pagination(int(input('Type the number of the option: ')))


    def registerStudent(self):

        self.id = str(ST.student.counterStudent(self))
        self.name = input('Student name: ')
        self.address = input('Student address (city / state): ')
        self.phone = input('Student phone: ')
        self.email = input('Student e-mail: ')
        self.age = input('Student age: ')

        ST.student.createStudent(self, self.id, self.name, self.address, self.phone, self.email, self.age)




if __name__ == '__main__':
    
    App = main()
    exec.App