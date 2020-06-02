from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    # print(request.user)
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def hltv_view(request, *args, **kwargs):
    my_context = {
        "title": "this is the G2 main page",
        "this_is_true": True,
        "my_number": 2,
        "my_list": ["what", "is", "happening"],
        "my_html": "<h1>Hello World</h1>"
    }
    return render(request, "hltv.html", my_context)


def blank_view(request, *args, **kwargs):
    return HttpResponse("<h1>This ARE not the page you are looking for.</h1>")
