from django.shortcuts import render , get_object_or_404 , redirect
from .models import Newsletter
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate , login , logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
import random
from random import randint
from django.contrib.auth.models import User ,Group ,Permission
from manager.models import Manager


# Create your views here.

def news_letter(request):

    if request.method == 'POST':

        txt = request.POST.get('txt')

        res = txt.find('@')

        if not int(res) == -1:
            b = Newsletter(txt=txt , status=1)
            b.save()
        else:
            try:
                int(txt)
                b = Newsletter(txt=txt , status=2)
                b.save()
            except :
                return redirect('home')

    return redirect('home')


def news_emails(request):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    emails = Newsletter.objects.filter(status=1)


    return render(request , 'back/emails.html' , {'emails':emails})


def news_phones(request):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    phones = Newsletter.objects.filter(status=2)


    return render(request , 'back/phones.html' , {'phones':phones})


def news_txt_del(request , pk , num):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    emails = Newsletter.objects.get(id=pk)
    emails.delete()

    if int(num) == 2:
        return redirect('news_phones')

    return redirect('news_emails')


def check_mychecklist(request):

    if request.method == 'POST':

        # for i in Newsletter.objects.filter(status=1):
        #
        #     x = request.POST.get(str(i.pk))
        #     print(x)
        #     if str(x) == 'on':
        #         b = Newsletter.objects.get(pk=i.id)
        #         b.delete()


        check = request.POST.getlist('checks[]')
        print(check)
        for i in check :
            b = Newsletter.objects.get(pk=i)
            b.delete()



    return redirect('news_emails')
