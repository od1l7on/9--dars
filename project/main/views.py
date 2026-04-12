from django.shortcuts import render, redirect
from .models import Brand, Car
from .forms import CarForm , BrandForm


def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    context = {'brands': brands, 'cars': cars}
    return render(request, 'index.html', context)


def brand_filter(request, brand_id):
    brand = Brand.objects.get(id= brand_id)
    cars = Car.objects.filter(brand=brand)
    brands = Brand.objects.all()
    context = {'brands': brands, 'cars': cars, 'selected_brand': brand}

    return render(request, 'index.html', context)


def car_detail(request, car_id):
    car = Car.objects.filter(id= car_id)
    context = {'car': car}
    return render(request, 'detail.html', context)


def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})


def add_brand(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BrandForm()

    return render(request, 'add_brand.html', {'form': form})