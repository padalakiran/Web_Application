from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Sample.models import sd


# Create your views here.
def home(request):
    # sd.objects.all().delete()
    # with connection.cursor() as cursor:
    #     cursor.execute("DELETE FROM sqlite_sequence WHERE name='Sample_sd';")
    return render(request, "Home_page.html")


def click(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        date = request.POST['DateOfBirth']

        print(username, email, age, date)
        my_user = sd.objects.create(name=username, email=email, age=age, DateOfBirth=date)
        my_user.save()

        instances = sd.objects.all()

        # Loop through instances and print their attributes
        # for instance in instances:
        #     print(instance.id, instance.name, instance.email, instance.age, instance.DateOfBirth)

    return render(request, "Home_page.html")


def data(request):
    return render(request, "Index.html")


def datas(request):
    instances = sd.objects.all()
    return render(request, 'Data_R.html', {'instances': instances})
