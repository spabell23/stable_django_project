from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Message'}))


class DynamicUrl(FormView):
    form_class = ContactForm
    success_url= "/contactus?dc=contactus"
    # template_name = "aboutus.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_template_names(self, **kwargs):
        print(self.args)
        if self.args[0] == "":
            return "index.html"
        return self.args[0] + ".html"

    def form_valid(self, form):

        send_mail(
            'New message from Cleveland rocks website',
            form.cleaned_data['name'] + ' aka ' + form.cleaned_data['email'] + " sent this message: \n \n" + form.cleaned_data['message'],
            'hello@clevelandrocksclimbing.com',
            ['kevin@clevelandrocksclimbing.com', 'karen@clevelandrocksclimbing.com'],
            fail_silently=False,
        )
        return HttpResponseRedirect(self.get_success_url())
