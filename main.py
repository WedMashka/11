import xml.etree.ElementTree as ET
import xml.etree as ETR


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
# tree.write("test2.xml")



pp = root.find('role:login', ns)
# print(pp.attrib)
str1 = pp.attrib.get('login')
# print(str1)
pp.attrib.clear()
pp.text = str1
# print(pp.attrib,pp.tag)





# for elem in root:
#     if elem.tag.__contains__('login') and elem.attrib.__contains__('login') and elem.attrib.__contains__('type'):
#         root.remove(elem)
#     for ele in elem:
#         if ele.tag.__contains__('login') and ele.attrib.__contains__('login') and ele.attrib.__contains__('type'):
#             elem.remove(ele)
#         for el in ele:
#             if el.tag.__contains__('login') and el.attrib.__contains__('login') and el.attrib.__contains__('type'):
#                 ele.remove(el)
#             for e in el:
#                 if e.tag.__contains__('login') and e.attrib.__contains__('login') and e.attrib.__contains__(
#                         'type'):
#                     el.remove(e)

# for elem in root:
#     if elem.tag.__contains__('login') and elem.attrib.__contains__('login') and elem.attrib.__contains__('type'):
#         root.remove(elem)
#     for ele in elem:
#         if ele.tag.__contains__('login') and ele.attrib.__contains__('login') and ele.attrib.__contains__('type'):
#             elem.remove(ele)
#         for el in ele:
#             if el.tag.__contains__('login') and el.attrib.__contains__('login') and el.attrib.__contains__('type'):
#                 ele.remove(el)
#             for e in el:
#                 if e.tag.__contains__('login') and e.attrib.__contains__('login') and e.attrib.__contains__(
#                         'type'):
#                     el.remove(e)

# dictFordel={}
# for elem in root:
#     if elem.tag.__contains__('login') and elem.attrib.__contains__('login') and elem.attrib.__contains__('type'):
#         print(elem.tag, elem.attrib)
#         dictFordel.__setitem__(root, elem)
#     # print(elem.tag, elem.attrib)
#     for ele in elem:
#         # print(ele.tag, ele.attrib)
#         if ele.tag.__contains__('login') and ele.attrib.__contains__('login') and ele.attrib.__contains__('type'):
#             print(ele.tag,ele.attrib)
#             dictFordel.__setitem__(elem, ele)
#         for el in ele:
#             # print(ele.tag, ele.attrib)
#             if el.tag.__contains__('login') and el.attrib.__contains__('login') and el.attrib.__contains__('type'):
#                 print(el.tag, el.attrib)
#                 dictFordel.__setitem__(ele, el)
#                 # ele.remove(el)
#             for e in el:
#                 # print(ele.tag, ele.attrib)
#                 if e.tag.__contains__('login') and e.attrib.__contains__('login') and e.attrib.__contains__('type'):
#                     print(el.tag, el.attrib)
#                     dictFordel.__setitem__(el, e)
#                     # ele.remove(el)

# for key in dictFordel:
#     print(key)
# tree = ET.parse("test2.xml")
# root = tree.getroot()

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