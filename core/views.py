from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from articulos.models import Article
from groups.models import UserGroup
from products.models import Product
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    # Obtener los últimos productos
    latest_products = Product.objects.all().order_by('-date')[:5]
    # Obtener los últimos artículos
    latest_articles = Article.objects.all().order_by('-date_published')[:5]

    # Obtener todos los usuarios
    users = User.objects.all()

    # Crear una lista para almacenar la información de usuario y grupo
    users_with_groups = []

    # Iterar sobre cada usuario
    for user in users:
        # Obtener los grupos del usuario a través del modelo intermedio UserGroup
        user_groups = UserGroup.objects.filter(user=user)

        # Crear una lista para almacenar los nombres de los grupos
        group_names = [user_group.group.name for user_group in user_groups]

        # Crear un diccionario con la información del usuario y sus grupos
        user_info = {'user': user, 'groups': group_names}

        # Agregar el diccionario a la lista
        users_with_groups.append(user_info)

    return render(request, 'core/home.html', {'latest_products': latest_products, 'latest_articles': latest_articles, 'users_with_groups': users_with_groups})

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)


def custom_logout(request):
    logout(request)
    return redirect('home')



