from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import  messages
from django.db.models import Q
from login.forms import CreateUserForm, Contactform, Productform, Postform
from django.contrib.auth import authenticate,login,logout
from login.models import Product, Enquire, Post


def signpage(request):
    form=CreateUserForm()
    if request.POST:
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'account was created for '+ user)
            return  redirect('login')
    return  render(request,'sign.html',{'form':form})

def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.info(request, 'username OR password incorrect')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def homepage(request):
    product = Product.objects.order_by('-date_added')
    return render(request ,'homepage.html',{'product':product})


def advert(request):
    form = Productform()
    if request.method == 'POST':
        form = Productform(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'upload successfull')
        return redirect('homepage')
    else:
     return render(request,'advert.html',{'form':form,})


def contact(request):
    form=Contactform()
    if request.POST:
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.info(request, 'Thankyou!! your feedback been has received '+ user)
    return  render(request, 'contact.html',{'form':form})

def electronics(request):
    product = Product.objects.order_by('id')
    paginator=Paginator(product,6)
    page_number=request.GET.get('page')
    product.obj=paginator.get_page(page_number)
    return  render(request,'electronics.html',{'product':product.obj,'paginator':paginator,'page_number':page_number})

def farm(request):
    product = Product.objects.order_by('id')
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    product.obj = paginator.get_page(page_number)
    return  render(request,'farm.html',{'product':product.obj,'paginator':paginator,'page_number':page_number})

def furniture(request):
    product = Product.objects.order_by('image')
    paginator = Paginator(product, 8)
    page_number = request.GET.get('page')
    product.obj = paginator.get_page(page_number)
    return render(request, 'furniture.html', {'product': product.obj, 'paginator': paginator, 'page_number': page_number})

def shoes(request):
    product = Product.objects.order_by('image')
    paginator = Paginator(product,6)
    page_number = request.GET.get('page')
    product.obj = paginator.get_page(page_number)
    return  render(request,'shoes.html',{'product':product.obj,'paginator':paginator,'page_number':page_number})

def blog(request):
    post=Post.objects.order_by('-date_added')
    paginator = Paginator(post, 10)
    page_number = request.GET.get('page')
    post.obj=paginator.get_page(page_number)
    return render(request, 'blog.html', {'post':post.obj,'paginator':paginator,'page_number':page_number})

def jobs(request):
    product=Product.objects.all()
    return  render(request,'jobs.html',{'product':product})

def about(request):
    return  render(request,'about.html')

def enquire_view(request,Enquire_id):
    if request.POST:
        name = request.POST.get('name')
        number = request.POST.get('number')
        enquireitem = Enquire()
        product = Product.objects.get(pk=Enquire_id)
        enquireitem.img = product
        enquireitem.name = name
        enquireitem.number = number
        enquireitem.save()
        return HttpResponse('your enquiry has been received..We will contact you soon')
    return render(request, 'detail.html')

def blogone(request):
    form = Postform()
    if request.POST:
        form = Postform(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return  redirect('blog')
    else:
     return render(request,'blogone.html',{'form': form})

def searchbar(request):
    if request.method == 'GET':
        search=request.GET.get('search')
        post=Post.objects.all().filter(title__icontains=search).order_by('-date_added')
        return render(request,'search.html',{'post':post})


def searchhome(request):
    if request.method == 'GET':
     search=request.GET.get('search')
     product=Product.objects.all().filter(name__icontains=search).order_by('-date_added')
     return  render(request,'searchhome.html',{'product':product})