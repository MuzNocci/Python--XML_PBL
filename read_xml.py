import xml.etree.ElementTree as ET



file = ET.parse('read_xml.xml')
root = file.getroot()


#Imprime todo o conteúdo do arquivo
print(ET.tostring(root))


#Imprime o nome da TAG root
print(root.tag)

#Imprime o valor do atributo "name" da TAG [0]
print(root[0].get('name'))

#Imprime o nome da TAG [0], e pode ser feito com subníveis como root[0][0].tag
print(root[0].tag)

#Imprime os atributos da TAG [0] (Formato dicionário Python)
print(root[0].attrib)

#Imprime o texto entre as TAGs "Rank" na TAG [0][0], e pode ser feito com subníveis como root[0][0].tag
print(root[0][0].text)

#Imprime o valor do atributo "name" da TAG [1][3] (Formato dicionário Python)
print(root[1][3].get('name'))


for item in file.findall('country'):
    print(item.attrib)

for item in file.findall('country'):
    print(item.attrib.values())

for item in file.findall('country/neighbor'):
    print(item.attrib)

#or

for item in file.findall('.//neighbor'):
    print(item.attrib['name'])


print(ET.tostring(file.find('country[@name="Panama"]')))


#Imprime os nomes das TAGs contidos na TAG principal
for child in root:
    print(child.tag, child.attrib, child.text)