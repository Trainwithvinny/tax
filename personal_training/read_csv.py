'''
Created on 5 Jan 2019

@author: vinny
'''
import os




class Readcsv(object):
    
    #path = ""
    '''adjust this argument to fit the extension type'''
    file_type = [".csv"]
    tables =[]
    files = []

    def __init__(self, path):
        '''
        HELP The constructor should load in all the spreadsheets in the specified
             folder (path).  It should omit any files that are not CSV files
             (i.e. that do not end in .csv), here you will be appending new objects of class Table to the list
             self.tables.
        '''
        
        
       
        for filename in (os.listdir(path)):
            
            #print "fname", os.path.splitext (filename) [1]
            if os.path.splitext (filename) [1] in self.file_type:
                self.files.append(filename)
        print self.files
        
        #for i in self.files:
            
                    
                #self.tables.append(Table(path, i))
         
            
       