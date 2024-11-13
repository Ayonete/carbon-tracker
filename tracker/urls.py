from django.urls import path

from . import views

# app_name = 'tracker'
urlpatterns = [
    path('', views.home, name='home'),
    path('add-record/', views.add_record, name='add-record'),
    path('edit-record/<int:record_id>/', views.edit_record, name='edit_record'),
    path('delete-record/<int:record_id>/', views.delete_record, name='delete_record'),


]