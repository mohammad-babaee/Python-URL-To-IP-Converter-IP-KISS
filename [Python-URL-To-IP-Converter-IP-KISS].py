from socket import *

from traceback import print_tb

print (
    '''                                                                 
88  88888888ba      88      a8P   88   ad88888ba    ad88888ba   
88  88      "8b     88    ,88'    88  d8"     "8b  d8"     "8b  
88  88      ,8P     88  ,88"      88  Y8,          Y8,          
88  88aaaaaa8P'     88,d88'       88  `Y8aaaaa,    `Y8aaaaa,    
88  88""""""'       8888"88,      88    `"""""8b,    `"""""8b,  
88  88              88P   Y8b     88          `8b          `8b  
88  88              88     "88,   88  Y8a     a8P  Y8a     a8P  
88  88              88       Y8b  88   "Y88888P"    "Y88888P"   
        
        | ------------------
        |   Fast URL 2 IP Converter !
        |
        |   Application Developer : Mohammad Babaee

        +++++++++++++++++++++++++++ 
    '''
)
print (" -------- -------- -------- -------- -------- -------- ")


ip = input(" > Please Enter The Damn URL Here (without http/s or www) : ")

ip1 = str(ip)


print("\n")

print (" ---> The Damn Ip Is : " +  str(gethostbyname(ip1)) )

print (" -------- -------- -------- -------- -------- -------- ")

print ('''
                           Happy Hacking !

        ------ This App Is Published Under (MIT License) ------
    ''')