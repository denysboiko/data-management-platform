from portal.views import *


from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^$', main),
    url(r'^upload/', upload),
    url(r'^draggable/', draggable),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', admin.site.urls),
]
