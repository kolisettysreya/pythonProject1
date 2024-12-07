from django.shortcuts import render

# Create your views here.
def staffhomepage(request):
    return render(request,'Staff/staffhomepage.html')
