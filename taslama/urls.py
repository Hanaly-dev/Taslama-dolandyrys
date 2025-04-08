from django.urls import path

from .views import*

urlpatterns = [
    path('', index, name='index'),
    path('taslamalar/', proyekt_list, name='proyekt-list'),
    path('taslama/<int:pk>/', proyekt_detail, name='proyekt-detail'),
    path('harytlar/', products, name='products'),
    path('login/', loginView, name='login'),
    path('logout/',logoutView, name='logout'),
    path('register/', registerView, name='register'),
    path('taslama/create/', taslama_create, name='taslama-create'),
]
