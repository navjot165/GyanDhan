from .views import *
from django.urls import re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

app_name = 'frontend'

urlpatterns = [

    re_path(r'^$', index, name='index'),
    re_path(r'^service$', service, name='service'),
    re_path(r'^blog$', blog, name='blog'),
    re_path(r'^contact$', contact, name='contact'),

]  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
