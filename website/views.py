from django.shortcuts import render
from website.models import MyApp


def index(request):
    all_apps = MyApp.objects.all()
    ctx = {
        'my_apps': all_apps,
        'page': request.path
    }
    return render(request, 'website/index.html', ctx)
