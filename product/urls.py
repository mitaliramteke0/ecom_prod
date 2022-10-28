
from django.contrib import admin
from django.urls import path
from product import views



urlpatterns = [
    path('get_one/<int:id>', views.get_by_id),
    path('get_all', views.get_by_all),
    path('get_by_filter/<str:fil>', views.get_by_filter),

]
