from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse

# Create your views here.


def prog_name(request, my_id=0):
    if request.method == 'GET':
        return JsonResponse({'Name': 'Backend'})
    elif request.method == 'POST':
        return JsonResponse('Updated successfully', safe=False)
    else:
        return HttpResponse('This method doesn\'t support', status=501)
