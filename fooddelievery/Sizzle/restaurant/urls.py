from django.urls import path, include
from . import views
app_name = 'restaurant'
urlpatterns = [
    path('restauranthomepage', views.restauranthomepage, name='restauranthomepage'),
     path('rrdarbar/', views.rrdarbar, name='rrdarbar'),
path('book_table/', views.book_table, name='book_table'),
    path('cancel_booking/', views.cancel_booking, name='cancel_booking'),

    ]