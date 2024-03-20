from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from products.forms import ProductForm
from products.models import Product


# Create your views here.

@login_required
def renderProducts(request):
    products = Product.objects.all()
    total_products = products.count()
    return render(request, 'products.html',{'products':products, 'total_products' : total_products })

@login_required
def productsDetail(request, id):
    product = get_object_or_404(Product,pk = id)
    return render(request, 'products_detail.html', {'product':product})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, '¡Producto agregado correctamente!')
            return redirect('products')  # Redirige a la página de productos o a donde quieras
    else:
        form = ProductForm()
    return render(request, 'agregar_producto.html', {'form': form})