from django.urls import path
from . import views

urlpatterns = [
    path('all_users/', views.index, name='index'),
    path('initial_info/', views.initial_info, name='initial_info'),
    path('family_info/', views.family_info, name='family_info'),
    path('professional_info/', views.professional_info, name='professional_info'),
    path('educational_info/', views.educational_info, name='educational_info'),
    path('desired_person/', views.desired_person, name='desired_person'),
    path('user_profile/<int:id>/', views.user_profile_with_all_info, name='user_profile'),
    path('user_login/', views.user_login, name='user_login'),
    path('', views.public_page, name='public'),
    path('user_admin/', views.user_admin, name='user_Admin'),
 
]