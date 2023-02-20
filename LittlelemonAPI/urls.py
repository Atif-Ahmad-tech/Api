from django.urls import path
from . import views


urlpatterns = [
    path('menu-items/', views.menu_items, name='menue-items'),
    path('menu-items/<int:id>', views.single_items, name='menue-items'),
    path('catagory/<int:pk>',views.catagory_detail, name='catagory-detail')
]