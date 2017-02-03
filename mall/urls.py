from django.conf.urls import url
from . import views


app_name = 'mall'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup', views.UserFormView.as_view(), name='signup'),
]