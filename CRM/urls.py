"""
URL configuration for CRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from recordLead import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_Lead, name='addLead'),
    path('show/', views.show_Lead, name='showLead'),
    path('update/', views.update_Lead, name='updateLead'),
    path('delete/<int:id>/', views.delete_Lead, name='deleteLead'),
    path('<int:id>/', views.update_Lead, name='updateLead'),
]
