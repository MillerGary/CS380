from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', admin.site.urls), #default
    url(r'^admin/', admin.site.urls),
    url(r'^film/', include('film.urls')),
]
