from django.shortcuts import render,redirect
from .models import Author,Reader
from django.contrib.auth.models import User
from django.contrib.auth import login as authlogin,logout as authlogout,authenticate
from django.contrib.auth.hashers import check_password
# Create your views here.

def home(request):
    
            
    return render(request,'home.html')


def login(request):

    if request.POST:
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        user=authenticate(username=uname,password=pwd)
        print(request.user)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        if user:
            authlogin(request,user)
            print(request.user)
            userpro=Author.objects.filter(user=user).exists()
            if userpro:
                author=Author.objects.get(user=user)
                
                request.session['author']=author.id
                return redirect('author_home')
            else:
                userpro=Reader.objects.filter(user=user).exists()
                if userpro:
                    reader=Reader.objects.get(user=user)
                    request.session['reader']=reader.id
                    
                    return redirect('reader_home')

        
    return render(request,'login.html')


# SINGLE TEMPLATE FOR REGISTRATION -registration.html   
def author_reg(request):
    print(request.method)
    
    if request.POST:
        print(request.POST)
        
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        name=request.POST.get('name')
        print(uname,pwd)
        checkexist=User.objects.filter(username=uname).exists()
        print(checkexist)
        flag=0
        if checkexist:
            
            checkexist=User.objects.get(username=uname)
            if check_password(pwd,checkexist.password):
                print("existtttttttttt")
                flag=1
        if flag==0:
            reg=User.objects.create_user(username=uname,password=pwd,first_name=name)
            author=Author(name=name,user=reg)
            author.save()
            
            return redirect(login)
    return render(request,'registration.html',{'type':'author'})


def reader_reg(request):
    print(request.method)
    if request.POST:
        
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        name=request.POST.get('name')
        print(uname,pwd)
        checkexist=User.objects.filter(username=uname).exists()
        print(checkexist)
        flag=0
        if checkexist:
            
            checkexist=User.objects.get(username=uname)
            if check_password(pwd,checkexist.password):
                print("existtttttttttt")
                flag=1
        if flag==0:
            reg=User.objects.create_user(username=uname,password=pwd)
            author=Reader(name=name,user=reg)
            author.save()
            
            return redirect(login)
    return render(request,'registration.html',{'type':'reader'})


def logout(request):
    authlogout(request)
    print("outtttt")
    print(request.user)
    return redirect('login')
