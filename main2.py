import xml.etree.ElementTree as ET


tree2 = ET.parse('exemplo2.xml')
content2 = tree2.getroot()

aula = content2.get('Aula')
satifacao = content2.get('Satisfacao')

for proj in tree2.findall('projeto'):
    print(proj.text)

print(f'\n{tree2.find('projeto[@id="1"]').text}')


for proj in tree2.findall('projeto'):
    del(proj.attrib['id'])
    

tree2.write('exemplo3.xml')


print(f'\nO resultado da aula "{aula}", é {satifacao.lower()}.')