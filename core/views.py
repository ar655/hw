from django.shortcuts import render,HttpResponse

from .models import Botlle


def  contacts(request):

    return render(request,'core/contacts.html')


def about(request):
    return render(request,'about.html')


def clients_list(request):
    context = {}
    bottles_list = Botlle.objects.all()
    context['bottles_list'] = bottles_list
    return render(request,'clients.html',context)