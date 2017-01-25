from django.conf.urls import url

from dashboard.views import profile, apikeys


urlpatterns = [
    url(r'^profile/$', profile, name='profile'),
    url(r'^apikeys/$', apikeys, name='apikeys'),
]
