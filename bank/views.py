from django.shortcuts import render
from django.http import JsonResponse

from .models import Bank, Client

from .forms import BankForm

def banks(request):
    clients = []
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BankForm(request.POST)
        print(form.data)
        # check whether it's valid:
        if form.is_valid():
            id = form.data.get('select')
            clients = Client.objects.filter(bank__exact = id);
    else:
        form = BankForm()


        
    return render(request,'bank.html', { 'form': form, 'clients': clients })    
