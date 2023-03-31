from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader


def home(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def sign_up(request):
    # template = loader.get_template('login.html')
    # return HttpResponse(template.render())

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'login.html', {'form': form})


def pricing(request):
    template = loader.get_template('pricing.html')
    return HttpResponse(template.render())


def recipe(request):
    template = loader.get_template('recipe.html')
    return HttpResponse(template.render())
