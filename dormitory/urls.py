from django.urls import path
from .views import DormitoryView

urlpatterns = [
    path('myroom/', DormitoryView.as_view(), name='myroom'),
    path('sorting/', DormitoryView.as_view(), name='sorting_dorm'),
]