from time import *  
import random as r

#**********Second code***********
#**************Chek mistak partest and usertest*******************

def mistake(pgTest,usertest):    #Partest==test1  and usertest==input.
    error=0
    for i in range(len(pgTest)):
        try:                                    #*********Catching error=====
            if pgTest[i]!= usertest[i]:
                error = error + 1
        except:
              error = error + 1
    return error

#*********Third code************
#**************Time working 1971 to present****************

def speed_time(initial_time,end_time,userinput):
    time_delay = end_time - initial_time
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)



#***********Start Code***********
while True:
    check = input("Ready to test : yes / no : ")
    if check=="yes":

#*********First code************
     test=["Python is a papular programming language. it was created by Guido van Rossum in 1991","my name is satyam i am user",
     "Python can be used on a server to creat web applications","The most recent major version of Python is Python 3"]
     test1=r.choice(test)
     print("        ***** typing speed *****")
     print(test1)
     print()
     print()
     initial_time = time()
     testinput=input(" Enter : ")    #************User input***************
     end_time = time()


     print("Speed : ",speed_time(initial_time,end_time,testinput)," w/sec")
     print("Error : ",mistake(test1,testinput))
    elif check=="no":
        print("Thank you")
        break
    else:
        print("Wrong input")
