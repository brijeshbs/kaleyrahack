# from django.shortcuts import render
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import *
import datetime

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    
    if request.user.admin:
        nb = Breakfast.objects.filter(dateOfEntry=datetime.datetime.now().date()).count()
        ns = Snacks.objects.filter(dateOfEntry=datetime.datetime.now().date()).count()
        brek = Breakfast.objects.filter(dateOfEntry=datetime.datetime.now().date())
        snak = Snacks.objects.filter(dateOfEntry=datetime.datetime.now().date())
        u_brek = [x.user.username for x in brek]
        u_snak = [x.user.username for x in snak]
        usrs = list(set(u_brek+u_snak))
        data = []
        for i in usrs:
            ur = User.objects.get(username=i)
            temp = []
            temp.append(ur.first_name+' '+ur.last_name)
            temp.append(ur.phone)
            if i in u_brek:
                temp.append("YES")
            else:
                temp.append("NO")
            if i in u_snak:
                temp.append("YES")
            else:
                temp.append("NO")
            
            data.append(temp)
            
        return render(request, "admin.html", {
            "no_of_breakfast": nb,
            "no_of_snacks": ns,
            "opts": data
        })

    nb = Breakfast.objects.filter(dateOfEntry=datetime.datetime.now().date()).count()
    ns = Snacks.objects.filter(dateOfEntry=datetime.datetime.now().date()).count()
    brek = Breakfast.objects.filter(user=request.user, dateOfEntry=datetime.datetime.now().date())
    snak = Snacks.objects.filter(user=request.user, dateOfEntry=datetime.datetime.now().date())
    if brek:
        already_brek = True
    else:
        already_brek = False
    if snak:
        already_snak = True
    else:
        already_snak = False
    if already_brek or already_snak:
        already_booked = True
        message = "Successfully opted-in the choices"
    else:
        already_booked = False
        message = ""
    return render(request, "user.html", {
        "message": message,
        "already_booked": already_booked,
        "no_of_breakfast": nb,
        "no_of_snacks": ns,
        "already_breakfast": already_brek,
        "already_snacks": already_snak
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
            
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        try:
            isadmin = request.POST["isadmin"]
            isadmin = True
        except:
            isadmin = False

        password = request.POST["password"]

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.phone = phone
            if isadmin:
                user.admin = True
            user.save()
        except:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def optin(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method != "POST":
        return HttpResponse("Method must be POST.")
    
    try:
        breakfast = request.POST["breakfast"]
        breakfast = True
    except:
        breakfast = False
    
    try:
        snacks = request.POST["snacks"]
        snacks = True
    except:
        snacks = False

    try:
        if breakfast:
            brk = Breakfast.objects.create(user=request.user)
        if snacks:
            snk = Snacks.objects.create(user=request.user)
        return HttpResponseRedirect(reverse("index"))
    except Exception as e:
        return HttpResponse(e)
