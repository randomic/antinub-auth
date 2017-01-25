from django.conf.urls import include, url
from django.contrib import admin

from dashboard.views import profile


urlpatterns = [
    url(r'^$', profile, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
]
