from django.contrib import admin
from django.urls import path
from myApp import views
# from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProfileView,CustomLoginView
# from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home),
    path('about/', views.about, name='about'),
    path('explore/', views.explore, name='explore'),
    path('contact/', views.contact, name='contact'),
    path('saveenquiry/', views.save_enquiry,name='saveenquiry'),#contact
    path('event/', views.event_list, name='event_list'),
    path('BookGenre/', views.BookGenre, name='BookGenre'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/',views.signup, name='signup'),
    path('set_password/', views.set_password, name='set_password'),
    path('forget/', views.forget, name='forget'),
    path('mainpage/',views.mainpage, name='mainpage'),
    path('userpro/',views.userpro, name='userpro'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<str:category_name>',views.category_view, name='category'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('products/<str:section_name>/', views.products_by_section, name='products_by_section'),
    path('searching/', views.search_view, name='search_results'),
    path('blog/', views.blog_page, name='blog_page'),#blog
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





admin.site.index_title = "BIBLIOPHILES"
admin.site.site_header = "The Admin Panel" 
admin.site.site_title = "BIBLIOPHILES Site Admin"