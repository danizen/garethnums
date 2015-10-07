from django.shortcuts import render
import random 
import builtins

def numbers(request):
    left = random.randrange(100)
    right = random.randrange(100)
    if (left < right):
        leftclasses = 'left correct'
        rightclasses = 'right wrong'
    elif (right < left):
        leftclasses = 'left wrong'
        rightclasses = 'right correct'
    else:
        leftclasses = 'left correct'
        rightclasses = 'right correct'
    return render(request, 'garethnums.html', locals())
