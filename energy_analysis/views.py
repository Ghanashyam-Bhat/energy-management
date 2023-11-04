from django.shortcuts import render


# Create your views here.
def dashboard(request):
    if request.method == "GET":
        return render(
            request, "dashboard.html", context={"message": "Success"}, status=201
        )
