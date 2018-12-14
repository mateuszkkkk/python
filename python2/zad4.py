import xml.dom.minidom

document = xml.dom.minidom.parse("sample.xml")
element = document.getElementsByTagName("note")[0]
element.getElementsByTagName("body")[0].childNodes[0].data="cos innego"
print(document.toxml())
