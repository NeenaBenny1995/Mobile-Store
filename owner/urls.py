from django.shortcuts import render
from django.urls import path
from .views import *
urlpatterns=[
  path('',OwnerHomeView.as_view(),name="base"),
  path('brands/add',create_brand,name="createbrand"),
  path('brands',view_brands,name="viewbrand"),
  path('brands/<int:id>',brand_details,name="branddetails"),
  path('brands/remove/<int:id>',remove_brand,name="removebrand"),
  path('brands/change/<int:id>',edit_brand,name="editbrand"),
  path('mobile/add',mobile_create,name="addmobile"),
  path('mobiles',mobile_list,name="listmobile"),
  path('mobile/change/<int:id>',mobile_edit,name="mobileedit"),
  path('mobile/remove/<int:id>',mobile_delete,name="mobiledelete"),
  path('mobile/<int:id>',view_mobile,name="viewmobile"),
  path('orders/',OrderListView.as_view(),name="orderlist"),
  path('orders/change/<int:pk>',OrderUpdateView.as_view(),name="orderupdate")





]