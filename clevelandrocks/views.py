from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django import forms
from results.models import Events
from django.utils import timezone

class ContactForm(forms.Form):
    name = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Message'}))

class Home(ListView):
    template_name = "index.html"
    model = Events

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):

        qs = super().get_queryset()

        return qs.filter(time_begin__gte=timezone.now())

class DynamicUrl(FormView):
    form_class = ContactForm
    success_url= "/contactus?dc=contactus"
    # template_name = "aboutus.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_template_names(self, **kwargs):

        if self.args[0] == "":
            return "index.html"
        elif self.args[0] == "favicon.ico":
            print("kevin")
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
