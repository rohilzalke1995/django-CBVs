from django.conf.urls import url
from basic_app import views
from django.urls import re_path, path


app_name = 'basic_app'

urlpatterns = [
    path('', views.schoollistview.as_view(), name = 'list'),
    path('<int:pk>/', views.schooldetailview.as_view(), name = 'detail'),
    path('create/', views.schoolcreateview.as_view(), name = 'create'),
    path('update/<int:pk>/', views.schoolupdateview.as_view(), name = 'update'),
    path('delete/<int:pk>/', views.schooldeleteview.as_view(), name = 'delete'),
]
