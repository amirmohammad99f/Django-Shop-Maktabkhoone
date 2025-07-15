from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.IndexViews.as_view(), name='index')
]