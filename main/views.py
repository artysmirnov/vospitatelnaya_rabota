from django.shortcuts import render
from .models import Events
from django.views.generic import DetailView

def index(request):
    events=Events.objects.order_by('-date')
    return render(request,'main/index.html', {'events':events})

class EventDetailView(DetailView):
    model = Events
    template_name = 'main/details_view.html'
    context_object_name = 'post'