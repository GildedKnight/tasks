#Script to find all the tags in a xml file and removing the duplicates.
#Using ElementTree Module

import xml.etree.ElementTree as ET

xmltree = ET.parse('/home/musadiq/Desktop/data/NCT02645604.xml') 

elemlist = []
for elem in xmltree.iter():
    elemlist.append(elem.tag)
    
    
elemlist = list(elemlist)
#print(elemlist)

result = []
for items in elemlist:
    if items not in result:
        result.append(items)
print(result)