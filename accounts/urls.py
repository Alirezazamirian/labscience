from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.First.as_view(), name='first'),

]

