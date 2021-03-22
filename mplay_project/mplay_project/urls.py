"""
"""
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from player.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('player.urls')),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico.jpeg')),
    path('', HomeView, name="homepage"),
]
