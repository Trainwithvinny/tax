'''
Created on 5 Jan 2019

@author: vinny
'''
import os
from read_csv import Readcsv

from grouping_data import Parse_account
from remaining_rows import SQLiteDatabase


'''HELP use the below variables to set up the data to be analysed'''
'''the only important thing here is that you end up pointing the folder with the data files - it has been set-up
which should ensure that, as long as you amend the final argument (the only argument you need to change on this page,
 you will be pointing the right direction'''
src_folder = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
print src_folder
#project_folder = os.path.split(src_folder)[0]
#print project_folder
data_folder = os.path.join(src_folder, "personal_training/data/")
print ("Data files are in " + data_folder + "\n")


#table1 = Table(data_folder, "test_file1.csv")
'''this variable runs the analysis on the folder, determined by the above argument - runs in this case = open and read'''
folder = Readcsv(data_folder)
'''this should include:
Direct costs, marketing costs, internet and phone bill (all of), travel, free sessions, training
industry magazines etc, stationary, sports clothing, subsistence on long travels, gym equipment, repairs,
gym rent, home rent $104'''

for i in Readcsv.files:
    allowed_expense = []
    output = lambda search_column, search_text, append_ingoing_or_outgoing: Parse_account(data_folder, i, search_column, search_text, append_ingoing_or_outgoing)
    print "\n"
    print "***********************************************************************"
    print "\n"
    print ">>>>>>", "File: ", i, "<<<<<<"
    print "\n"
    print "TOTAL MONEY IN: "
    output1 = output("Money_in", "0", "Money_in")
    #allowed_expense.append(output1.Return_total())
    
    print "\n"
    print "TOTAL MONEY OUT: "
    output2 = output("Money_out", "0", "Money_out")
    #allowed_expense.append(output2.Return_total())
    
#USE A LIST OF ALLOWABLE EXPENSES AND MAP THE FUNCTION TO THE LIST OF SEARCHES

    print "\n"
    print "BARK list is: "
    output3 = output("Description", "BARK", "Money_out")
    allowed_expense.append(output3.Return_total())
    
    print "\n"
    print "MOREFIT list is: "
    output4 = output("Description", "THOMSON", "Money_out")
    allowed_expense.append(output4.Return_total())
    
    print "\n"
    print "PAYPAL: "
    output5 = output("Description", "PAYPAL", "Money_out")
    #allowed_expense.append(output5.Return_total())
    
    print "\n"
    print "RENT: "
    output6 = output("Description", "RENT", "Money_out")
    #allowed_expense.append(output6.Return_total())
    
    print "\n"
    print "UCL GYM: "
    output7 = output("Description", "BLOOMSBURY FITNESS", "Money_out")
    allowed_expense.append(output7.Return_total())
    
    print "\n"
    print "HOLLAND & BARRETT: "
    output8 = output("Description", "HOLLAND", "Money_out")
    allowed_expense.append(output8.Return_total())
    
    print "\n"
    print "PHONE BILL: "
    output9 = output("Description", "O2", "Money_out")
    allowed_expense.append(output9.Return_total())
    
    print "\n"
    print "SOUTBANK GYM: "
    output10 = output("Description", "SQUAS", "Money_out")
    allowed_expense.append(output10.Return_total())
    
    print "\n"
    print "TFL: "
    output11 = output("Description", "TFL", "Money_out")
    allowed_expense.append(output11.Return_total())
    
    print "\n"
    print "Neil "
    output11 = output("Description", "NEIL", "Money_in")
    #allowed_expense.append(output11.Return_total())
    
    print "\n"
    print "Drake's: "
    output12 = output("Description", "OMNI", "Money_out")
    allowed_expense.append(output12.Return_total())
    
    print "\n"
    print "SPORTS DIRECT: "
    output13 = output("Description", "SPORTS", "Money_out")
    allowed_expense.append(output13.Return_total())
    
    print "\n"
    print "GYMBOX: "
    output14 = output("Description", "FITNESSAGENTS", "Money_out")
    allowed_expense.append(output14.Return_total())
    
    print "\n"
    print "ALI IN: "
    output14 = output("Description", "DYET", "Money_in")
    #allowed_expense.append(output14.Return_total())
    
    print "\n"
    print "JESS IN: "
    output15 = output("Description", "JESS", "Money_in")
    #allowed_expense.append(output15.Return_total())
    
    
    print "********************************* \n"
    print "********************************* \n"
    print "TOTAL MONEY IN: "
    output1 = output("Money_in", "0", "Money_in")
    #allowed_expense.append(output1.Return_total())
    
    print "\n"
    print "TOTAL MONEY OUT: "
    output2 = output("Money_out", "0", "Money_out")
    #allowed_expense.append(output2.Return_total())
    print allowed_expense
    print "****************************************************"
    print "**********", "DEDUCTIBLE EXPENSES: ", sum(allowed_expense), "************"
    print "****************************************************"



