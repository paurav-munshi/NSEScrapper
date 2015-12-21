# NSEScrapper
NSEScrapper is a tool to scrape daily bhavcopy file from NSE exchange which contains daily closing prices for stocks and 
futures and options. After scraping the purpose is to build a analytical tool on the same. 

Though I am much more familiar and experienced in Java, this is my effort to use python to develop a robust tool 
by putting various OOP design patterns and concurrent patterns in effect. By this tool I am trying to build a 
ETL tool in python which will load zip files of stock prices from NSE web site and load that data in memory or directly
in database. The plan is to develop a layerd and modularized ETL tool and try to implement various OO and concurrency design patterns
in Python.

So far this work have given me good insight into Python as a data processing platform and its OO and concurrent feature support. 
But, by the way of this tool I am trying to understand other dynamics of python like distirbuted transactions, memory management, 
thread management and other such data structures with which I have experience in Java.

Over time I will keep on updating this file to track and report the progress of this project. 
Below this I will keep on adding the technical details of architechture or sturucture of the program

Data Loader
===============================

Data Loader is the backbone module for this software project. The role of Data loader is to read the data from NSE website. 
The url of NSE website provides data in zip files. The modular design of Data loader lets you develop and plug a ZipFileFetcher 
which will help in extracting the csv files from zip files. The Extract part of Data Loader reads the data from the source and 
makes the data available for processing for the transformer. The Extract part is basically divided in two parts

1) Extract - Source and Fetchers
Source classes are basically used to define a data source and some properties related to it. This Source class is internally
passed a fetcher object which will actually hit the datasource and download the data. The relation and defition of Source and Fetchers
makes the design highly pluggable and extensible. Right now the DataLoader only has code for reading files from local disk / mount / http
and additionally getting data as zip files and extracting files from it fi required.

Additionally we have a composite design for Source for enabling extract of data from multiple source by extracting data sequentially 
or parallely. 

2) Transform - Yet to be added

3) Load - Yet to be added

