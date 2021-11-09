from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.


def all_lesson_name(request):
    if request.method == 'GET':
        return JsonResponse({'cat': 'dop'})
    elif request.method == 'POST':
        return JsonResponse('Updated successfully', safe=False)
    else:
        return HttpResponse('This method doesn\'t support', status=501)


def lesson_name(request, my_id=0):
    if request.method == 'GET':
        return JsonResponse({'cat' + str(my_id): 'dop'})
    elif request.method == 'POST':
        return JsonResponse('Updated successfully', safe=False)
    else:
        return HttpResponse('This method doesn\'t support', status=501)
