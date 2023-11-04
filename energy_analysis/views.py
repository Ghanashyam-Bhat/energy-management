from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/login/")
def dashboard(request):
    if request.method == "GET":
        return render(
            request, "dashboard.html", context={"message": "Success"}, status=201
        )
