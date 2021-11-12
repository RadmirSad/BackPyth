from django.http import JsonResponse

# Create your views here.


def all_lesson_name(request):
    if request.method == 'GET':
        return JsonResponse({'cat': 'dog'})
    elif request.method == 'POST':
        return JsonResponse({'Updated successfully': 'object'})
    else:
        return JsonResponse({request.method: 'Not supported'}, status=405)


def lesson_name(request, my_id=0):
    if request.method == 'GET':
        return JsonResponse({'cat' + str(my_id): 'dog'})
    elif request.method == 'POST':
        return JsonResponse({'Updated successfully': my_id})
    else:
        return JsonResponse({request.method: 'Not supported'}, status=405)
