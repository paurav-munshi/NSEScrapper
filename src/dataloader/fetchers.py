'''
Created on Dec 17, 2015

@author: paurav
'''
import urllib.request
from urllib.error import HTTPError
from datetime import time, datetime
import zipfile

class Fetcher:
    
    def __init__(self):
        pass
    
    def fetchDataAsList(self,location,properties):
        pass
    
    def fetchDataAsBytes(self,location,properties):
        pass


class FileFetcher(Fetcher):
    
    tempDir = 'D:\\temp\\'
    
    def __init__(self):
        pass
    
    def downloadFileFromURL(self,location,properties):
        fileBytes=None
        try:
            print(properties)
            hdrs = properties['urlHeaders']
            req = urllib.request.Request(location,None,headers=hdrs)
            output = urllib.request.urlopen(req)
            fileBytes = output.read()
        except HTTPError as e:
            print("Error while fetching data", e)
            raise e
        except Exception as er:
            print('Unknown error while fetching data',er) 
            raise er
        
        fileName = 'tempFileScrapper'
        if 'tempFileFromURL' in properties:
            fileName = properties['tempFileFromURL']
            
        tempFile = FileFetcher.tempDir + fileName + datetime.now().strftime("%Y%B%d")
        
        if(fileBytes):
            tf = open(tempFile,'w+b')
            tf.write(fileBytes)
            tf.close()
            return tempFile
        else:
            return None 
    
    def readLinesFromFile(self,fileLocation,properties):
        f = open(fileLocation,'r')
        lines =  f.readlines()
        f.close()
        return lines
    
    def readBytesFromFile(self,fileLocation,properties):
        f = open(fileLocation,'rb')
        bytesData = f.read()
        f.close()
        return bytesData
    
    def processLinesPostRead(self,linesList,fileLocation,properties):
        return linesList
    
    def processBytesPostRead(self,bytesData,fileLocation,properties):
        return bytesData
           
    def fetchDataAsList(self, location, properties):
        if(not isinstance(location,str)):
            raise TypeError("Provided location should be string")
        if(not isinstance(properties,dict)):
            raise TypeError("Provided properties should be dictionary")
        
        fileLocation = location
        
        if(location.startswith("http://")):
            fileLocation = self.downloadFileFromURL(location, properties)  
        
        linesList = self.readLinesFromFile(fileLocation, properties)
        
        linesList = self.processLinesPostRead(linesList,fileLocation,properties)
        return linesList 
    
    def fetchDataAsBytes(self, location, properties):
        if(not isinstance(location,str)):
            raise TypeError("Provided location should be string")
        if(not isinstance(properties,dict)):
            raise TypeError("Provided properties should be dictionary")
        
        fileLocation = location
        
        if(location.startswith("http://")):
            fileLocation = self.downloadFileFromURL(location, properties)  
        
        if(fileLocation):
            bytesData = self.readBytesFromFile(fileLocation, properties)
            bytesData = self.processBytesPostRead(bytesData,fileLocation,properties)
            return bytesData  
        else:
            return None 
    
class ZipFileFetcher(FileFetcher):  
    
    def readBytesFromFile(self, fileLocation, properties):
        pass
    
    def processBytesPostRead(self,bytesData,fileLocation,properties):
        zipFile = zipfile.ZipFile(fileLocation,"r")
        
        extractedFileName = properties['extractFile'] 
        ''' 
        need to adda counter here along with time 
        '''
        
        zipFile.extract(extractedFileName,FileFetcher.tempDir)
        
        bytesRead = None
        extractedFile = open(FileFetcher.tempDir + extractedFileName, "rb")
        bytesRead = extractedFile.read()
        extractedFile.close()
        zipFile.close()
        
        return bytesRead