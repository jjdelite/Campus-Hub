# planner/views.py -- WHAT HAPPENS when someone visits a Campus Hub Page?.
#
# A "view" is just a Python function. Django calls it when a browser
# asks for a URL/web address, and gives it one argument: "request"
# The view must RETURN a "response" which is what to send back to the browser which is what needs to be displayed on the page.
# HttpResponse is Django's simplest response: plain text.
from django.http import HttpResponse


def home(request):
    """The Campus Hub home page."""
    return HttpResponse("Welcome to Campus Hub!")
