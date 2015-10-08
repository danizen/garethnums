from django.shortcuts import render
from django.http import HttpResponse
import random 
import builtins
import garethnums

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

def version(request):
    content = str(garethnums.version)
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Length'] = len(content)
    return response

    
