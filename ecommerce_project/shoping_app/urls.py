from . import views
from django.urls import path
app_name='shoping_app'

urlpatterns = [

    path('',views.AllProdCat,name='allprodcat'),
    path('<slug:c_slug>/',views.AllProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='prodcatdetail'),
    ]