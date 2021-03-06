from .base import *


HOST_DOMAIN = 'antinub-in.space'
DEFAULT_FROM_EMAIL = 'no-reply@antinub-in.space'
USE_HTTPS = True


# YOU SHOULDN'T NEED TO MODIFY ANYTHING BELOW THIS COMMENT
CSRF_COOKIE_SECURE = USE_HTTPS
SESSION_COOKIE_SECURE = USE_HTTPS
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.{}'.format(HOST_DOMAIN)]
