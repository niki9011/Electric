from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def send_email(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["name"]
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["nikiprogramist@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("send email")
    return render(request, "contact/email_sent.html", {"form": form})


def contact(request):
    form = ContactForm()
    context = {"form": form}
    return render(request, "contact/contact.html", context)
