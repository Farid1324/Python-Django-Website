from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page, name='home'),
    path('thanks/', views.thanks_page, name='thanks'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/', views.report, name='report'),

    # Settings routes
    path('settings/', views.settings_page, name='settings'),
    path('settings/profile/', views.settings_profile, name='settings_profile'),
    path('settings/password/', views.settings_password, name='settings_password'),
    path('settings/preferences/', views.settings_preferences, name='settings_preferences'),
    path('settings/delete/', views.settings_delete_account, name='settings_delete_account'),

    path('export/', views.export_data, name='export_data'),
    path('expenses/add/', views.add_expense, name='add_expense'),
]
