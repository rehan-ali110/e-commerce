from django.urls import path
from . import views
app_name='shop'
urlpatterns=[
    path('',views.allProdCat,name='allProdCat'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProdCatDetail,name='ProdCatDetail'),

]
