from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.test, name='test'),
    url(r'^signup/$', views.test, name='test'),
    url(r'^question/(\d+)/$', views.test, name='test'),
    url(r'^ask/', views.test, name='test'),
    url(r'^popular/$', views.test, name='test'),
    url(r'^new/$', views.test, name='test'),
    url(r'^$', views.test, name='test'),
]