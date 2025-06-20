"""
URL configuration for college project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from college import views


urlpatterns = [
    path('superuser/', admin.site.urls),
    path("",views.homepage),
    path("main.html",views.homepage),
    path("about.html",views.aboutpage),
    path("concession.html",views.concessionpage),
    path("contact.html",views.contactpage),
    path("login.html",views.loginpage),
    path("saveContact",views.saveContact,name="saveContact"),
    path("saveConcession",views.saveConcession,name="saveConcession"),
    path('admin.html', views.adminpage, name='adminpage'),
    path("concession.html",views.add_student),
    path("delete/<int:id>/", views.deleteConcession, name="delete_concession"),
    path('print_form/<int:student_id>/', views.printable_form, name='print_form'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logout_view, name='logout'),
]
