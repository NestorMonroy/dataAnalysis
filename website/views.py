from django.shortcuts import render
from website.models import MyApp


def index(request):
    all_apps = MyApp.objects.all()
    ctx = {
        'my_apps': all_apps,
        'app_name': request.resolver_match.app_name
    }
    return render(request, 'website/index.html', ctx)
