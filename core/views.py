from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import EmailSubscription

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:  # Check if the email field is not empty
            # Here you can save the email to the database or perform any other actions you need
            subscription = EmailSubscription(email=email)
            subscription.save()
            return redirect('/')
    else:
        return render(request, 'index.html')

def bloghome(request):
    return render(request, 'bloghome.html')

def blogsingle(request):
    return render(request, 'blogsingle.html')

def category(request):
    return render(request, 'category.html')

def contact(request):
    return render(request, 'contact.html')

def elements(request):
    return render(request, 'elements.html')

def price(request):
    return render(request, 'price.html')

def search(request):
    return render(request, 'search.html')

def single(request):
    return render(request, 'single.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def signup(request):
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        pass1= request.POST['password']
        pass2= request.POST['password2']

        if pass1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=name).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            elif len(pass1) < 8:
                messages.info(request, 'Password too short')
                return redirect('signup')
            elif not name.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!!")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=name, email=email, password=pass1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:   
        return render(request, 'login.html')

