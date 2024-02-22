import os
import xml.etree.ElementTree as ET



tree = ET.parse("test2.xml")
root = tree.getroot()

ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)
    print(name.text)
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
            if elem.tag.__contains__('login') and elem.attrib.__contains__('login') and elem.attrib.__contains__('type'):
                  element.remove(elem)
            if len(elem):
                  delTegLogin(elem)


delTegLogin(root)
delTegLogin(root)
delTegLogin(root)
delTegLogin(root)



tree.write("test2.xml")