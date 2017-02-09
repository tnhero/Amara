from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


app_name = 'mall'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.UserFormView.as_view(), name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'mall/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/mall'}, name='logout'),
    url(r'^personal/$', views.tr, name='personal')
    ]
