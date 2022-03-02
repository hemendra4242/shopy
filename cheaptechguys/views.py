from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.template import loader
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import Userform, ContactForm, Profileform, Commentform, wishlistform
from django.contrib.auth.decorators import login_required
from .models import Product
from datetime import datetime

def Home(request):
    offer = Product.objects.filter(type='Top').order_by('Dateofpublished')[0:1]
    products = Product.objects.order_by('Dateofpublished')[0:5]
    return render(request, 'index-4.html', {'offer':offer, 'products':products})
@login_required(login_url='profile')
def navsearch(request):
    if request.method == 'GET':
        if 'q' in request.GET:
            q = request.GET.get('q')
            data = Product.objects.filter(Title__icontains=q).order_by('-id')
            return render(request, 'searchbar.html', {'data':data})
        else:
            return render(request, 'searchbar.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
@login_required(login_url='profile')
def product_list(request, choice):
    Produc = Product.objects.filter(choice=choice)
    paginator = Paginator(Produc, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'Products':page_obj, 'choice':choice}
    return render(request, 'demo.html', context)
@login_required(login_url='profile')
def product_page(request, name):
    product = Product.objects.get(Title=name)
    pro = Product.objects.filter(choice=product.choice)
    form = Commentform
    if request.method == 'POST':
        form = Commentform(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.product = product
            form.save()
    return render(request, 'product.html', {'product':product, 'pro':pro, 'form':form})

def about_us(request):
    return render(request, 'about.html')

def privacy_policy(request):
    return render(request, 'privacy.html')

def affiliate_disclosure(request):
    return render(request, 'affiliate.html')


def profile(request):
    form = Profileform()
    if request.method == 'POST':
        form = Profileform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'profile.html', context)
@login_required(login_url='login')
def contactus(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "your message has delivered successfully")
            return redirect('contactus')
    context = {'form':form}
    return render(request, 'contactus.html', context)
@login_required(login_url='profile')
def like(request, pk):
    post = get_object_or_404(Product, id=request.POST.get('product_id'))
    post.likes.add(request.user)
    return redirect(reverse('product', kwargs={'name':post.Title}))

