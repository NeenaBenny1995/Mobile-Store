from django.urls import path
from .views import *
urlpatterns=[
    path("account/register",RegistrationView.as_view(),name="register"),
    path("account/signin",Signin,name="signin"),
    path("account/signout",signout,name="signout"),
    path("home", UserHome.as_view(), name="home"),
    # path('home',lambda request:render(request,"userhome.html"),name="home"),
    path("products/<int:id>",ProductDetail.as_view(),name="productdetail"),
    path("carts/<int:id>",AddToCart.as_view(),name="addtocart"),
    path("cart/",ViewCart.as_view(),name="viewcart"),
    path("placeorder/<int:c_id>/<int:p_id>",PlaceOrder.as_view(),name="placeorder"),
    path('orders/', MyOrders.as_view(), name="myorders"),
    path('orders/<int:pk>', OrderDetail.as_view(), name="orderdetail"),
    path('orders/change/<int:pk>',OrderChangeView.as_view(),name="orderchange"),
# path('orders/remove/<int:pk>',OrderDeleteView.as_view(),name="orderdelete"),
path('orders/remove/<int:id>',CancelOrderView.as_view(),name="cancelorder"),
path('mobile/search',Mobile_Search.as_view(),name="search"),




]