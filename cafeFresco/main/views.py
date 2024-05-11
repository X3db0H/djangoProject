from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegForm
from .models import Reg
from django.http import JsonResponse


def index(request):
    return render(request, 'main/bootstrap/index.html')


def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            login = request.POST.get('login')
            if not Reg.objects.filter(login=login).exists():
                form.save()
                return redirect('thanks')
            else:
                return JsonResponse({'message': 'User with this login already exists. Please choose another login.'})

    form = RegForm

    data = {
        'form': form
    }

    return render(request, 'main/bootstrap/registration.html', data)


def thanks(request):
    data = Reg.objects.latest('id')
    return render(request, 'main/bootstrap/thanks.html', {'data': data})


def menu(request):
    return render(request, 'main/bootstrap/menu.html')


def about(request):
    return render(request, 'main/bootstrap/about.html')
