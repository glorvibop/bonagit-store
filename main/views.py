from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import ChocolateProduct
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login') # Agar main page HANYA dapat diakses oleh pengguna yang sudah login (terautentikasi)
def show_main(request):
    product_entries = ChocolateProduct.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'product_name' : 'Läderach',
        'price' : '$110',
        'description' : 'Premium chocolate from Swiss with the freshest ingredients to create memorable moments of joy!',
        'type' : 'Dark Chocolate',
        'cocoa_ratio' : '80%',
        'app_name' : 'Bonagit Store',
        'name' : 'Shaine Glorvina Mathea',
        'my_class' : 'PBP B',
        'npm' : '2306245573',
        'product_entries' : product_entries,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

# Menghasilkan form yang dapat menambahkan data Product Entry secara otomatis ketika data di-submit dari form
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

# Menyimpan hasil query dari seluruh data yang ada pada entry ChocolateProduct
def show_xml(request):
    data = ChocolateProduct.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Menyimpan hasil query dari seluruh data yang ada pada entry ChocolateProduct
def show_json(request):
    data = ChocolateProduct.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Menyimpan hasil query dari data dengan id tertentu yang ada pada entry ChocolateProduct
def show_xml_by_id(request, id):
    data = ChocolateProduct.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Menyimpan hasil query dari data dengan id tertentu yang ada pada entry ChocolateProduct
def show_json_by_id(request, id):
    data = ChocolateProduct.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

# Mengautentikasi pengguna yang ingin login
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

# Melakukan mekanisme logout dan menghapus cookie last_login saat pengguna melakukan logout.
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response