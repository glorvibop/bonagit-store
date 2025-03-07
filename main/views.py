from django.shortcuts import render, redirect, reverse
from main.forms import ProductForm
from main.models import ChocolateProduct
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

@login_required(login_url='/login') # Agar main page HANYA dapat diakses oleh pengguna yang sudah login (terautentikasi)
def show_main(request):
    context = {
        'name': request.user.username, # Menampilakn nama user yang sedang logged in
        'app_name' : 'Bonagit Store',
        'my_name' : 'Shaine Glorvina Mathea',
        'my_class' : 'PBP B',
        'npm' : '2306245573',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

# Menghasilkan form yang dapat menambahkan data Product Entry secara otomatis ketika data di-submit dari form
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False) # Menambahkan informasi user sebelum objek disimpan ke database
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

# Menyimpan hasil query dari seluruh data yang ada pada entry ChocolateProduct
def show_xml(request):
    data = ChocolateProduct.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Menyimpan hasil query dari seluruh data yang ada pada entry ChocolateProduct
def show_json(request):
    data = ChocolateProduct.objects.filter(user=request.user)
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
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if(form.is_valid()):
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            date_now = datetime.datetime.now()
            date_formatted = date_now.strftime("%a, %d %B %Y (%H:%M:%S)")
            response.set_cookie('last_login',date_formatted)
            return response
        else:
            messages.error(request, "Invalid username or password :( Please try again!")
    else:
        form = AuthenticationForm

    context = {'form':form}
    return render(request,'login.html',context)

# Melakukan mekanisme logout dan menghapus cookie last_login saat pengguna melakukan logout.
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get product entry berdasarkan id
    product = ChocolateProduct.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product berdasarkan id
    product = ChocolateProduct.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

# Menambahkan product baru ke basis data dengan AJAX
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    product_name = strip_tags(request.POST.get("product_name")) # strip HTML tags! --> untuk "membersihkan" data baru
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))   # strip HTML tags! --> untuk "membersihkan" data baru
    type = strip_tags(request.POST.get("type"))
    cocoa_ratio = request.POST.get("cocoa_ratio")               # strip HTML tags! --> untuk "membersihkan" data baru
    user = request.user

    new_product = ChocolateProduct(
        product_name=product_name, price=price,
        description=description, type=type, cocoa_ratio=cocoa_ratio,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

# Integrasi Form Flutter Dengan Layanan Django
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            product_name = data["product_name"]
            price = int(data["price"])
            description = data["description"]
            type_ = data["type"]  
            cocoa_ratio = int(data["cocoa_ratio"])

            # Create a new ChocolateProduct object
            new_product = ChocolateProduct.objects.create(
                user=request.user, 
                product_name=product_name,
                price=price,
                description=description,
                type=type_,
                cocoa_ratio=cocoa_ratio,
            )
            new_product.save()

            return JsonResponse({"status": "success"}, status=200)
        except KeyError as e:
            return JsonResponse({"status": "error", "message": f"Missing field: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)