from django.contrib import admin
from django.urls import path , include
from . import views
app_name = 'librarian'
urlpatterns = [
    path('managebooks/',views.managebooks,name='managebooks'),
    path('add_book_details/',views.add_book_details,name='add_book_details'),
    path('view_book_details/',views.view_book_details,name='view_book_details'),
    path('edit_book_details/<int:book_id>',views.edit_book_details,name='edit_book_details'),
    path('delete_book_details/<int:book_id>', views.delete_book_details, name='delete_book_details'),
    path('book_application_list/', views.book_application_list, name='book_application_list'),

]