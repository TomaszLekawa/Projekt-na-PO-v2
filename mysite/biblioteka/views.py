from django.http import HttpResponse


def index(request):
    return HttpResponse("Dzien dobry, witamy w bibliotece!")