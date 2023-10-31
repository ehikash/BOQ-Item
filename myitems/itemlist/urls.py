from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.create_item, name='create_item'),
    path('edit/<int:item_id>/', views.update_item, name='edit_item'),
    path('logout/', views.logout, name="logout view")
]
