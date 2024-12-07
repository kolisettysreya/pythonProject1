from django.shortcuts import render

from .models import IceCream


# Create your views here.
def pizzaitems(request):
    return render(request,'Delivery/pizzaitems.html')
def icecreams(request):
    return render(request,'Delivery/icecreams.html')
def manchurian(request):
    return render(request,'Delivery/manchurian.html')
def northindian(request):
    return render(request,'Delivery/northindian.html')
def wraps(request):
    return render(request,'Delivery/wraps.html')
def starters(request):
    return render(request,'Delivery/starters.html')
def burgers(request):
    return render(request,'Delivery/burgers.html')
def mocktails(request):
    return render(request,'Delivery/mocktails.html')
def southindian(request):
    return render(request,'Delivery/southindian.html')
def icecream_list(request):
    # Sorting by price in ascending order
    icecreams = IceCream.objects.all().order_by('price')

    return render(request, 'icecreams.html', {'icecreams': icecreams})
import cv2
import pytesseract
from django.shortcuts import render
import numpy as np

def process_image(request):
    if request.method == 'POST':
        image = request.FILES['image']


        img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        text = pytesseract.image_to_string(thresh)

        restaurant = Restaurant(
            name="...",
            rating=...,
            delivery_time="...",
            cuisine="...",
            location="...",
            discount="..."
        )
        restaurant.save()

        return render(request, 'result.html', {'restaurant': restaurant})

    return render(request, 'upload_image.html')
# views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Cart, CartItem, Item


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from .models import Category, Item, Cart, CartItem
from .forms import AddToCartForm

# Views for Category
class CategoryListView(ListView):
    model = Category
    template_name = 'delivery:category_list.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'delivery:category_detail.html'

# Views for Item
class ItemListView(ListView):
    model = Item
    template_name = 'delivery:item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'delivery:item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddToCartForm()
        return context

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = AddToCartForm(request.POST)

    if form.is_valid():
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('delivery:cart_view', pk=pk)


def cart_view(request):
    # cart = request.user.cart
    # items = cart.items.all()
    # total_price = sum(item.quantity * item.item.price for item in items)
    #
    # context = {'items': items, 'total_price': total_price}
    return render(request,'Delivery/finalcart.html')


def remove_from_cart(request, item_pk):
    cart = request.user.cart
    cart_item = get_object_or_404(CartItem, cart=cart, item_id=item_pk)
    cart_item.delete()
    return redirect('cart')





