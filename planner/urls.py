# planner/urls.py -- WHICH web address runs WHICH view (for the planner app).
#
# This list is basically amapping which maps the web address to a Python view.

from django.urls import path   # path() creates one mapping entry
from . import views            # "." means "this app's folder": planner/views.py

urlpatterns = [
    # This is the home page (nothing after the site address)
    # views.home = the Python function to run
    # name="home" = a nickname, so other code can say "home" instead of typing the address

    path("", views.home, name="home"),
]
