from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from balloon.forms import BalloonForm, ClientForm
from balloon.models import Balloon, Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('balloon:client_list')

class ClientListView(ListView):
    model = Client


class BalloonCrateView(CreateView):
    model = Balloon
    success_url = reverse_lazy('balloon:balloon-list')
    form_class = BalloonForm




class BalloonListView(ListView):
    model = Balloon

class BalloonUpdateView(UpdateView):
    model = Balloon
    success_url = reverse_lazy('ballon:balloon-list')

class BalloonDeleteView(DeleteView):
    model = Balloon
    success_url = reverse_lazy('ballon:balloon-list')
