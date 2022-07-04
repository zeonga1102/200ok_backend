from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoungeView.as_view(), name='lounge'),
    path('post/', views.LoungeView.as_view(), name='comment_post'),
    path('edit/<int:obj_id>/', views.LoungeView.as_view(), name='comment_edit'),
    path('delete/<int:obj_id>/', views.LoungeView.as_view(), name='comment_delete'),
    # path('<int:obj_id>/', views.LoungeView.as_view(), name='comment_update'),
]