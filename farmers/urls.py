from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('farming-practice/',views.farming_practise,name='farming_practice'),
    path('contact/',views.contact,name='contact'),
    path('news-details/',views.news_details,name='news_details'),
    path('news/',views.news,name='news'),
    path('shop/',views.shop,name='shop'),
    path('product/',views.product_view,name='our_product'),
    path('signup/farmer/', views.farmer_signup, name='farmer_signup'),   
    path('signup/seller/', views.seller_signup, name='seller_signup'), 
    path('signup/worker/', views.worker_signup, name='worker_signup'),
    path('signup/transport/',views.transport_signup, name='transport_signup'), 
    path('farmer/login/', views.farmer_login, name='farmer_login'),
    path('seller/login/', views.seller_login, name='seller_login'),
    path('worker/login/', views.worker_login, name='worker_login'),
    path('transport/login/', views.transport_login, name='transport_login'),
    path('logout/',views.logout,name='logout'),

    path('payment/',views.pay,name='pay')
]
