import xml.etree.cElementTree as ET



def studentMenu():
    print("")
    print("S T U D E N T  D A T A B A S E")
    print("1 -Show all students")
    print("2 -Search for student")
    print("3 -Edit a student")
    print("4 -Create a student")
    print("5 -Delete a student")
    print("x -Exit")
    userinput=input("Choose option 1-5 or 'x' to exit: ")
    return userinput


def showAllStudents():
    for contact in root.findall('contact'):
        name = contact.find('name').text
        address = contact.find('address').text
        phone = contact.find('phone').text
        age = contact.find('age').text
        email= contact.find('email').text
        id= contact.find('id').text
        print("--------------------------------------------")
        print("ID: "+ id)        
        print("Name: "+ name)
        print("Address: "+ address)
        print("Phone: "+ phone)
        print("Email: "+ email)
        print("Age: "+ age)
    print("--------------------------------------------")
    print("End of list")

    
def searchForStudent():

    email =input("Enter the Email address of the student you want to search for: ")
    
    for contact in root.findall('contact'):
        emailb = contact.find('email').text
        print("email1: "+ email +" email2: "+ emailb)

        if emailb==email:

            id = contact.find('id').text
            name = contact.find('name').text
            address = contact.find('address').text
            phone = contact.find('phone').text
            age = contact.find('age').text

            print("--------------------------------------------")
            print("STUDENT RECORD ID: "+ id)
            print("ID: "+ id)        
            print("Name: "+ name)
            print("Address: "+ address)
            print("Phone: "+ phone)
            print("Email: "+ emailb)
            print("Age: "+ age)
            print("--------------------------------------------")


def recordExists(email):

    retValue=False

    for contact in root.findall('contact'):
        emailb = contact.find('email').text
        
        if emailb==email:

            retValue=True
       
    return retValue


def editStudent():

    email =input("Enter the Email address of the student to edit: ")

    for contact in root.findall('contact'):
        emailb = contact.find('email').text

        if emailb==email:

            id = contact.find('id').text
            name = contact.find('name').text
            address = contact.find('address').text
            phone = contact.find('phone').text
            email = contact.find('email').text
            age = contact.find('age').text

            name = input("Please enter name:(" + name + ")") or name
            contact.find('name').text= name

            address = input("Please enter address:(" + address + ")") or address
            contact.find('address').text= address

            phone = input("Please enter phone:(" + phone + ")") or phone
            contact.find('phone').text= phone

            phone = input("Please enter email:(" + email + ")") or email
            contact.find('email').text= email

            age = input("Please enter age:(" + age + ")") or age
            contact.find('age').text= age
            
            ntree.write("students.xml")            

            print("--------------------------------------------")
            print("STUDENT RECORD ID: "+ id + " UPDATED")            
            print("--------------------------------------------")

         
def newid():
    maxid = 0
    for contact in root.findall('contact'):
        id= int(contact.find('id').text)
        if id>maxid:
            maxid=id
    return maxid+1


def createStudent():

    email =input("Enter the Email address of the student you want to search for: ")    
    exists=recordExists(email)
    if exists==False:
        
        nid=newid()

        print("Create a record")
        name=input("Name:")
        address=input("Address:")
        age=input("Age:")
        email=input("Email:")
        phone=input("Phone:")

        newrecord = ET.SubElement(root, "contact",id=str(nid))

        ET.SubElement(newrecord, "id", name="id").text = str(nid)
        ET.SubElement(newrecord, "name", name="name").text = name
        ET.SubElement(newrecord, "address", name="address").text = address
        ET.SubElement(newrecord, "phone", name="phone").text = phone
        ET.SubElement(newrecord, "email", name="email").text = email
        ET.SubElement(newrecord, "age", name="age").text = age

        ntree.write("students.xml")    

    else:
        print("--------------------------------------------")
        print("Record already exists")
        print("--------------------------------------------")


def deleteStudent():

    deleterecord=input("Enter the Email address of the record you want to delete: ")

    for contact in root.findall('contact'):

        emailb= contact.find('email').text

        if emailb == deleterecord:

            root.remove(contact)            

            ntree.write("students.xml")        



ntree = ET.parse('students.xml')
root = ntree.getroot()

userinput=""
while userinput !="x":    
    userinput=studentMenu()

    if userinput =="1":
        showAllStudents()

    if userinput =="2":
        searchForStudent()

    if userinput =="3":
        editStudent()

    if userinput =="4":
        createStudent()

    if userinput =="5":
        deleteStudent()