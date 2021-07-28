from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from accountapp.models import HelloWorld
from django.urls import reverse


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # db 목록 조회
        hello_world_list = HelloWorld.objects.all()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        # return HttpResponse('안녕하세요 바뀐게 자동으로. 오 다시 바뀌네 다시.자동저장ON')
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
