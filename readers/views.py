from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as authlogin,logout as authlogout,authenticate
from django.contrib.auth.hashers import check_password
# Create your views here.
from public.models import Book,Author,Review,Reader

from django.contrib.auth.decorators import login_required

@login_required(login_url='logout')
def reader_home(request):
    
    return render(request,'reader_home.html')


@login_required(login_url='logout')
def view_authors(request):
    data={}
    authors=Author.objects.all()
    data['authors']=[]
    data['book_count']=[]
    for author in authors:
        book_count = author.book.count()
        data['authors'].append({'author':author,'rating':author.total_rating, 'book_count':book_count})
        print(data['authors'])

    if 'action' in request.GET:
        action=request.GET['action']
        id=request.GET['id']
        review_obj=None
    else:
        action=None
    if action=='update':
        review=Review.objects.filter(author=id,user=request.user.id).exists()
        if review:
            review_obj=Review.objects.filter(author=id,user=request.user.id)
            data['myreview']=review_obj
        data['review']=1
        print(review)

    if action=='view':
        data['allReview']="No"
        review=Review.objects.filter(author=id).exists()
        if review:
            review_obj=Review.objects.filter(author=id)
            data['allReview']=review_obj
        
        
        
    if 'submit' in request.POST:
        review=request.POST.get('review')
        rating=request.POST.get('rating')
        
       
        if review_obj:
            review_obj.update(review=review,rating=rating)
            return redirect(view_authors)
        else:
            my_review=Review.objects.create(review=review,rating=rating,user=User.objects.get(pk=request.user.id),author=Author.objects.get(pk=id))
            return redirect(view_authors)
    return render(request,'view_authors.html',data)



@login_required(login_url='logout')
def view_books(request):
    data={}
    data['books']=Book.objects.all()
    print('bokksssssssssssssssss')
    print(data['books'])

    if 'action' in request.GET:
        action=request.GET['action']
        id=request.GET['id']
        review_obj=None
    else:
        action=None
    if action=='update':
        review=Review.objects.filter(book=id,user=request.user.id).exists()
        if review:
            review_obj=Review.objects.filter(book=id,user=request.user.id)
            data['myreview']=review_obj
        data['review']=1
        print(review)

    if action=='view':
        data['allReview']="No"
        review=Review.objects.filter(book=id).exists()
        if review:
            review_obj=Review.objects.filter(book=id)
            data['allReview']=review_obj
        
        
        
    if 'submit' in request.POST:
        review=request.POST.get('review')
        rating=request.POST.get('rating')
        
       
        if review_obj:
            review_obj.update(review=review,rating=rating)
            return redirect(view_books)
        else:
            my_review=Review.objects.create(review=review,rating=rating,user=User.objects.get(pk=request.user.id),book=Book.objects.get(pk=id))
            return redirect(view_books)
    return render(request,'view_books.html',data)

