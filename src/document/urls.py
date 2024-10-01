from django.urls import path

from .api import views

urlpatterns = [
    path('doc/', views.DocumentListAPIView.as_view(), name='doc-list'),
    path('departament/', views.DepartamentListAPIview.as_view(), name='departament-list')
]
