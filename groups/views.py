from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Group, UserGroup

@login_required
def choose_group(request):
    if request.method == 'POST':
        group_id = request.POST.get('group')
        if group_id:
            group = Group.objects.get(pk=group_id)
            user_group, created = UserGroup.objects.get_or_create(user=request.user, defaults={'group': group})
            if not created:
                # El usuario ya ha elegido un grupo
                return redirect('group_already_chosen')
            return redirect('home')  # Redirige a la página de inicio o donde quieras
    else:
        user_has_group = UserGroup.objects.filter(user=request.user).exists()
        if user_has_group:
            user_group_name = UserGroup.objects.get(user=request.user).group.name
            return render(request, 'groups/already_chosen.html', {'user_group_name': user_group_name})
        else:
            groups = Group.objects.all()
            # Obtener la cantidad de integrantes en cada grupo
            group_member_counts = {group.name: UserGroup.objects.filter(group=group).count() for group in groups}
            return render(request, 'groups/choose_group.html', {'groups': groups, 'group_member_counts': group_member_counts})

@login_required
def admin_groups(request):
    if not request.user.is_superuser:
        return redirect('home')  # Redirige a la página de inicio o a donde quieras
    groups = Group.objects.all()
    return render(request, 'admin_groups.html', {'groups': groups})
