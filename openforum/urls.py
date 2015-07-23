from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<boardname>.*)/$', views.board),
    url(r'^(?P<boardname>.*)/(?P<questionid>[0-9]+)/$', views.question),
    # board url url(,views.board, name='board')
]
