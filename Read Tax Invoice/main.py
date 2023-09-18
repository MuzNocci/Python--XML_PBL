import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.parse('673X462486858125699S.xml').getroot()
nsNFE = {'ns':'http://www.barueri.sp.gov.br/nfe'}

numero_nfe = root.find('ns:ListaNfeServPrestado/ns:CompNfeServPrestado/ns:NfeServPrestado/ns:InfNfeServPrestado/ns:NumeroNfe', nsNFE)
print(f'O número da nota fiscal é {numero_nfe.text}.')
