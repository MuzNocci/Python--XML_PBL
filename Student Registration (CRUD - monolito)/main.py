# This program was made in python 3.4
# It demonstrates how to perfrom full CRUD using the etree XML library


import xml.etree.cElementTree as ET



#------------------------------------------------------------
# s t u d e n t M e n u
#------------------------------------------------------------
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

#------------------------------------------------------------
# s h o w A l l S t u d e n t s 
#------------------------------------------------------------
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

    
#------------------------------------------------------------
# s e a r c h F o r S t u d e n t
#------------------------------------------------------------
def searchForStudent():
    #ask the user for the student id to search for
    email =input("Enter the Email address of the student you want to search for: ")
    
    #go through each record to find the record with the specified Email address
    for contact in root.findall('contact'):
        emailb = contact.find('email').text
        print("email1: "+ email +" email2: "+ emailb)

        #is the rquested id the same as this records id?
        if emailb==email:
            #we have found a match get all the record field values
            id = contact.find('id').text
            name = contact.find('name').text
            address = contact.find('address').text
            phone = contact.find('phone').text
            age = contact.find('age').text
            #print the field values
            print("--------------------------------------------")
            print("STUDENT RECORD ID: "+ id)
            print("ID: "+ id)        
            print("Name: "+ name)
            print("Address: "+ address)
            print("Phone: "+ phone)
            print("Email: "+ emailb)
            print("Age: "+ age)
            print("--------------------------------------------")

#------------------------------------------------------------
# r e c o r d E x i s t s
#------------------------------------------------------------
def recordExists(email):

    #set the default return value to false
    retValue=False

    #go through each record to find the one with the specified Email address
    for contact in root.findall('contact'):
        emailb = contact.find('email').text
        
        #is the rquested id the same as this records id?
        if emailb==email:
            #we have found a match set the return value to true
            retValue=True
    #finally return if the record was found to the caller        
    return retValue



#------------------------------------------------------------
# e d i t S t u d e n t
#------------------------------------------------------------
def editStudent():
    #ask the user for the student id to edit 
    email =input("Enter the Email address of the student to edit: ")

    #go through each record to find the record with the specified id
    for contact in root.findall('contact'):
        emailb = contact.find('email').text

        #test: is the rquested id the same as this records id?
        if emailb==email:
            #YES: we have found a match get all the record field values
            id = contact.find('id').text
            name = contact.find('name').text
            address = contact.find('address').text
            phone = contact.find('phone').text
            email = contact.find('email').text
            age = contact.find('age').text

            #edit name
            name = input("Please enter name:(" + name + ")") or name
            contact.find('name').text= name
            #edit address
            address = input("Please enter address:(" + address + ")") or address
            contact.find('address').text= address
            #edit phone
            phone = input("Please enter phone:(" + phone + ")") or phone
            contact.find('phone').text= phone
            #edit email
            phone = input("Please enter email:(" + email + ")") or email
            contact.find('email').text= email
            #edit age
            age = input("Please enter age:(" + age + ")") or age
            contact.find('age').text= age
            
            #save the update
            ntree.write("students.xml")            
            #print the field values
            print("--------------------------------------------")
            print("STUDENT RECORD ID: "+ id + " UPDATED")            
            print("--------------------------------------------")

            

#------------------------------------------------------------
# n e w i d
#------------------------------------------------------------
def newid():
    maxid = 0
    for contact in root.findall('contact'):
        id= int(contact.find('id').text)
        if id>maxid:
            maxid=id
    return maxid+1



#------------------------------------------------------------
# c r e a t e S t u d e n t
#------------------------------------------------------------
def createStudent():
    #add a record-but we would need to check for duplicates first
    #ask the user for the student email address to search for
    email =input("Enter the Email address of the student you want to search for: ")    
    exists=recordExists(email)
    if exists==False:
        
        #gt a new id
        nid=newid()

        #get the field values from the user
        print("Create a record")
        name=input("Name:")
        address=input("Address:")
        age=input("Age:")
        email=input("Email:")
        phone=input("Phone:")

        #create a contact element at root level
        newrecord = ET.SubElement(root, "contact",id=str(nid))

        #add the fields into out new record
        ET.SubElement(newrecord, "id", name="id").text = str(nid)
        ET.SubElement(newrecord, "name", name="name").text = name
        ET.SubElement(newrecord, "address", name="address").text = address
        ET.SubElement(newrecord, "phone", name="phone").text = phone
        ET.SubElement(newrecord, "email", name="email").text = email
        ET.SubElement(newrecord, "age", name="age").text = age

        #finally save the update
        ntree.write("students.xml")    

    else:
        print("--------------------------------------------")
        print("Record already exists")
        print("--------------------------------------------")

#------------------------------------------------------------
# d e l e t e S t u d e n t 
#------------------------------------------------------------
def deleteStudent():

    #get a variable for the record that you want to delete
    deleterecord=input("Enter the Email address of the record you want to delete: ")

    #OK, now loop through all records looking for specified email address
    for contact in root.findall('contact'):
        #get the email of the current record, 
        emailb= contact.find('email').text
        #check is this the email we are looking for?
        if emailb == deleterecord:
            #YES: remove the record from the xml tree
            root.remove(contact)            
            #finally save the update
            ntree.write("students.xml")        



#------------------------------------------------------------
# main program execution starts here!
#------------------------------------------------------------
#open/read the entire student database
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