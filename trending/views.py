from django.shortcuts import render , get_object_or_404 , redirect
from .models import Trending
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate , login , logout
from django.core.files.storage import FileSystemStorage

# Create your views here.

def trending_add(request):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    if request.method == 'POST':

        txt = request.POST.get('txt')

        if txt == '':
            error = "All Fields Required"
            return render(request , 'back/error.html' , {'error' : error})

        b = Trending(txt = txt)
        b.save()

    trendinglist = Trending.objects.all()

    return render(request , 'back/trending.html' , {'trendinglist':trendinglist})

def trending_del(request , pk):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    b = Trending.objects.filter(id= pk)
    b.delete()

    return render(request , 'back/trending.html')

def trending_edit(request , pk):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    mytxt = Trending.objects.get(id = pk).txt

    if request.method == 'POST':

        txt = request.POST.get('txt')

        if txt == '':
            error = "All Fields Required"
            return render(request , 'back/error.html' , {'error' : error})

        b = Trending.objects.get(id = pk)
        b.txt = txt
        b.save()
        return redirect('trending_add')

    return render(request , 'back/trending_edit.html' , {'mytxt':mytxt , 'pk':pk})
