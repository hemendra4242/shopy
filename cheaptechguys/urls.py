from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', views.Home , name='Home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('categorylist/<choice>', views.product_list, name='categorylist'),
    path('product/<name>', views.product_page, name='product'),
    path('about us', views.about_us, name='about us'),
    path('affiliate disclosure', views.affiliate_disclosure, name='affiliate disclosure'),
    path('navsearch', views.navsearch, name='navsearch'),
    path('profile', views.profile, name='profile'),
    path('contactus', views.contactus, name='contactus'),
    path('privacypolicy', views.privacy_policy, name='privacypolicy'),
    path('like/<int:pk>', views.like, name='like'),
]
