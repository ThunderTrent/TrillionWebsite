"""trillionizer URL Configuration

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

from django.conf.urls import url
from django.contrib import admin
from htmlService import frontPage
from material.frontend import urls as frontend_urls
from htmlService import characterJS
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'service/charactersLoad.js', characterJS, name='characterJS'),
    url(r'', frontPage, name='frontPage'),
    #url(r'', include(frontend_urls)),
]
