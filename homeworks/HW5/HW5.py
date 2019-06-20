# Murad Ali, alixx800, 008, HW5

#==========================================
# Name: cnt_occur
# Purpose: Takes in a list and a value (x) and returns the number of times the element is in the list
# Precondition: First parameter must a be a list      
# Input Parameter(s): mylist (list), element (element)  
# Return Value(s): Will return 0 if the list is empty, but will return a value of how many times the value (x) appears in the list 
#============================================
def cnt_occur(mylist, element):
    if mylist == []:
        return 0
    elif isinstance(mylist[0], list) == True:
        return cnt_occur(mylist[0], element) + cnt_occur(mylist[1:], element)
    elif mylist[0] == element:
        return cnt_occur(mylist[1:], element) + 1
    else:
        return cnt_occur(mylist[1:], element)

#==========================================
# Name: position
# Purpose: takes in a list and an element and returns a list of numbers corresponding to the position of every occurrence of the element in the list
# Precondition: Both parameters need to be a integer and the first parameter needs to be a list
# Input Parameter(s): mylist(list), element(element)
# Return Value(s): Returns value(s) the is computed in the helper function which is a list of the index values of that match the value of element
#============================================
def position(mylist, element):
    return helper(mylist,element,0)

#==========================================
# Name: helper
# Purpose: Takes in a parameters of position function and incorporates a count parameter, and will eventually return a value that is thrown back into the position function  
# Precondition: (What needs to be true for function to work?)
# Input Parameter(s): list (mylist), number (element), value (count)
# Return Value(s): Computes a value(s) of index(es) that value match the value of element
#============================================
def helper(mylist, element, count):
    if mylist == []:
        return []
    elif mylist[0] != element:
        return helper(mylist[1:], element, count + 1)
    else:
        return [count] + helper(mylist[1:], element, count + 1)
    
#==========================================
# Name: rm_conseq_dubs
# Purpose: takes in a list of elements and returns a new list with the consecutive duplicates of any element removed
# Precondition: values within list must be integers
# Input Parameter(s): mylist (list)
# Return Value(s): new list with the consecutive duplicates of any element removed
#============================================
def rm_conseq_dups(mylist):
    if mylist == []:
        return []
    elif len(mylist) == 1:
        return [mylist[0]]
    elif mylist[0] != mylist[1]:
        return [mylist[0]] + rm_conseq_dups(mylist[1:])
    else:
        return rm_conseq_dups(mylist[1:]) 
    

#==========================================
# Name: sequence 
# Purpose: should take in the one input parameter that represents the nth value to calculate
# Precondition: term parameter needs to be a integer
# Input Parameter(s): term (term)
# Return Value(s): return the value that represents the nth value in the sequence {3, 6, 12, 24, 48, 96, ...} 
#============================================
def sequence(term):
    if term == 1:
        return 3
    else:
        return 2 * sequence(term - 1)

#==========================================
# Name: rangeIt 
# Purpose: creates a list containing all integers within a given range.
# Precondition: start value must be equal or less than end vaul
# Input Parameter(s): start (first parameter), end (second parameter)
# Return Value(s): will return a list of values between the start and end value, or will return a single value 
#============================================
def rangeIt(start, end):
    if start == end:
        return [start]
    else:
        return [start] + rangeIt(start + 1, end) 
    
