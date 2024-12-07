from django.urls import path, include
from . import views
app_name='staff'

urlpatterns = [

    path('staffhomepage/',views.staffhomepage,name='staffhomepage'),
    ]