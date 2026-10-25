"""
THIS IS THE DEFAULT DJANGO COMMENTS FOR THE SAMPLE PAGE. I KEPT IT HERE FOR REFERENCE.
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# config/urls.py -- the MAIN list of web addresses for the Campus Planner Site.
# Django checks these from top to bottom for every request.

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django's built-in admin website lives at /admin/
    path("admin/", admin.site.urls),

    # Everything else is handed to the Campus Hub's planner app's own urls.py.
    # include() lets each app keep its own list of web addresses / url patterns which keeps things neat and organized.
    # This will become clearer as more URL patterns and apps are added
    path("", include("planner.urls")),
]
