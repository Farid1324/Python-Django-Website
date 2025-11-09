"""landingpagewebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from crm import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page, name='index'),                   # Homepage
    path('thanks/', views.thanks_page, name='thanks_page'),     # Thank you page
    path('dashboard/', views.dashboard, name='dashboard'),      # Dashboard
    path('add-expense/', views.add_expense, name='add_expense'),# Add expense page
    path('report/', views.report, name='report'),               # Report page
    path('settings/', views.settings_page, name='settings'),    # Main settings page
    path('settings/profile/', views.settings_profile, name='settings_profile'),
    path('settings/password/', views.settings_password, name='settings_password'),
    path('settings/preferences/', views.settings_preferences, name='settings_preferences'),
    path('settings/delete/', views.settings_delete_account, name='settings_delete_account'),
    path('export/', views.export_data, name='export_data'),     # Data export page

    # Authentication URLs (login, logout, password change/reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
