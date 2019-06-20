#==========================================
# Name: sameKeys
# Purpose: looks for keys that are found in both dictionaries and returns a new dictionary that contains key:value pairs where
# the key in the new dictionary is the key found in both dictionaries, diction1 and diction2, and the new
# key’s value being a list of the values of diction1.key and diction2.key values concatenated together. 
# Precondition: must enter in two different dictionaries
# Input Parameter(s): diction1 (dictionary), diction2 (dictionary)
# Return Value(s): an empty list or a list of the values of diction1.key and diction2.key values concatenated together
#============================================
def sameKeys(diction1, diction2):
    new_dict = {}
    for x in diction1:
        if x in diction2:
            new_dict[x] = [diction1[x], diction2[x]]
    return new_dict
    

#==========================================
# Name: averageGrades
# Purpose: takes in a dictionary with keys representing students and
# values representing their grades and will return a new dictionary with keys representing students
# and values representing an average of their grades
# Precondition: a dictionary must be input
# Input Parameter(s): diction (dictionary)
# Return Value(s): an empty dictionary for zero inputs, a keyword and a 0 for no inputs matching input, or
# will return a new dictionary with keys representing students and values representing an average of their grades.
#============================================
def averageGrades(diction):
    new_dict = {}
    if diction == {}:
        return new_dict
    else:
        for x in diction:
            if diction[x] != []:
                average = int(sum(diction[x]) / len(diction[x]))
                new_dict[x] = average
            else:
                new_dict[x] = 0
        return new_dict
#==========================================
# Name: allKeys
# Purpose: (What does the function do?)
# Precondition: (What needs to be true for function to work?)
# Input Parameter(s): (Each parameter by name and what it represents)
# Return Value(s): (What gets returned? Possibilities?)
#============================================
def allKeys(diction, element):
    new_list = []
    for x in diction:
        if element in diction[x]:
            new_list.append(x)
            new_list1 = new_list.sort()
    return new_list
#==========================================
# Name: invertFiles
# Purpose: function creates a new .txt file will all words and what document
# number they exist in 
# Precondition: in order to work, doc files need to be in the same directory
# as python 
# Input Parameter(s): list_of_file_names (files)
# Return Value(s): a list of words and what document number they exist in
#============================================
import re
def invertFiles(list_of_file_names):
    new_dict = { }
    for x in list_of_file_names:
        file = open(x,"r")
        open_file = file.readline().strip()
        for a in file:
            data = re.split("[ .,:;!?1234567890\s\b]+|[\r\n]+", a.lower())
            data = filter(None, data)
            for b in data:
                if b in new_dict.keys() and open_file not in new_dict[b]:
                    new_dict[b] = new_dict[b] + [open_file]
                else:
                    new_dict[b] = [open_file]

    end = open("HW6_output.txt", 'w+')

    for x,y in sorted(new_dict.items()):
        for value in new_dict[x]:
            end.write(x +' '+str(value)+"\r\n")



        
            
           
        
        
        
    
        
        
        
        

    
            

        
            
