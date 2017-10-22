from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(?P<bk>[\w\-]+)_(?P<chapter>[\w\-]+)', views.chap_view, name='chap_view'),
    url(r'^$', views.index, name='index'),
]