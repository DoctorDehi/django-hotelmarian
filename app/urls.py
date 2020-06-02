from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from app.views import *

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pokoj/<int:pk>', DetailPokojeView.as_view(), name='detailpokoje'),
    path('rezervace', RezervovatPokojView.as_view(), name='rezervace')
]