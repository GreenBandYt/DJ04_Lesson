from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news_home'),
    path('news_add/', views.news_add, name='news_add'),
    # path('new', views.new, name='new'),
    # path('data', views.data, name='data'),
    # path('test', views.test, name='test'),
]
