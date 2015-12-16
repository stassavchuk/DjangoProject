# coding=utf-8
from django.shortcuts import render



# Create your views here.
def about(request):
    # яку саме сторінку повертати, вказаноу  другому параметрі (другйи аргумен)
    return render(request, "about.html", {})


"""
    To set something in your home.html page you should
    * type in context
        "<Something that is in home.html page>":<the text/value you want to show>
    * type in your home.html file
        "{{<Something that is in home.html page>}}

    For instance:
        context = {
            ...

            "time": datetime.datetime.now()
        }

        home.html:
                <br><h2>The current time is: {{time}}</h2>
"""
