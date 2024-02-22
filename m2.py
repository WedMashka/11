import os
import re
import xml.etree.ElementTree as ET

FPTH_IN_XML = os.getcwd()
FPTH_OUT_TXML = os.getcwd() + r'\resultXml'
files = os.listdir(FPTH_IN_XML)

for nf in files:
    if nf.__contains__('.xml'):
        fileName = nf
        with open(fileName, 'r', encoding='windows-1251') as targetFileName:
            tree = ET.parse(targetFileName)
            root = tree.getroot()
            ns = {'real_person': 'http://people.example.com',
                  'role': 'http://characters.example.com'}

            for actor in root.findall('real_person:actor', ns):
                name = actor.find('real_person:name', ns)
                for char in actor.findall('role:contract', ns):
                    if char.attrib.__contains__("trusted-ipilist"):
                        (char.attrib).pop("trusted-ipilist")
                        (char.attrib).pop("allow-trusted-ip-only")

            pp = root.find('role:login', ns)
            str1 = pp.attrib.get('login')
            pp.attrib.clear()
            pp.text = str1


            def delTegLogin(element):
                for elem in element:
                    if elem.tag.__contains__('login') and elem.attrib.__contains__(
                            'login') and elem.attrib.__contains__('type'):
                        element.remove(elem)
                    if len(elem):
                        delTegLogin(elem)


            delTegLogin(root)
            delTegLogin(root)
            delTegLogin(root)
            delTegLogin(root)
            fileOutXml = open('gg.xml', 'w', encoding='windows-1251')
            fileOutXml.write(root)
            fileOutXml.close()
            # with open(os.path.join(FPTH_OUT_TXML, nf), 'w', encoding='windows-1251') as fileOutXml:
            #     fileOutXml.write(root)

# with open(os.path.join()) as fileOutXml:
#     f = '<?xml version="1.0" encoding="windows-1251"?>'