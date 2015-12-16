# coding=utf-8
from django.conf import settings
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from .models import SignUp

# Create your views here.
def home(request):
    title = "Welcome, %s" % request.user.username
    form = SignUpForm(request.POST or None)
    context = {
        "title":title,
        "form":form,
    }
    if request.user.is_authenticated():
        title = "Welcome, %s" % request.user.username

    if form.is_valid():
        """
        # You can use this variant ot save a data from from
        form.save()

        # Or this variant
        instance = form.save(commit=False)      # commit means if you want to save this data
        instance.save()                         # saving data

        # To take data from frorm you can use next:
        full_name = form.cleaned_data.get("full_name")
        """

        context = {
            "title": "Thank you",
        }

    if request.user.is_authenticated and request.user.is_staff:
        signups = []
        for item in SignUp.objects.all():
            signups.append(item)
            print(item)
        context = {
            "signups": signups
        }

    # яку саме сторінку повертати, вказаноу  другому параметрі (другйи аргумен)
    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)

    # How to get data from the form
    # Можна це зробити у циклі, якщо у  нас багато полів, бо form.cleaned_data.get - це словник
    if form.is_valid():
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        full_name = form.cleaned_data.get("full_name")
        subject = "Site contact form"
        contact_message = "%s : %s via %s"%(full_name, message, email)
        from_email = settings.EMAIL_HOST_USER
        to_email = ['stanislav.savchuk@gmail.com', from_email]
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)
        print email, message, full_name

    context = {
        "form":form,
    }

    return render(request, "forms.html", context)


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
