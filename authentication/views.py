from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import airConditioner, consumer


# Create your views here.
@csrf_exempt
def login_api(request):
    if request.method == "GET":
        return render(
            request, "login_page.html", context={"message": "Success"}, status=201
        )
    elif request.method == "POST":
        try:
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return render(
                    request,
                    "login_page.html",
                    context={"message": "User not availabe"},
                    status=404,
                )
        except Exception as e:
            return render(
                request, "login_page.html", context={"message": "Error"}, status=501
            )


@csrf_exempt
def signup_api(request):
    if request.method == "GET":
        return render(
            request, "signup_page.html", context={"message": "Success"}, status=201
        )
    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]
        if password != cpassword:
            return render(
                request,
                "signup_page.html",
                context={"message": "Password mismatch"},
                status=401,
            )
        user = User.objects.filter(username=email).first()
        if user:
            return render(
                request,
                "signup_page.html",
                context={"message": "Account Exists"},
                status=401,
            )
        try:
            # Create a new user
            user = User.objects.create_user(username=email, password=password)
            new = consumer(id=email)
            new.save()
            login(request, user)
            return redirect("/auth/add_ac/")
        except Exception as e:
            return render(
                request, "signup_page.html", context={"message": "Error"}, status=501
            )


@login_required(login_url="/auth/login/")
def logout_api(request):
    logout(request)
    return redirect("/auth/login/")


def get_ac(request):
    if request.method == "GET":
        return render(
            request, "get_ac.html", context={"message": "Success"}, status=201
        )
    elif request.method == "POST":
        ac_data = list()
        count = 0
        while True:
            count += 1
            try:
                ac = request.POST[f"acWatts{count}"]
                ac_data.append(ac)
            except:
                break
        ac_data = list(map(int, ac_data))
        for i in ac_data:
            user = consumer.objects.get(id=request.user)
            new = airConditioner(user=user, watts=i)
            new.save()
        return redirect("/")
