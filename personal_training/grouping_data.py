'''
Created on 5 Jan 2019

@author: vinny
'''
import os, csv, sys
class Parse_account(object):
    '''
    HELP This class represents the relevant data contained in a single spreadsheet.
    '''
            
            
    def __init__(self, path, filename, search_column, search_text, append_ingoing_or_outgoing):
       
        '''These empty list variables are all the pieces of data pulled from the csv necessary for the analysis'''
           
        
        '''this uses os rather than absolute paths to point to and open the table and renames the function to do
        this as csvfile'''        
        with open(os.path.join(path, filename), 'r') as csvfile:
            reader = csv.DictReader(csvfile)
                     
            
            
            '''skip the headers'''
            list_empty = []
            
            row =  next(reader)
            #print row
            #headers = reader.fieldnames
            #print "headers", headers
            for row in reader:
                
                if search_text in row[search_column]:
                    try:
                        list_empty.append(float(row[append_ingoing_or_outgoing]))
                    except ValueError,e:
                        print "error",e,"on line",row
                #rent.append(row["Money_out"])
            tuple(list_empty)
            #list_name = list_empty 
            print list_empty
            print "*****total is: ", sum(list_empty)
            self.total = sum(list_empty)
    def Return_total(self):
            return self.total
             
    