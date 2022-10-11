from cProfile import Profile
from msilib.schema import LockPermissions
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm,UserRegisterForm,recommendForm
from .models import profile,moviedb
from django.contrib.auth.models import User
from .recommend import rec
movies=[
    {
        'title':'Avatar',
        'director':'James Cameron',
        'release_year':'2010',
        'description':'Alien Movie'
    },
    {
        'title':'Titanic',
        'director':'James Cameron',
        'release_year':'2010',
        'description':'Love Story'
    },
    {
        'title':'Interstellar',
        'director':'Chritopher Nolan',
        'release_year':'2010',
        'description':'Space Movie'
    }
]
def register(request):
    if(request.method == 'POST'):
        form=UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created! Now LogIn')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'movies/register.html',{'form':form})
@login_required
def Profile(request):
    context={
        'profile':profile.objects.all()
    }
    return render(request,'movies/profile.html',context)
def recommend(request):
    if(request.method=='POST' ):
        form=recommendForm(request.POST)
        if form.is_valid():
            movie_name=form.cleaned_data.get('movie')
            y=request.user.profile
            movie_list=rec(movie=movie_name,pf=y)
            context={
                'movie':movie_list
            }
            return render(request,'movies/recommend.html',context)
        else:
            movie_name=request.POST.get("choice")
            print(movie_name)
            x=moviedb.objects.filter(title=movie_name).first()
            y=request.user.profile
            y.title.add(x)
            return redirect('profile')
    else:
        form=recommendForm()
    return render(request,'movies/recommend.html',{'form':form})