from django.urls import path

from . import views


urlpatterns = [
    path('test/', views.MainView.as_view(), name='view'),
    path('designer/', views.designer, name='designer'),
    path('', views.index, name='index'),
    path('ajax/collect_words/', views.collect_words, name='collect-words'),
]
