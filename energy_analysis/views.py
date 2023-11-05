from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/login/")
def dashboard(request):
    if request.method == "GET":
        return render(
            request, "dashboard.html", context={"message": "Success"}, status=201
        )


@login_required(login_url="/auth/login/")
def profile(request):
    if request.method == "GET":
        return render(
            request, "profile_page.html", context={"message": "Success"}, status=201
        )


@login_required(login_url="/auth/login/")
def form_submit(request):
    if request.method == "GET":
        return render(
            request, "user_input.html", context={"message": "Success"}, status=201
        )
