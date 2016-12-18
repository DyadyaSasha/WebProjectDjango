from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.another, name='another'),
    url(r'^signup/$', views.another, name='another'),
    url(r'^question/(\d+)/$', views.test, name='test'),
    url(r'^ask/', views.another, name='another'),
    url(r'^popular/$', views.another, name='another'),
    url(r'^new/$', views.another, name='another'),
]