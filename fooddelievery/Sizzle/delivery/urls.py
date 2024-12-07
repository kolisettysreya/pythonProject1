from django.urls import path, include
from . import views
app_name = 'delivery'
urlpatterns = [
    path('pizzaitems', views.pizzaitems, name='pizzaitems'),
    path('icecreams', views.icecreams, name='icecreams'),
path('manchurian', views.manchurian, name='manchurian'),
path('northindian', views.northindian, name='northindian'),
path('wraps', views.wraps, name='wraps'),
path('starters', views.starters, name='starters'),
path('burgers', views.burgers, name='burgers'),
path('mocktails', views.mocktails, name='mocktails'),
path('southindian', views.southindian, name='southindian'),
path('icecreams_list/', views.icecream_list, name='icecream_list'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart_view/',views.cart_view,name='cart_view'),
    path('remove_from_cart/',views.remove_from_cart,name='remove_from_cart'),
    ]