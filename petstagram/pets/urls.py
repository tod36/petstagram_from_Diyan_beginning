

from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path('add/', views.pet_add_page, name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>', include([
        path('', views.pet_detail_page, name='pet-detail'),
        path('edit/', views.pet_edit_page, name='edit-pet'),
        path('delete/', views.pet_delete_page, name='delete-pet'),
    ])),
]