from django.contrib import admin
# Register your models here.
from .models import SignUp
from .forms import SignUpForm


class SignUpAdmin(admin.ModelAdmin):  # Allows to show the info fromm signups in the proper way
    list_display = ["__unicode__", "timestamp", "updated"]
    form = SignUpForm
    # class Meta:
    #     model = SignUp


admin.site.register(SignUp, SignUpAdmin)  # the second agr is necessary is you want to show more details
