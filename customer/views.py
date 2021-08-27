from django.shortcuts import render,redirect

# Create your views here.
from owner.models import Mobile
from customer.models import Cart,Orders
from customer import forms
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .decorators import *
from django.utils.decorators import method_decorator
from .filters import Mobile_filter


# def registration(request):
#     form=forms.UserRegistrationForm()
#     context={"form":form}
#     if request.method=="POST":
#         form=forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("signin")
#         else:
#             context={"form":form}
#             return render(request, "registration.html", context)
#
#     return render(request,"registration.html",context)


class RegistrationView(CreateView):
    model=User
    form_class = forms.UserRegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("signin")

def Signin(request):
    form = forms.SignInForm()
    context = {"form": form}
    if request.method == "POST":
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                context={"form":form}
                return render(request, "login.html", context)

    return render(request, "login.html", context)

def signout(request):
    logout(request)
    return redirect("signin")

# def customer_home(request):
#     return render(request,"userhome.html")
@method_decorator(signin_required, name='dispatch')
class UserHome(TemplateView):
    model=Mobile
    template_name="userhome.html"
    def get(self,request,*args,**kwargs):
        mobiles=self.model.objects.all()
        return render(request,self.template_name,{"mobiles":mobiles})

@method_decorator(signin_required, name='dispatch')
class ProductDetail(TemplateView):
    model=Mobile
    template_name="product_detail.html"
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        mobile=self.model.objects.get(id=id)
        return render(request,self.template_name,{"mobile":mobile})

@method_decorator(signin_required, name='dispatch')
class AddToCart(TemplateView):
    model=Cart

    def get(self, request, *args, **kwargs):
        pid=kwargs["id"]
        product=Mobile.objects.get(id=pid)
        cart_item=self.model(mobile=product,user=request.user)
        cart_item.save()
        print("add successfully")
        return redirect("viewcart")

@method_decorator(signin_required, name='dispatch')
class ViewCart(TemplateView):
    def get(self, request, *args, **kwargs):
        cart_items=Cart.objects.filter(user=request.user,status="in_cart")

        return render(request,"view_cart.html",{"items":cart_items})


@method_decorator(signin_required, name='dispatch')
class PlaceOrder(TemplateView):
    model=Orders
    template_name = "placeorder.html"
    form_class=forms.PlaceOrderForm
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context['form']=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        cart_id=kwargs["c_id"]
        p_id=kwargs["p_id"]
        form=self.form_class(request.POST)
        if form.is_valid():
            address=form.cleaned_data["address"]
            order=self.model()
            order.address=address
            order.user=request.user
            order.product= Mobile.objects.get(id=p_id)
            order.save()
            cart_item=Cart.objects.get(id=cart_id)
            cart_item.status="order_placed"
            cart_item.save()
            return redirect("home")
        else:
            self.context['form']=form
            return render(request, self.template_name, self.context)

@method_decorator(signin_required, name='dispatch')
class MyOrders(ListView):
    model=Orders
    template_name = "list_orders.html"
    context_object_name = "orders"
    context={}

    def get(self, request, *args, **kwargs):
        orders=self.model.objects.filter(user=request.user)
        self.context["orders"]=orders
        return render(request,self.template_name,self.context)
    # def get_queryset(self):
    #     return self.model.objects.filter(user=self.request.user)

@method_decorator(signin_required, name='dispatch')
class OrderDetail(DetailView):
    model=Orders
    template_name = "order_detail.html"
    context_object_name = "order"

@method_decorator(signin_required, name='dispatch')
class OrderChangeView(UpdateView):
    model = Orders
    template_name = "orderchange.html"
    form_class = forms.OrderChangeForm
    success_url =reverse_lazy("myorders")

@method_decorator(signin_required, name='dispatch')
class OrderDeleteView(DeleteView):
    model=Orders
    template_name = "order_delete.html"
    context_object_name = "order"
    success_url = reverse_lazy("myorders")

@method_decorator(signin_required, name='dispatch')
class CancelOrderView(TemplateView):
    model=Orders

    def get(self,request,*args,**kwargs):
        id=self.kwargs["id"]
        order=self.model.objects.get(id=id,user=request.user)
        order.status="cancelled"
        order.save()
        return redirect("myorders")

@method_decorator(signin_required, name='dispatch')
class Mobile_Search(TemplateView):
    def get(self,request,*args,**kwargs):
        mobiles=Mobile.objects.all()
        mobile_filter=Mobile_filter(request.GET,queryset=mobiles)
        return render(request,"mobile_search.html",{"filter":mobile_filter})










