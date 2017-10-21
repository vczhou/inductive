from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(?P<bk>[\w\-]+)_(?P<chap>[\w\-]+)', views.index, name='index'),
]