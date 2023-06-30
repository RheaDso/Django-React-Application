
from django.urls import path
from . import views

urlpatterns = [
    # path('posts/', views.PostView.as_view(), name= 'posts_list'),
    path('add/', views.api_add, name = 'api_add'),
    path('create-predict/', views.api_create_predict, name = 'api_create_prediction'),
    path('predict-test/', views.api_predict, name = 'api_predict'),
]
