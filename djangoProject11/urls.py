"""djangoProject11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including anot her URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from login.views import signpage, loginpage, homepage, logoutUser, contact, electronics, farm, shoes, blog, jobs, about, \
    enquire_view, blogone, searchbar, advert, furniture, searchhome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('Enquire/<int:Enquire_id>/', enquire_view, name='Enquire'),
    path('sign/',signpage,name='sign'),
    path('login/',loginpage,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('contact/',contact,name='contact'),
    path('advert/',advert,name='advert'),
    path('electronics/',electronics,name='electronics'),
    path('farm/',farm,name='farm'),
    path('shoes/',shoes,name='shoes'),
    path('blog/',blog,name='blog'),
    path('search/',searchbar,name='search'),
    path('searchhome/',searchhome,name='searchhome'),
    path('jobs/',jobs,name='jobs'),
    path('about/',about,name='about'),
    path('blogone/',blogone,name='blogone'),
    path('furniture/',furniture,name='furniturepage'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)