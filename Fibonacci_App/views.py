from django.shortcuts import render
import datetime
import time

# Create your views here.
def Fibonacci(request):

    return render(request,'Fibonacci_App/input.html')

def Fibonacci1(request):
    date=datetime.datetime.now()
    start_time=(round(time.time()*1000))
    #time.sleep(5)
    Nth_Trems = int(request.POST['num1'])
    #first two terms
    First_Numaber = 0
    Second_Number = 1
    Counter = 0 #to counts the terms
    while Counter < Nth_Trems:
        temp = First_Numaber + Second_Number
        #update the values
        First_Numaber = Second_Number
        Second_Number = temp
        Counter +=1
    results = First_Numaber
    date1=datetime.datetime.now()
    end_time=(round(time.time()*1000))
    dif = end_time-start_time
    return render(request,'Fibonacci_App/results.html',{'result':results,'time':dif,'Number':Nth_Trems},)
