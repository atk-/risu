from django.urls import path

from . import views


urlpatterns = [
    path('designer/', views.designer, name='designer'),
    path('', views.index, name='index')
]
