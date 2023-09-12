import xml.etree.ElementTree as ET



file = ET.parse('update_xml.xml')
root = file.getroot()


new_item = ET.Element('Icecream')
new_item.text = 'Morango'
root.append(new_item)

root.set('name','Nome da empresa')

root[0].set('name','Nome do funcionário')
root[0].set('idade','37')

for elem in file.findall('Employee/SSN'):
    elem.tag = 'EESSNN'
    elem.text = '9999999999999'
    elem.set('name','Teste')

for elem2 in file.findall('Employee/Dependent'):
    elem2.set('name','Teste2')

for elem3 in file.findall('Employee/Fruit/Banana'):
    elem3.tag = 'Mango'
    elem3.text = '888888888'


file.write('update2_xml.xml')