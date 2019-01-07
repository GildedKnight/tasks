
#Script to find all mesh_terms in the xml files.
#Using ElementTree Module

import xml.etree.ElementTree as ET
import glob
import json
import requests


file_list= glob.glob('/home/musadiq/Desktop/data/*.xml')
#print(file_list)
#parsing the xml files
for elements in file_list:
    xmltree = ET.parse(elements) 
    root = xmltree.getroot()
    mesh_list = []
    #extracting the mesh_terms from the files
    for mesh_term in root.iter('mesh_term'):
        mesh_list.append(mesh_term.text)
  
    
    print(mesh_list)


#using havoc api to find the content of the term extracted from xml files. 
#api_token = '4w1-0c03599de51f803b75d3'
api_url_base = 'http://havoc.appliedinformaticsinc.com/concepts'

term = input("Enter the term you want to serach: ")
user = input("Enter user name: ")
token = input("Enter your Token: ")

link_param = {'term':term, 'user':user,'token':token}
response = requests.get(api_url_base,params=link_param)
print(response.concepts)



#Extracting the cui of the term 
result = response.json()
for items in result:
    print(items["cui"])



#synonyms
cui = input("Enter the cui: ")
user = input("Enter user name: ")
token = input("Enter your Token: ")
link_param_syno = {'user':user,'token':token}
base_url = 'http://havoc.appliedinformaticsinc.com/concepts/' + cui + '/synonyms'
response = requests.get(base_url,params=link_param_syno)
print(response.json())
