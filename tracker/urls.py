from django.urls import path

from . import views

# app_name = 'tracker'
urlpatterns = [
    path('', views.home, name='home'),
    path('add-record/', views.add_record, name='add-record'),

]