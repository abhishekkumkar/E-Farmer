from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .models import farmer,labourer,seller,transport
from django.contrib import auth
from .forms import *
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def home(request):
    return render(request,'index.html',{'string':'xyz'})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def farming_practise(request):
    return render(request,'farming-practice.html')

def news_details(request):
    return render(request,'news-details.html')

def news(request):
    return render(request,'news.html')

def product_view(request):
    return render(request,'product.html')

def shop(request):
    return render(request,'shop.html')

User = get_user_model()

def farmer_signup(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data.get("f_name")
            m_name = form.cleaned_data.get("m_name")
            l_name = form.cleaned_data.get("l_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            prof_pic = form.cleaned_data.get("prof_pic")
            addr_l1 = form.cleaned_data.get("addr_l1")
            addr_l2 = form.cleaned_data.get("addr_l2")
            city = form.cleaned_data.get("city")
            state = form.cleaned_data.get("state")
            user = farmer(f_name=f_name,m_name=m_name,l_name=l_name,email = email,password = password,prof_pic=prof_pic,addr_l1=addr_l1,addr_l2=addr_l2,city=city,state=state)
            user.save()
            user2 = User.objects.create_user(username = email,email = email,password = password,first_name ='farmer')
            return redirect('/')
    else:
        form = FarmerForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

def seller_signup(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data.get("f_name")
            m_name = form.cleaned_data.get("m_name")
            l_name = form.cleaned_data.get("l_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            prof_pic = form.cleaned_data.get("prof_pic")
            b_name = form.cleaned_data.get("b_name")
            addr_l1 = form.cleaned_data.get("addr_l1")
            addr_l2 = form.cleaned_data.get("addr_l2")
            city = form.cleaned_data.get("city")
            state = form.cleaned_data.get("state")
            user = seller(f_name=f_name,m_name=m_name,l_name=l_name,email = email,password = password,prof_pic=prof_pic,b_name=b_name,addr_l1=addr_l1,addr_l2=addr_l2,city=city,state=state)
            user.save()
            user2 = User.objects.create_user(username = email,email = email,password = password,first_name ='seller')
            return redirect('/')
    else:
        form = SellerForm()
        return render(request, 'registration/signup.html', {
        'form': form
    })

def worker_signup(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            f_name = form.cleaned_data.get("f_name")
            m_name = form.cleaned_data.get("m_name")
            l_name = form.cleaned_data.get("l_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            prof_pic = form.cleaned_data.get("prof_pic")
            city = form.cleaned_data.get("city")
            state = form.cleaned_data.get("belongs_to")

            user = labourer(f_name=f_name,m_name=m_name,l_name=l_name,email = email,password = password,prof_pic=prof_pic,city=city,state=state)
            user.save()
            user2 = User.objects.create_user(username = email,email = email,password = password,first_name ='worker')
            return redirect('/')
    else:
        form = WorkerForm()
    return render(request, 'registration/signup.html', {
        'form': form,
    })


def transport_signup(request):
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data.get("f_name")
            m_name = form.cleaned_data.get("m_name")
            l_name = form.cleaned_data.get("l_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            prof_pic = form.cleaned_data.get("prof_pic")
            transport_mode = form.cleaned_data.get("transport_mode")
            weight_capacity = form.cleaned_data.get("weight_capacity")
            reg_no = form.cleaned_data.get("reg_no")
            permit_type = form.cleaned_data.get("permit_type")
            user = transport(f_name=f_name,m_name=m_name,l_name=l_name,email = email,password = password,prof_pic=prof_pic,transport_mode=transport_mode,weight_capacity=weight_capacity,reg_no=reg_no,permit_type=permit_type)
            user.save()
            user2 = User.objects.create_user(username = email,email = email,password = password,first_name ='transport')
            return redirect('/')
    else:
        form = TransportForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

def logout(request):
    auth.logout(request)
    return render(request,'index.html')

def farmer_login(request):
    form = LoginForm(request.POST)
    context = {
        "form":form,
    }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username = username,password = password)
            if user and User.objects.get(username=username).first_name=='farmer':
                context["type"]=User.objects.get(username=username).first_name
                login(request,user)                
                context["form"] = LoginForm()
                return render(request, 'index.html',context)
            else:
                redirect("/farmer/login")
        else:
            redirect("/farmer/login")

    else:
        context["form"] = LoginForm()
    return render(request, 'registration/login.html',context)

def seller_login(request):
    form = LoginForm(request.POST)
    context = {
        "form":form,
    }
    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username = username,password = password)
            if user and User.objects.get(username=username).first_name=='seller':
                context["type"]=User.objects.get(username=username).first_name
                login(request,user)                
                context["form"] = LoginForm()
                return render(request, 'index.html',context)
            else:
                redirect("/seller/login")
    else:
        context["form"] = LoginForm()
    return render(request, 'registration/login.html',context)
    
def worker_login(request):
    form = LoginForm(request.POST)
    context = {
        "form":form,
    }
    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username = username,password = password)
            if user and User.objects.get(username=username).first_name=='worker':
                context["type"]=User.objects.get(username=username).first_name
                login(request,user)                
                context["form"] = LoginForm()
                return render(request, 'index.html',context)
            else:
                redirect("/worker/login")
    else:
        context["form"] = LoginForm()
    return render(request, 'registration/login.html',context)

def transport_login(request):
    form = LoginForm(request.POST)
    context = {
        "form":form,
    }
    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username = username,password = password)
            if user and User.objects.get(username=username).first_name=='transport':
                context["type"]=User.objects.get(username=username).first_name
                login(request,user)                
                context["form"] = LoginForm()
                return render(request, 'index.html',context)
            else:
                redirect("/tranport/login")
    else:
        context["form"] = LoginForm()
    return render(request, 'registration/login.html',context)
    
def pay(request):
    return render(request,'payment.html')

