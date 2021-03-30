from django.shortcuts import render

# Create your views here.


def welcome(request):
    ctx = {
        'page': request.path
    }
    return render(request, 'airpollution/welcome.html', ctx)
