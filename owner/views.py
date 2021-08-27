from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, TemplateView

from .forms import *
from .models import Brand
from django.contrib import messages
from customer.models import Orders
from customer.decorators import *
from django.utils.decorators import method_decorator

# Create your views here.
@admin_permission_required
def create_brand(request):

    form=BrandCreationForm()
    context={"form":form}
    if request.method=="POST":
        form = BrandCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("base")
        else:
            context = {"form": form}
            return render(request, "create_brand.html", context)


    return render(request,"create_brand.html",context)


@admin_permission_required
def view_brands(request):
    form=SearchForm()
    brand=Brand.objects.all()
    context={}
    context['form'] = form
    context['brands']=brand
    if request.method=="POST":
        form=SearchForm(request.POST)
        if form.is_valid():
            brand_name=form.cleaned_data["brand_name"]
            brands=Brand.objects.filter(brand_name__contains=brand_name)
            context['brands']=brands
            return render(request, 'viewbrand.html', context)
        else:
            context['form']=form
            return render(request, 'viewbrand.html', context)

    return render(request, 'viewbrand.html', context)

@admin_permission_required
def brand_details(request,id):

    brand=Brand.objects.get(id=id)
    context={}
    context['brand']=brand
    return render(request,'brand_details.html',context)


@admin_permission_required
def remove_brand(request,id):
    brand=Brand.objects.get(id=id)
    brand.delete()
    return redirect("viewbrand")


@admin_permission_required
def edit_brand(request,id):
    brand=Brand.objects.get(id=id)
    form=BrandUpdateForm(instance=brand)
    context={}
    context['form']=form
    if request.method=="POST":

        form=BrandUpdateForm(instance=brand,data=request.POST)
        if form.is_valid():
            form.save()

            return redirect("viewbrand")
        else:
            context['form']=form
            return render(request, 'edit_brand.html', context)
    return render(request,'edit_brand.html',context)

@admin_permission_required
def mobile_create(request):
    context={}
    form=MobileCreationForm()
    context['form']=form
    if request.method=="POST":
        form=MobileCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Mobile Added")
            return redirect("addmobile")
        else:
            messages.error(request,"Mobile Failtoadd")
            context={"form":form}
            return render(request, "mobile_create.html", context)

    return render(request,"mobile_create.html",context)

@admin_permission_required
def mobile_list(request):
    mobiles=Mobile.objects.all()
    context={"mobiles":mobiles}
    return render(request,"list.html",context)

@admin_permission_required
def get_object(id):
    return Mobile.objects.get(id=id)

@admin_permission_required
def mobile_edit(request,id):
    mobile=get_object(id)
    form=MobileCreationForm(instance=mobile)
    context={"form":form}
    if request.method=="POST":
        form=MobileCreationForm(instance=mobile,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmobile")
        else:
            context={"form":form}
            messages.error(request, "Failed to edit")
            return render(request, "mobile_edit.html", context)


    return render(request,"mobile_edit.html",context)

@admin_permission_required
def mobile_delete(request,id):
    form=get_object(id)
    form.delete()
    return redirect("listmobile")


def view_mobile(request,id):
    mobile = Mobile.objects.get(id=id)
    context = {}
    context['mobile'] = mobile
    return render(request, 'mobile_details.html', context)

@method_decorator(admin_permission_required, name='dispatch')
class OrderListView(ListView):
    model=Orders
    template_name="orderlist.html"
    context_object_name = "orders"
    def get_queryset(self):
        return self.model.objects.exclude(status="cancelled")

@method_decorator(admin_permission_required, name='dispatch')
class OrderUpdateView(UpdateView):
    model=Orders
    template_name = "orderupdate.html"
    form_class = UpdateOrderForm
    context_object_name = "order"
    success_url = reverse_lazy("orderlist")
    # pk_url_kwarg =
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        order=self.model.objects.get(id=self.kwargs["pk"])
        context["order"]=order
        return context
@method_decorator(admin_permission_required, name='dispatch')
class OwnerHomeView(TemplateView):
    template_name = "index.html"
    model=Orders
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count = self.model.objects.filter(status="order_placed").count()
        context["oredrcount"]=count
        context["orders"]=self.model.objects.filter(status="order_placed")
        qs=self.model.objects.filter(status="dispated")
        context["orders_dispated"] = qs
        context["orders_dispated_count"]=qs.count()

        return context




