from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication import models as authModels
from .models import airConditionerUnits, electricityUnits, gas as GasUnits, dailyHistory


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
        ac_obj = authModels.airConditioner.objects.filter(user__id=request.user)
        ac = list()
        count = 0
        for obj in ac_obj:
            count += 1
            ac.append(f"AC-{count} used [{obj.watts} W]")
        return render(
            request,
            "user_input.html",
            context={"message": "Success", "ac_list": ac},
            status=201,
        )
    elif request.method == "POST":
        date = request.POST["date"]
        energy = float(request.POST["energy"])
        gas = float(request.POST["gas"])

        ac_data = list()
        totalAcWatt = 0

        count = 0
        ac_obj = authModels.airConditioner.objects.filter(user__id=request.user)
        ac = list()
        count = 0
        for obj in ac_obj:
            count += 1
            ac.append((obj, f"AC-{count} used [{obj.watts} W]"))
        for i in ac:
            hrs = float(request.POST[i[1]])
            ac_data.append((hrs, i[0]))
            totalAcWatt += hrs * i[0].watts

        consumerObj = authModels.consumer.objects.get(id=request.user)
        for i in ac_data:
            newAc = airConditionerUnits(date=date, time=i[0], ac=i[1])
            newAc.save()

        newGas = GasUnits(date=date, weight=gas, user=consumerObj)
        newGas.save()

        newEnergy = electricityUnits(date=date, units=energy, user=consumerObj)
        newEnergy.save()

        newHistory = dailyHistory(
            date=date,
            user=consumerObj,
            totalAc=totalAcWatt,
            totalElectricity=energy,
            totalGas=gas,
        )
        newHistory.save()

        return redirect("/")
