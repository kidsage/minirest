from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from account.models import HelloWorld

# Create your views here.

def hello_world(request):

    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # post render 반복
        # return render(request, 'account/hello_world.html', context={'hello_world_list':hello_world_list})

        return HttpResponseRedirect(reverse('account:hello_world'))

    else:

        hello_world_list = HelloWorld.objects.all()
        return render(request, 'account/hello_world.html', context={'hello_world_list':hello_world_list})