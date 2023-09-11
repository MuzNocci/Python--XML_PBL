import xml.etree.ElementTree as ET


file = ET.parse('create_xml.xml')
root = file.getroot()

#Imprime todo o conteúdo do arquivo
print(ET.tostring(root))

#Imprime os atributos da TAG principal (Formato dicionário Python)
print(root.attrib)

#Imprime os nomes das TAGs contidos na TAG principal
for child in root:
    print(child.tag, child.attrib, child.text)