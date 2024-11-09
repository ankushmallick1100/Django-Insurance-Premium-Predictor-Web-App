from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Contact
import joblib

model = joblib.load("static/ml/gradient_boosting_regressor.joblib")

# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        Contact(user=user, name=name, email=email, msg=msg).save()
        return render(request, 'contactus.html')
    else:
        return render(request, 'contactus.html')

def insurancePrediction(request):
    if request.method == "POST":
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))

        pred = model.predict([[age, sex, bmi, children, smoker, region]])

        context = {
            'pred': round(pred[0])
        }
        
        return render(request, 'prediction.html', context)
    else:
        return render(request, 'prediction.html')
    
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User(username=username, email=email, password=password).save()
        set_permission(username)
        return redirect('/login')
    else:    
        return render(request, 'signup.html')

def set_permission(username):
    user = User.objects.get(username=username)
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()
    
def logout_from_page(request):
    logout(request)
    return redirect('/login')