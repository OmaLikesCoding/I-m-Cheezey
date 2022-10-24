from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cheeses/', views.cheeses_index, name='index'),
    path('cheeses/<int:cheeses_id>/', views.cheeses_detail, name='detail'),
    path('cheeses/create/', views.CheeseCreate.as_view(), name='cheeses_create'),
    path('cheeses/<int:pk>/update/', views.CheeseUpdate.as_view(), name='cheeses_update'),
    path('cheeses/<int:pk>/delete/', views.CheeseDelete.as_view(), name='cheeses_delete'),
    path('cheeses/<int:cheese_id>/add_wine/', views.add_wine, name='add_wine'),
    path('dishes/', views.DishList.as_view(), name='dishes_index'),
    path('dishes/<int:pk>/', views.DishDetail.as_view(), name='dishes_detail'),
    path('dishes/create/', views.DishCreate.as_view(), name='dishes_create'),
    path('dishes/<int:pk>/update/', views.DishUpdate.as_view(), name='dishes_update'),
    path('dishes/<int:pk>/delete/', views.DishDelete.as_view(), name='dishes_delete'),
    path('cheeses/<int:cheese_id>/assoc_dish/<int:dish_id>/', views.assoc_dish, name='assoc_dish'),
    path('accounts/signup/', views.signup, name='signup'),
]