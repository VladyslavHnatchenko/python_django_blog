from django.http import HttpResponse


def hello(request):
    return HttpResponse('<h1>What\'s up, man?</h1>')
