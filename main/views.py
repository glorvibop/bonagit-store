from django.shortcuts import render

def show_main(request):
    context = {
        'name_product' : 'Läderach',
        'price' : '$110',
        'description' : 'Premium chocolate from Swiss with the freshest ingredients to create memorable moments of joy!',
        'type' : 'Dark Chocolate',
        'cocoa_ratio' : '80%',
        'app_name' : 'Bonagit Store',
        'name' : 'Shaine Glorvina Mathea',
        'my_class' : 'PBP B'
    }
    return render(request, "main.html", context)