from django.http import HttpResponse

# Create your views here.


def landing_page(request):
    if request.method == 'GET':
        return HttpResponse('This is a main page')
    else:
        return HttpResponse('This method doesn\'t support', status=405)
