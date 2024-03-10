from django.contrib import admin
from django.urls import path , include
from . import views
from .views import get_the_book

app_name='librarypatrons'


urlpatterns = [
    path('searchbooks/',views.searchbooks,name='librarypatrons/searchbooks'),
    path('book_details_list/',views.book_details_list,name='book_details_list'),
    path('submit_form/',views.submit_form,name='submit_form'),
    path('addlibpatronsprofile/',views.addlibpatronsprofile,name='addlibpatronsprofile'),
    path('get_the_book/<int:book_id>/',views.get_the_book,name='get_the_book'),
    path('contactmail',views.contactmail,name='contactmail'),
    path('feedback', views.feedback, name='feedback'),
path('feedback1', views.feedback1, name='feedback1'),

]