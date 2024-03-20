from django.urls import path
from .views import choose_group, admin_groups

urlpatterns = [
    path('choose-group/', choose_group, name='choose_group'),
    path('admin/groups/', admin_groups, name='admin_groups'),
    # Otros patrones de URL...
]

