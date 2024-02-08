# myapp/test_urls.py
from django.urls import path
from francoralite.apps.francoralite_front.views.test_errors import test_view_err500
from francoralite.urls import *


urlpatterns += [
    path("test-err500/", test_view_err500, name="test_view_err500"),
]
