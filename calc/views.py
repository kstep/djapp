from django.views.generic import TemplateView
import math


# Create your views here.

class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self):
        return {'PI': math.PI}
