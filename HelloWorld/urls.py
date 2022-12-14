"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin

from myweb import views as myweb_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload', myweb_views.uploadImg),
    url(r'^show/$', myweb_views.showImg),
    url(r'^artupload', myweb_views.uploadArt),
    url(r'^musupload', myweb_views.uploadMus),
    url(r'^vidupload', myweb_views.uploadVideo),
    url(r'^show/(\S+)/(\S+)/$', myweb_views.exshow),
    url('myweb/',include('myweb.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
