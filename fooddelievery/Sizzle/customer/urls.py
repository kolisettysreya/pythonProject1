from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Order
app_name='customer'

urlpatterns = [
    path('', views.homepage, name='HomePage'),
    path('MainPage/',views.MainPage,name='MainPage'),
    path('SignUpLogic/', views.SignUpLogic, name='SignUpLogic'),
    path('SignUpCall/', views.SignUpCall, name='SignUpCall'),
    path('SignInCall/', views.SignInCall, name='SignInCall'),
    path('SignInLogic/', views.SignInLogic, name='SignInLogic'),
    path('SignOut/', views.SignOut, name='SignOut'),
    path('home123/',views.home123,name='home123'),
    path('user_feedback/', views.user_feedback, name='user_feedback'),
    path('choosing/',views.choosing,name='choosing'),
path('payment/',views.payment,name='payment'),
# path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
#     path('cart/', views.view_cart, name='cart'),
path('payonline/',views.payonline,name='payonline'),
path('order/',Order.as_view(), name='order'),
    path('Online/',views.Online, name='Online'),
    path('Cash/',views.Cash,name='Cash'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)