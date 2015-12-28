from dataloader.fetchers import Fetcher
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures._base import as_completed
class Source:
    
    def __init__(self):
        self.name = None
        self.location = None
        self.properties = {}
        self.fetcher = None
        
    def setName(self,new_name):
        if(not isinstance(new_name,str)):
            raise TypeError("Provided name should be string")
        
        self.name = new_name

    def setLocation(self,new_loc):
        if(not isinstance(new_loc,str)):
            raise TypeError("Provided location should be string")
        
        self.location = new_loc
        
    def setProperties(self,new_props):
        if(not isinstance(new_props,dict)):
            raise TypeError("Provided properties should be dictionary")
        
        self.properties = new_props
        
    def setFetcher(self,new_fetcher):
        if(not issubclass(new_fetcher.__class__, Fetcher)):
            raise TypeError('Provided Fetcher should be a subclass of Fetcher')
        
        self.fetcher = new_fetcher
    
    def fetchDataAsBytes(self):
            if(self.fetcher):
                fetchedData = self.fetcher.fetchDataAsBytes(self.location,self.properties)
                return fetchedData
            
    
    def fetchDataAsList(self):
            if(self.fetcher):
                fetchedData = self.fetcher.fetchDataAsList(self.location,self.properties)
                return fetchedData
            
class ParallelCompositeSource(Source):
    
    def __init__(self):
        self.subSources = []
        
    def addSouce(self, source):
        if(not issubclass(source.__class__,Source)):
            raise TypeError("Element to be added as sub source should of type Source")
        
        self.subSources.append(source)
        
    def fetchDataAsBytes(self):
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for source in self.subSources:
                futures.append(executor.submit(source.fetchDataAsBytes))
                
            for future in as_completed(futures):
                print('completed load of source data in bytes', future.result())
                
    def fetchDataAsList(self):
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for source in self.subSources:
                futures.append(executor.submit(source.fetchDataAsList))
                
            for future in as_completed(futures):
                print('completed load of source data in list')
              