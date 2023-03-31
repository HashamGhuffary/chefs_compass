from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def sign_up(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())


def pricing(request):
    template = loader.get_template('pricing.html')
    return HttpResponse(template.render())


def recipe(request):
    template = loader.get_template('recipe.html')
    return HttpResponse(template.render())
