from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register),
    url(r'^makeaccount/$', views.makeaccount),
    url(r'^ask/$', views.ask),
    url(r'^respond/$', views.respond),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^(?P<boardname>.*)/(?P<questionid>[0-9]+)/$', views.question),
    url(r'^(?P<boardname>.*)/$', views.board),
    # board url url(,views.board, name='board')
]
