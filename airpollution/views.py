from django.shortcuts import render

# Create your views here.


def welcome(request):
    ctx = {
        'app_name': request.resolver_match.app_name
    }
    return render(request, 'airpollution/welcome.html', ctx)


def upload_file(request):
    ctx = {
        'app_name': request.resolver_match.app_name,
        'message_sucess': 'File uploaded successfully!'
    }
    return render(request, 'airpollution/welcome.html', ctx)
