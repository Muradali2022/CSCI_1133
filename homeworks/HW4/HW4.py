#Murad Ali, alixx800, Lab Section 008, Homework 4

#============================================
# Name: separate_int_and_str
# Purpose: Given a list of integer and strings, create two new lists. One
#       list will contain the integers and the other list will contain the
#       strings.
# Precondition: The list will only contain ints and strings
# Input Parameter(s)
#       my_list: a list containing integers and strings
# Return Value(s)
#       -- if the input parameter is an empty list , return a list
#           with two empty lists: [ [ ], [ ] ]
#       -- else return a list with the 0th index position containing the
#           list of integers, and the 1st index position containing the
#           list of strings. If there are no ints or strings, return
#           an empty list in that position
#============================================

def separate_int_and_str(mylist):
    list_str = [ ]
    list_int = [ ]
    for x in mylist:
        result = isinstance(x, int)
        if result == True:
            list_str.append(x)
        elif result == False:
            list_int.append(x)
    int_str = [list_str, list_int]
    return int_str

#============================================
# Name: average_of_lists
# Purpose: Given a list of ints
# Precondition: The list will only contain numbers
# Input Parameter(s)
#       average_of_lists: a list containing integers
# Return Value(s)
#       -- if the input parameter is an empty list, return a list
#          with an empty list: []
#       -- else return a list with the average on of mylist 
#============================================

def average_of_lists(mylist):
    list_avg = []
    i = 0 
    for x in mylist:
        list_sum = sum(mylist[i])
        list_length = len(mylist[i])
        list_avg1 = round(list_sum / list_length)
        list_avg.append(list_avg1)
        i += 1
    return list_avg

#============================================
# Name: min_of_lists
# Purpose: Given a list of lists containing integers, the function should be
#       be able to iterate through the lists and find the smallest value
# Precondition: The list will contains lists of integers
# Input Parameter(s)
#       min_of_lists: a list of lists containing integers
# Return Value(s)
#       --  if empty list as input parameter return the empty list back
#       --  return the integear with the smallest value in all lists
#============================================

def min_of_lists(mylist):
    if mylist == []:
        return []
    else:
        initial_min = mylist[0][0]
        i = 0
        while i < len(mylist):
            x = 0
            while x < len(mylist[i]):
                if mylist[i][x] < initial_min:
                    initial_min = mylist[i][x]
                x += 1
            i += 1
        return initial_min

#============================================
# Name: greater_than
# Purpose: Given a list and an "x" integer value, the function should
#       will compute wether the values in the list are greater than the
#       x value
# Precondition: The list will only contain ints and will need an additional
#       x value integer to compare against
# Input Parameter(s)
#       my_list: a list containing integers
#       x: an integer that is used to compare against the values in my_list
# Return Value(s)
#       -- if the input parameter is an empty list , return with a "True
#       -- else return with a "True" or "False" depending on wether there is a
#       a value in my_list that is greater than x 
#============================================

def greater_than(mylist, x):
    empty = []
    i = 0
    while i < len(mylist):
        if mylist[i] > x:
            i += 1
        elif mylist[i] < x:
            return False
        
    return True

#============================================
# Name: selection_sort
# Purpose: Using the selection short algorithm, the function will
#    determine the smallest element in the list and swap it with the first element,
#    then repeat the process for the remaining elements in the list 
# Precondition: The list will only contain ints 
# Input Parameter(s)
#       selection_sort: a list containing integers from 0 to 9 
# Return Value(s)
#       -- no return statment but the result can be called upon in
#       in the terminal 
#============================================       

def selection_sort(mylist):
    for i in range(0 , len(mylist)):
        x = i
        for y in range (x + 1, len(mylist)):
            if mylist[x] > mylist[y]:
                x = y
        if x != i:
            value = mylist[i] 
            mylist[i] = mylist[x]
            mylist[x] = value
        
            
    
        
                
                
                 
                

                 
                    
            
            
        
        
    
    




