import xml.etree.ElementTree as ET



file = ET.parse('update2_xml.xml')
root = file.getroot()


for atrib in file.findall('Employee'):
    del(atrib.attrib['idade'])


file.write('delete_xml.xml')