from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import ChocolateProduct
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    product_entries = ChocolateProduct.objects.all()

    context = {
        'product_name' : 'Läderach',
        'price' : '$110',
        'description' : 'Premium chocolate from Swiss with the freshest ingredients to create memorable moments of joy!',
        'type' : 'Dark Chocolate',
        'cocoa_ratio' : '80%',
        'app_name' : 'Bonagit Store',
        'name' : 'Shaine Glorvina Mathea',
        'my_class' : 'PBP B',
        'product_entries' : product_entries,
    }
    return render(request, "main.html", context)

# Menghasilkan form yang dapat menambahkan data Product Entry secara otomatis ketika data di-submit dari form
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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