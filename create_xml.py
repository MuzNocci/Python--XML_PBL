from xml.etree.ElementTree import Element, ElementTree


instrumento = Element('Instrumento', tipo='Violão', status='Disponível')

yamaha = Element('Yamaha', cor="Marrom")
memphis = Element('Memphis', cor='Preto', modelo='Comum')
gianini = Element('Gianini', cor='Bege', modelo='Elétrico')
tagima = Element('Tagima', cor ='Preto', modelo='Comum')
gibson = Element('Gibson', cor='Preto')

instrumento.append(yamaha)
instrumento.append(memphis)
instrumento.append(gianini)
instrumento.append(tagima)
instrumento.append(gibson)

ElementTree(instrumento).write('create_xml.xml')