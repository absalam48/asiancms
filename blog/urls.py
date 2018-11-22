from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    #path('about/', views.AboutView.as_view(), name='about'),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('<int:pk>', views.DetailView.as_view(), name='detail')
]
