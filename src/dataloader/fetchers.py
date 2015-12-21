'''
Created on Dec 17, 2015

@author: paurav
'''
import urllib.request
from urllib.error import HTTPError
from datetime import time
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
            hdrs = properties['urlHeaders']
            req = urllib.request.Request(location,None,headers=hdrs)
            output = urllib.request.urlopen(req)
            fileBytes = output.read()
        except HTTPError as e:
            print("Error while fetching data", e)
        except Exception as er:
            print('Unknown error while fetching data',er) 
        
        tempFile = FileFetcher.tempDir + 'tempFileScrapper' + time.time()
        
        tf = open(tempFile,'w+b')
        tf.write(fileBytes)
        tf.close()
        return tempFile 
    
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
        
        bytesData = self.readBytesFromFile(fileLocation, properties)
        
        bytesData = self.processBytesPostRead(bytesData,fileLocation,properties)
        return bytesData   
    
class ZipFileFetcher(FileFetcher):  
    
    def readBytesFromFile(self, fileLocation, properties):
        pass
    
    def processBytesPostRead(self,bytesData,fileLocation,properties):
        zipFile = zipfile.ZipFile(fileLocation,"r")
        
        extractedFileName = properties['extractFile']
        extractedFileName = extractedFileName + time.time() 
        ''' 
        need to adda counter here along with time 
        '''
        
        zipFile.extract(extractedFileName,FileFetcher.tempDir)
        
        bytesRead = None
        extractedFile = open(FileFetcher.tempDir + extractedFileName, "rb")
        bytesRead = extractedFileName.read()
        extractedFile.close()
        zipFile.close()
        
        return bytesRead