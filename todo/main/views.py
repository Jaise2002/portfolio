from django.shortcuts import render,redirect
from . import views
from . models import Member,mark
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def main(request):
    return render(request,'home.html')

def user_login(request):
    return render(request,'login.html')

def home(request):
    mem = Member.objects.all()
    count = Member.objects.all().count()
    return render(request,'home_todo.html',{'mem':mem,'count':count})

def dummy(request):
    mar = mark.objects.all()
    return render(request,'dummy.html',{'mar':mar})

def add(request):
    return render(request,'add.html')

def addmarks(request):
    
    return render(request,'addmark.html')

def seemarks(request):
    mem = mark.objects.all()
    return render(request,'seemark.html',{'mem':mem})


def addrec(request):
    x= request.POST['first']
    y= request.POST['last']
    z= request.POST['country']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect('/')

def addmark(request):
    z=request.POST['mark4']
    x= request.POST['mark1']
    y= request.POST['mark2']
    z= request.POST['mark3']
    mem=mark.object.get(id=id)
    mem=mark(mark1=x,mark2=y,mark3=z,id=id)
    mem.save()
    return redirect('/')

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect('/')

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x= request.POST['first']
    y= request.POST['last']
    z= request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z

    mem.save()
    return redirect('/')

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('main')
            elif user.is_staff:
                return redirect("home")
            else:
                return redirect("home")
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    return redirect('login')

def register(request):
    return render(request,'register.html')

def user_register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('login')