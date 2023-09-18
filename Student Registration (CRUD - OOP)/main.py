import os
import student as ST
import page as PG



class main:


    def __init__(self):

        os.system('clear')

        print('############################################')
        print('Welcome to Student Registration  1.0')
        print('############################################\n')

        PG.page.mainPage(self)


    def pagination(self, selected):

        os.system('clear')

        if selected:

            match selected:
                case 1:
                    PG.page.registerStudentPage(self)
                case 2:
                    ST.student.showAllStudents(self)
                case 3:
                    PG.page.searchStudentPage(self)
                case 4:
                    PG.page.updateStudentPage(self)
                case 5:
                    PG.page.deleteStudentPage(self)
                case '':
                    PG.page.mainPage(self)

            self.__init__() if input('Choose other action? (Y/N) ').upper() == 'Y' else os.system('exit')

        else:

            self.__init__()



if __name__ == '__main__':
    
    App = main()
    exec.App