from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django4facebook', 'url': 'http://pypi.python.org/pypi/django4facebook/0.1.0'},
    ]
    context = {
        'title': 'anand-crowdbotics-43',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
