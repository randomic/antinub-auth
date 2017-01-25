from django.conf.urls import url
from django.contrib.auth.views import login, logout

from accounts.forms import LoginForm
from accounts.views import register, activate


urlpatterns = [
    url(r'^login/$',
        login,
        {
            'template_name': 'accounts/login.djhtml',
            'authentication_form': LoginForm,
        },
        name = 'login'),
    url(r'^logout/$',
        logout,
        {
            'next_page': 'home',
        },
        name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^activate/$', activate, name='activate'),
]
