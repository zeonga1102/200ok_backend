from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoungeView.as_view(), name='lounge'),
    path('<obj_id>/', views.LoungeView.as_view(), name='lounge_comment_update'),
]