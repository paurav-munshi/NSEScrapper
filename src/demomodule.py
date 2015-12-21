'''
Created on Dec 13, 2015

@author: paurav
'''
import io
from urllib.error import HTTPError

if __name__ == '__main__':
    pass

print("Hello")

import urllib.request
import zipfile

hdrs={"Accept":"*/*",
"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"en-US,en;q=0.8",
"Connection":"keep-alive",
"Host":"www.nseindia.com",
"Referer":"http://www.nseindia.com/products/content/derivatives/equities/homepage_fo.htm",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
"X-Requested-With":"XMLHttpRequest"}

print('hello')

output = None
bytesData = None

try:
    req = urllib.request.Request("http://www.nseindia.com/content/historical/DERIVATIVES/2015/DEC/fo09DEC2015bhav.csv.zip",None,headers=hdrs)
    output = urllib.request.urlopen(req)
except HTTPError as e:
    print("Error while fetching data", e)
except Exception as er:
    print('Unknown error while fetching data',er)    
     
if(output):
    bytesData = io.BytesIO(output.read()).getvalue()

if(bytesData):
    file = open("D:\\temp.zip","wb")
    file.write(bytesData)
    file.close()
    
print('Now getting zipinfo');

zi = zipfile.ZipInfo("D:\\temp.zip")  

print("FileName is ",zi.filename)  

zf = zipfile.ZipFile("D:\\temp.zip","r")

print(zf.namelist())

zf.extractall("D:\\tempextract\\")

open("http://www.nseindia.com/content/historical/DERIVATIVES/2015/DEC/fo09DEC2015bhav.csv.zip","rb")