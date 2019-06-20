import time
import random

class StopWatch:
#==========================================
# Name: __init__
# Purpose: sets both start and end times with the current time of day as
# returned by the time() function (from the time module)
# Precondition: need to import time library
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): nothing returned but start and end are set to time of day
#============================================
    def __init__ (self):
        self._start = time.time()
        self._end = time.time()
#==========================================
# Name: get_end
# Purpose: returns the values stored in the instance variables end
# Precondition: self._end needs to be defined earlier
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): returns the self._end value that was restored as current time of day
#============================================
    def get_end(self):
        return self._end
#==========================================
# Name: get_start
# Purpose: returns the values stored in the instance variables start
# Precondition: self._start needs to be defined earlier
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): returns the self._start value that was restored as current time of day
#============================================
    def get_start(self):
        return self._start
#==========================================
# Name: current_time
# Purpose: gets the current local time in the form: HH:MM:SS
# Precondition: need to import time library
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): returns the current local time in the form: HH:MM:SS
#============================================
    def current_time(self):
        time_1 = time.ctime().split()
        tyme = time_1[3]
        return (tyme)
#==========================================
# Name: set_start
# Purpose: will reset start to the current time
# Precondition: need to import time library earlier
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): nothing is returned but self._start is set equal to current time of day 
#============================================
    def set_start(self):
        self._start = time.time()
#==========================================
# Name: set_end
# Purpose: will reset end to the current time
# Precondition: need to import time library earlier
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): nothing is returned but self._end is set equal to current time of day 
#============================================
    def set_end(self):
        self._end = time.time()
#==========================================
# Name: elapsed_time
# Purpose: the difference between the end time and the start time
# Precondition: needs self._end and self._start to compute
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): returns the elapsed time for the stop watch as a
# float
#============================================
    def elapsed_time(self):
        return (self._end - self._start)


    
class VideoGame:
#==========================================
# Name: __init__
# Purpose: allows the programmer to create an object of type VideoGame
# with the game title, and ESRB rating
# Precondition: needs user to define
# Input Parameter(s): self (acts in place of other parameters), title (title of game),
# esrb (ESRB rating), and lst_rating (Average rating)
# Return Value(s): nothing is returned by values are being stored
#============================================
    def __init__(self, title, esrb, lst_rating):
        self.lst_rating = lst_rating
        self.title = title
        self.esrb = esrb
#==========================================
# Name: get_title
# Purpose: returns the value entered the by user as title
# Precondition: self._title needs to be defined 
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): returns the value entered the by user as title
#============================================
    def get_title(self):
        return self.title
#==========================================
# Name: get_esrb
# Purpose: returns the value entered the by user as esrb
# Precondition: self._ersb needs to be defined 
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): returns the value entered the by user as ersb
#============================================
    def get_esrb(self):
        return self.esrb
#==========================================
# Name: set_title
# Purpose: will reset the value back to self.title
# Precondition: self.tittle needs to be defined
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): nothing is returned but self._title will reset the value
# back to self.title
#============================================
    def set_title(self):
        return self.title
#==========================================
# Name: set_esrb
# Purpose: will reset the value back to self.title
# Precondition: self.tittle needs to be defined
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): nothing is returned but self._title will reset the value
# back to self.title
#============================================
    def set_esrb(self):
        return self.title
#==========================================
# Name: get_average
# Purpose: get the average value for all of the ratings for a video game
# Precondition: needs a lst_rating input of a list
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): Return the average value as an integer by truncating the original value
#============================================
    def get_average(self):
        product = 0
        for i in range(len(self.lst_rating)):
           product = self.lst_rating[i] * (i+1) + product
        total = sum(self.lst_rating)
        average = round(product / total)
        return (average)
#==========================================
# Name: __str__
# Purpose: returns a string containing the game title, ESRB rating
# and average rating in the following form
# Precondition: need self.tittle, self.esrb, and self.get_average to complete
# return statement
# Input Parameter(s): self (acts in place of other parameters)
# Return Value(s): returns a string containing the game title, ESRB rating
#============================================           
    def __str__(self):
        return ("Title: " + self.title + ", ESRB Rating: " + self.esrb + ", Average Rating: " + str(self.get_average())) 

if __name__ == '__main__':
    #Problem A Test Code
    x = StopWatch()
    print(x.current_time())
    mylist = []
    i = 0
    while i < 30000:
        mylist.append(random.randint(1, 10000))
        i += 1
    x.set_start()
    mylist.sort()
    x.set_end()
    print(x.elapsed_time())
    print(x.current_time())
    mylist_1 = []
    a = 0
    while a < 50000:
        mylist_1.append(random.randint(1,10000))
        a += 1
    x.set_start()
    mylist.sort()
    x.set_end()
    print(x.elapsed_time())
    print(x.current_time())

    #Problem B Test Code
    mylist = []
    game1 = VideoGame("Call of duty", "AO", [2, 3, 9, 2, 1])
    mylist.append(game1)
    game2 = VideoGame("Fornite", "E10", [1, 4, 3, 6, 10])
    mylist.append(game2)
    game3 = VideoGame("Fifa 19", "E", [5, 5, 5, 5, 5])
    mylist.append(game3)
    for value in mylist:
        print(value.__str__())
