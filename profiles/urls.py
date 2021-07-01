from os import name
from registration.models import Profile
from django.urls import path
from .views import ProfilesListView, ProfilesDetailView

profile_patterns = ([
    path('', ProfilesListView.as_view(), name='list'),   
    path('<username>/', ProfilesDetailView.as_view(), name = 'detail'),
], "profiles")