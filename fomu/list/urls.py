from django.urls import path
from . import views

urlpatterns = [
    
    path('slist', views.StudentListView.as_view(), name="slist"),
    path('add', views.StudentCreateView.as_view(), name="add"),
    path('rlist/<int:pk>/', views.StudentDetailView.as_view(), name="rlist"),
    path('elist/<int:pk>/', views.StudentUpdateView.as_view(), name="elist"),
    path('dlist/<int:pk>/', views.StudentDeleteView.as_view(), name="dlist"),
    path('', views.ListTask, name='ListTask'),
    path('UpdateTask/<str:pk>/', views.UpdateTask, name='UpdateTask'),
    path('DeleteTask/<str:pk>/', views.DeleteTask, name='DeleteTask'),
]