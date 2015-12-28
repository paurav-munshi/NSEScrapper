'''
Created on Dec 29, 2015

@author: paurav
'''
import dataloader
from dataloader.fetchers import ZipFileFetcher
from dataloader.source import Source, ParallelCompositeSource
from concurrent.futures._base import Future

url = "http://www.nseindia.com/content/historical/DERIVATIVES/2015/DEC/fo09DEC2015bhav.csv.zip"

hdrs={"Accept":"*/*",
"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"en-US,en;q=0.8",
"Connection":"keep-alive",
"Host":"www.nseindia.com",
"Referer":"http://www.nseindia.com/products/content/derivatives/equities/homepage_fo.htm",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
"X-Requested-With":"XMLHttpRequest"}

urlFetcherProps = {}
urlFetcherProps['urlHeaders'] = hdrs 
urlFetcherProps['extractFile'] = 'fo09DEC2015bhav.csv'
print(urlFetcherProps)

fetcher = ZipFileFetcher()

source = Source()
source.setName("NSE India");
source.setLocation(url)
source.setProperties(urlFetcherProps)
source.setFetcher(fetcher)

compositeSource = ParallelCompositeSource()
compositeSource.addSouce(source)

compositeSource.fetchDataAsBytes()