from django.shortcuts import render

from pages.forms import carForm
from .models import Car

# Create your views here.3
data =[{"name":"salma","age":23,"salary":4000},{"name":"sara","age":24,"salary":2000},{"name":"aliaa","age":24,"salary":21000},{"name":"salwa","age":23,"salary":10000}]
dictionary = {"users" : data}
def pagesIndex(request) :
    return render(request,'pages/file.html' , dictionary)

def viewCars(request):
     return render(request,'pages/cars.html',{"cars":Car.objects.all()})

def singleCar (request,id):
    singleCar= Car.objects.get(pk = id)
    return render(request,'pages/singleCar.html',{"car":singleCar})

def createCar(request):
    Car = carForm(request.POST, request.FILES)
    if Car.is_valid():
        Car.save() 
    else :
        print("not valid")
    return render(request,'pages/createCar.html',{"form":carForm})

def  editCar (request,id):
    carID = Car.objects.get(pk = id)
    form = carForm(request.POST or None,instance=carID)
    if form.is_valid():
        form.save()
    else :
        print("not valid")
    return render(request,'pages/editCar.html',{"car" : carID,"form":form})

def deleteCar  (request,id):
    car = Car.objects.get(pk = id)
    car.delete()
    cars = Car.objects.all().order_by('id')
    return render(request,'pages/cars.html',{"cars":cars})

         