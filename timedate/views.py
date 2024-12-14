from django.shortcuts import render
from datetime import datetime

# Create your views here.
def time(request):
    # print("hello")
    dt= datetime.now()

    t=dt.strftime("%I:%M:%S")
    a_p=dt.strftime("%p")
    # print(t)
    
    dt= datetime.now()

    d=dt.strftime("%A, %d-%b-%Y")
    # print(d)
    
    data={
        'time' : t,
        'date' : d,
        'am_pm': a_p
    }

    return render(request, 'time.html' , data)