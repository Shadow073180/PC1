from django.urls import path
from . import views

urlpatterns =[
    path('', views.user_list, name='user_list'),
    path('new/', views.new_user, name='new_user'),
    path('<int:user_id>/', views.user_detail, name='user_detail'),
    path('<int:user_id>/edit', views.edit_user, name='edit_user'),
    path('<int:user_id>/delete', views.delete_user, name='delete_user'),
    # --------------------------Pets
    path('<int:user_id>/pets', views.pets_list, name='pets_list'),
    path('<int:user_id>/pets/new', views.new_pet, name='new_pet'),
    path('<int:user_id>/pets/<int:pet_id>', views.pet_detail, name='pet_detail'),
    path('<int:user_id>/pets/<int:pet_id>/edit', views.edit_pet, name='edit_pet'),
    path('<int:user_id>/pets/<int:pet_id>/delete', views.delete_pet, name='delete_pet'),
    # -----------------------------Match
    path('<int:user_id>/matches', views.match_list, name='match_list'),
    # path('<int:user_id>/pets/<int:pet_id>/delete', views.delete_pet, name='delete_pet'),
    # path('<int:user_id>/pets/<int:pet_id>/delete', views.delete_pet, name='delete_pet'),
    # path('<int:user_id>/pets/<int:pet_id>/delete', views.delete_pet, name='delete_pet'),
    # path('<int:user_id>/pets/<int:pet_id>/delete', views.delete_pet, name='delete_pet'),
    

    
    
    
]