from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.


def prog_name(request, my_id=0):
    if request.method == 'GET':
        return JsonResponse({'Name' + str(my_id): 'Backend'})
    elif request.method == 'POST':
        return JsonResponse({'Updated successfully': my_id})
    else:
        return JsonResponse({request.method: 'Not supported'}, status=405)
