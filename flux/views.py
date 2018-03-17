from django.views.generic.base import TemplateView
from django.views.generic import FormView

class DynamicUrl(TemplateView):

    # template_name = "aboutus.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_template_names(self, **kwargs):
        print(self.args)
        return self.args[0] + ".html"
