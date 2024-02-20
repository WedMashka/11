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
            # print(char.attrib)
tree.write("test2.xml")
            # char.pop("trusted-ipilist")
            # char.pop("allow-trusted-ip-only")

for elem in root.iter():
    print(elem.tag, elem.attrib)
