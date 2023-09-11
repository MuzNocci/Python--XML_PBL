import xml.etree.ElementTree as ET

file = ET.parse('exemplo3.xml')
data = file.getroot()

proj = ET.Element('projeto')
proj.text = 'Jogo da velha'
data.append(proj)

file.write('exemplo3.xml')