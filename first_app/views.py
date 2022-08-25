from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User
from . import forms

# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    # my_dictionary = {'insert_me': 'Hello I am from first_app/index.html'}
    return render(request, 'first_app/index.html', context=date_dict)

def users(request):
    webpages_list = User.objects.order_by('LastName')
    users_dict = {'users': webpages_list}

    return render(request, 'first_app/users.html', context=users_dict)

def sign_up(request):

    form = forms.LoggingForm()

    if request.method == 'POST':
        form = forms.LoggingForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, 'first_app/login_page.html', {'form':form})
