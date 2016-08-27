from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # mixing inbuilt login with custom form implementation
    url(r'^accounts/login/$', login, {'extra_context': {'next': '/'}}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
