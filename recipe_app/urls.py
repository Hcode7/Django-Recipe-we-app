from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('recipe/detail/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('update-recipe/<slug:slug>', views.update_recipe, name='update_recipe'),
    path('delete-recipe/<slug:slug>/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('about/', views.about_view, name='about'),
    path('menus/', views.menu_view, name='menu')
]