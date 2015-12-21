'''
Created on Dec 17, 2015

@author: paurav
'''

name="Paurav"
print(type(name))

def checkStrType(new_name):
    print(new_name)
    
    print((isinstance(new_name,str)))

checkStrType(name)

dictio={}
print(type(dictio))
print(isinstance(dictio,dict))