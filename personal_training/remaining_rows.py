'''
Created on 6 Jan 2019

@author: vinny
'''

import sqlite3 as lite
import sys



class SQLiteDatabase(object):
    '''
    This class represents an SQLite database.
    The constructor will set con to the object that represents the database
    connection (the name 'con' is arbitrary)
    '''
    filename = ""
    con = None


    def __init__(self, filename):
        '''
        This attempts to connect to the named file as an SQLite database.
        It will create the database if it does not exist. 
        Note that the process is places within try, except, and finally statements.
        '''
        self.filename = filename
        
        
        #the try statement attempts to connect to the given argument, if it is unable to do this, it will output an error msg
        try:
    
            ''' First, you connect to the test.db. It will create it if it does not exist. '''
            self.con = lite.connect(self.filename)
            ''' Now print a list of tables in the database (if it is not new and there are some). '''
            cursor = self.con.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            print("Opened database " + self.filename)
            print("\nContains tables: " + str(cursor.fetchall()))
  
        except lite.Error, e:
            ''' If it was not possible to open the database, report the error and quit. ''' 
            print "Error %s:" % e.args[0]
            sys.exit(1)     
    def csv_sql(self):
     
        con = lite.connect(":memory:")
        cur = con.cursor()
        cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

        with open('data.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin) # comma is default delimiter
            to_db = [(i['col1'], i['col2']) for i in dr]

        cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
        con.commit()
        con.close()

   
        
    def close(self):
        if self.con:
            self.con.close() 
            print ("\nClosed database " + self.filename)
        else:
            print ("\nDatabase " + self.filename + " was not open!")
            
    
    def create_table(self, table, columns):
        '''
            This function creates a table with a user specified name and user specified
            columns.  The columns must be specified as exactly the string that would be provided
            in the CREATE TABLE SQL statement.
        '''
        
        ''' Assemble the SQL string '''
        sql_string1 = "DROP TABLE IF EXISTS %s" % table
        sql_string2 = "CREATE TABLE %s (%s)" % (table, columns)
        print(sql_string2)
     
        try:
            cur = self.con.cursor()
            cur.execute(sql_string1)
            cur.execute(sql_string2)
            self.con.commit()   
           
        except lite.Error, e:
            ''' Or, if there was an error, roll back to the previous state '''
            if self.con:
                self.con.rollback()
                print "Error %s\nRolled back to previous state" % e.args[0]
        
        
        
    def extract_value(self, return_col, table, search_col, comparison, value):
        '''
            This module runs a query on the database and returns a list of
            matching entries 
        '''    
        
        ''' Assemble the SQL string '''
        sql_string = "SELECT %s FROM %s WHERE %s %s ?" % (return_col, table, search_col, comparison)
        #print("Comparator " + comparison)
        print "\n This is your search format"
        print (sql_string)
        print "Search value: ", value
        ''' Execute the SQL statement.  Note that when passing 'value' (the value to
            search for) we convert it to the first item in a tuple - the trailing 
            comma is not a typo but is essential!'''
        try:
            cur = self.con.cursor()
            cur.execute(sql_string, (value,))
            self.con.commit()   
            rows = cur.fetchall()
            print "\nThe search results for your SQL query: "
            print "\n", rows
            return(rows)
            
        except lite.Error, e:
            ''' Or, if there was an error, roll back to the previous state '''
            if self.con:
                self.con.rollback()
                print "Error %s\nSearch failed" % e.args[0]
                
                
    def insert_row(self, table, data):
        '''
            This function creates a table with a user specified name and user specified
            columns.  The columns must be specified as a tuple of values.
        '''
        
        ''' Assemble the SQL string.  This is complicated by the fact that we try to do it safely
            using the placeholder '?' in the SQL statement
            (see https://docs.python.org/2/library/sqlite3.html for an explanation).  This means
            we need as many placeholders as there are columns in the data.  Uncomment
            print(sql_string) to see what is actually passed to the execute function '''
        sql_string = "INSERT INTO %s VALUES(" % table
        for i in range(1, len(data)):
            sql_string += "?,"
        sql_string += "?)"        
        print "sql string", (sql_string)
     
        ''' Now execute the SQL statement.  Note that you need to pass the actual data as the
            second argument to execute '''
        try:
            cur = self.con.cursor()
            cur.execute(sql_string, data)
            self.con.commit()   
            ''' This will tell us if any rows have been updated '''
            print "Number of rows updated: %d" % cur.rowcount
           
        except lite.Error, e:
            ''' Or, if there was an error, roll back to the previous state '''
            if self.con:
                self.con.rollback()
                print "Error %s\nRolled back to previous state" % e.args[0]
                
                        
    def print_table(self, table):
        '''
            Print all the rows in the given table.
        '''
        
        ''' Create the SQL query string.  The preferred way of adding the contents of variables
            into an SQL string is to use the placeholder '?' but that doesn't seem to be possible
            when the variable contains the table name.  This solution uses string formatting, but
            a program where security is an issue should really check that the table name exists
            (see e.g. discussion at
            https://stackoverflow.com/questions/3247183/variable-table-name-in-sqlite. '''
        print "printing whole table..."
        sql_string = "SELECT * FROM %s" % table
        
        try:
            cur = self.con.cursor()
            cur.execute(sql_string)

            rows = cur.fetchall()
            print ("\nTable " + table + " contains:")
            for row in rows:
                try:
                    print(row)
                except:
                    row = 0
                    print "no info in table"
                
                #print(type(row))
                #print(row[1])
        
        except lite.Error, e:
            print "Error %s\nQuery failed" % e.args[0]
                
                
    
    def update_value(self, table, key, column, value):
        '''
            This module simply updates a table in the database by selecting a
            single entry and updating the associated columns with new data 
        '''    
        
        ''' Assemble the SQL string '''
        sql_string = "UPDATE %s SET %s=? WHERE Id=?" % (table, column)
        #print(sql_string)
        
        ''' Execute the SQL statement, passing the relevant data '''
        try:
            cur = self.con.cursor()
            cur.execute(sql_string, (value, key))
            self.con.commit()   
            print "Number of rows updated: %d" % cur.rowcount
            
        except lite.Error, e:
            ''' Or, if there was an error, roll back to the previous state '''
            if self.con:
                self.con.rollback()
                print "Error %s\nRolled back to previous state" % e.args[0]
     
     
