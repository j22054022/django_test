from os import name
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.first_app_index, name='first_app_index'), 
    # path('<int:id>', views.first_app_index, name='first_app_index_client'), 
    path('WSGIRequest', views.getWSGIRequest), 
    path('user', views.user, name='user'),
    path('formpage', views.form_page, name='form_page'), 
    path('userformpage', views.user_form_page, name='user_form_page'), 
    path('userregister', views.user_register, name='user_register'), 
    path('userlogin', views.user_login, name='user_login'),
    path('userlogout', views.user_logout, name='user_logout')
]
