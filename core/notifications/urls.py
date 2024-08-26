from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # ... другие пути
    path('', TemplateView.as_view(template_name='index.html')),
]
