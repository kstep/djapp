from django.views.generic import TemplateView, ListView
from . import models
import math


# Create your views here.

class IndexView(TemplateView):
    template_name = 'calc/index.html'

    def get_context_data(self):
        return {'PI': math.PI}


class HistoryView(ListView):
    template_name = 'calc/history.html'
    model = models.Expr
