from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django-facebook-users', 'url': 'http://pypi.python.org/pypi/django-facebook-users/0.6.0'},
	{'name':'django-federated-login', 'url': 'http://pypi.python.org/pypi/django-federated-login/1.0.0'},
	{'name':'django4facebook', 'url': 'http://pypi.python.org/pypi/django4facebook/0.1.0'},
    ]
    context = {
        'title': 'anand-crowdbotics-43',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
