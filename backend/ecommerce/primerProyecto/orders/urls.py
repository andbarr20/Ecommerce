from django.urls import re_path
from .views import productListApi, categoryListApi, productCreateApi, carListApi, carItemListApi,productFoodListApi, productFarmacyListApi, productSnackListApi, productToyListApi

app_name = 'orders'

urlpatterns = [
    re_path(r"^getproducts$", productListApi.as_view(), name="getproducts"),
    re_path(r"^getcategories$", categoryListApi.as_view(), name="getcategories"),
    #re_path(r"^createOrder$", salesCheckCreateApi.as_view(), name="createOrder"),
    re_path(r"^createProduct$", productCreateApi.as_view(), name="createProduct"),
    #re_path(r"^getOrders$", orderListApi.as_view(), name="getOrders"),
    re_path(r"getCar$", carListApi.as_view(), name="getCar"),
    re_path(r"getItemCar$", carItemListApi.as_view(), name="getItemCar"),
    re_path(r"getFoodProducts$", productFoodListApi.as_view(), name="getFood"),
    re_path(r"getFarmacyProducts$", productFarmacyListApi.as_view(), name="getFarmacy"),
    re_path(r"getToyProducts$", productToyListApi.as_view(), name="getToy"),
    re_path(r"getSnackProducts$", productSnackListApi.as_view(), name="getSnack"),


]