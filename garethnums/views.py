from django.shortcuts import render
import random 

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
    context = { 
        'left': left, 
        'leftclasses': leftclasses,
        'rightclasses': rightclasses,
        'right': right }
    return render(request, 'garethnums.html', context)
