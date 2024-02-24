from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as authlogin,logout as authlogout,authenticate
from django.contrib.auth.hashers import check_password
# Create your views here.
from public.models import Book,Author,Review

from django.contrib.auth.decorators import login_required

@login_required(login_url='logout')
def author_home(request):
    
    return render(request,'author_home.html')


@login_required(login_url='logout')
def author_manage_book(request):
    print("rrrrrrrrrrrrrrrrrr",request.user.id)
    print(request.session['author'])
    data={}
    
    book_list=Book.objects.filter(author=request.user.id)
    data['list']=book_list
    print(book_list)
    if 'submit' in request.POST:
        print('file checkkkkk')
        print(request.FILES)
        title=request.POST.get('title')
        des=request.POST.get('des')
        img=request.FILES.get('img')

        cobj=Book.objects.create(title=title,author=Author.objects.get(pk=request.session['author']))
       
        return redirect(author_manage_book)
    
    if 'action' in request.GET:
        action=request.GET['action']
        id=request.GET['id']
    else:
        action=None
    print(request.GET)
    print(action)
    if action=='delete':
        dobj=Book.objects.filter(pk=id)
        dobj[0].delete()
        return redirect(author_manage_book)
    
    if action=='update':

        print('enter update')
        
        
        upobj=Book.objects.filter(pk=id)
        print(upobj)
        data['updater']=upobj
        
    if action=='review':
        data['allReview']='No'
        review=Review.objects.filter(book=id).exists()
        if review:
            review_obj=Review.objects.filter(book=id)
            data['allReview']=review_obj
        print(data['allReview'])
    if 'update' in request.POST:
        title=request.POST.get('title')
        
       
        print("$$$$$$$$$$$^^^^^^^^^^^^^^^^^W")
        upobj.update(title=title)
        return redirect(author_manage_book)

    return render(request,'author_manage_books.html',data)

