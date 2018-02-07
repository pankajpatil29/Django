from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^HTML/create/$', formcreate, name='formcreate'),
    url(r'^HTML/signup/$', signup, name='signup'),
    url(r'^HTML/formlogin/$', formlogin, name='formlogin'),
    url(r'^HTML/login/$', login, name='login'),
   

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
