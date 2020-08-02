from django.shortcuts import render , get_object_or_404 , redirect
from .models import Manager
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate , login , logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
import random
from random import randint
from django.contrib.auth.models import User , Group , Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here

def manager_list(request):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    manager = Manager.objects.all().exclude(utxt='ali')

    return render(request , 'back/manager_list.html' , {'manager':manager})


def manager_del(request , pk):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    manager = Manager.objects.get(id = pk)
    b = User.objects.filter(username = manager.utxt)
    b.delete()

    manager.delete()

    return render(request , 'back/manager_list.html' , {'manager':manager})


def manager_group(request):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    group = Group.objects.all().exclude(name = 'masteruser')


    return render(request , 'back/manager_group.html' , {'group':group})


def manager_group_add(request):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    if request.method == 'POST':

        name = request.POST.get('name')

        if not name == 0:
            if not Group.objects.filter(name = name).exists():
                group = Group(name = name)
                group.save()


    return redirect('manager_group')


def manager_group_del(request , name):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    b = Group.objects.filter(name=name)
    b.delete()

    return redirect('manager_group')


def users_groups(request , pk):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    manager = Manager.objects.get(id=pk)

    user = User.objects.get(username=manager.utxt)

    ugroup = []
    for i in user.groups.all():
        ugroup.append(i.name)

    group = Group.objects.all()

    return render(request , 'back/users_groups.html' , {'ugroup':ugroup , 'group':group , 'pk':pk})


def add_users_to_groups(request , pk):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    if request.method == 'POST':

        gname = request.POST.get('gname')

    group = Group.objects.get(name=gname)
    manager = Manager.objects.get(id=pk)
    user = User.objects.get(username=manager.utxt)
    user.groups.add(group)

    return redirect('users_groups' , pk)


def del_users_to_groups(request , pk , name):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )


    group = Group.objects.get(name=name)
    manager = Manager.objects.get(id=pk)
    user = User.objects.get(username=manager.utxt)
    user.groups.remove(group)

    return redirect('users_groups' , pk)


def manager_perms(request):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    perms = Permission.objects.all()


    return render(request , 'back/manager_perms.html' , {'perms':perms})


def manager_perms_del(request , name):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    perms = Permission.objects.filter(name=name)
    perms.delete()


    return redirect('manager_perms')


def manager_perms_add(request):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    if request.method == 'POST':

         name = request.POST.get('name')
         cname = request.POST.get('cname')

         if not Permission.objects.filter(codename = cname).exists():

             content_type = ContentType.objects.get(app_label = 'main' , model = 'main')
             permission = Permission.objects.create(codename = cname , name = name , content_type = content_type)

         else:
            error = 'This Codename Used Before '
            return render(request , 'back/error.html' , {'error' : error} )


    return redirect('manager_perms')


def users_perms(request , pk):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    manager = Manager.objects.get(id=pk)

    user = User.objects.get(username=manager.utxt)

    permission = Permission.objects.filter(user=user)

    uperms = []
    for i in permission:
        uperms.append(i.name)

    perms = Permission.objects.all()


    return render(request , 'back/users_perms.html' , {'uperms':uperms , 'pk':pk , 'perms':perms})


def users_perms_del(request , pk , name):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    manager = Manager.objects.get(id=pk)
    user = User.objects.get(username=manager.utxt)

    permission = Permission.objects.get(name=name)
    user.user_permissions.remove(permission)




    return redirect('users_perms' , pk=pk)


def users_perms_add(request , pk):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    if request.method == 'POST':

        pname = request.POST.get('pname')

        manager = Manager.objects.get(id=pk)
        user = User.objects.get(username=manager.utxt)

        permission = Permission.objects.get(name=pname)
        user.user_permissions.add(permission)




    return redirect('users_perms' , pk=pk)


def groups_perms(request , name):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    group = Group.objects.get(name=name)
    perms = group.permissions.all()

    allperms = Permission.objects.all()

    return render(request , 'back/groups_perms.html' , {'perms':perms , 'name':name , 'allperms':allperms})


def groups_perms_del(request , gname , name):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    group = Group.objects.get(name=gname)
    perms = Permission.objects.get(name=name)

    group.permissions.remove(perms)

    return redirect('groups_perms' , name=gname)


def groups_perms_add(request , name):

    #login user start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login user end

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = 'Access Denied '
        return render(request , 'back/error.html' , {'error' : error} )

    if request.method == 'POST':
         pname = request.POST.get('pname')

    group = Group.objects.get(name=name)
    perms = Permission.objects.get(name=pname)

    group.permissions.add(perms)

    return redirect('groups_perms' , name=name)
