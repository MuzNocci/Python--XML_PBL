import xml.etree.ElementTree as ET



def createStudent(id, fullname, address, phone, email, age):

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



#createStudent("1", "Muller", "Campos / RJ", "22 98806-6987", "muller.nocciolli@gmail.com", "37")
#createStudent("2", "Melanie", "Campos / RJ", "22 98800-0000", "melanie.nocciolli@gmail.com", "10")