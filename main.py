import xml.etree.ElementTree as ET 


tree = ET.parse('exemplo.xml')
content = tree.getroot()

content.set('Aula', 'XML com Python')
content.set('Satisfacao', 'satisfatório')

for id, proj in enumerate(tree.findall('projeto')):
    proj.set('id', str(id+1))

tree.write('exemplo2.xml')