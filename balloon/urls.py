from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from balloon.apps import BalloonConfig
from balloon.views import BalloonListView, BalloonCrateView, ClientCreateView, ClientListView

app_name = BalloonConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('balloon_list/', BalloonListView.as_view(), name='balloon-list'),
    path('balloon_create/', BalloonCrateView.as_view(), name='balloon-create'),
]