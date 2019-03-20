from home.views import *
from django.urls import path


urlpatterns = [
     path('', IndexView.as_view(), name='index'),
     path('home/', IndexView.as_view(), name='index'),
     path('contact/', AboutView.as_view(), name='about'),
     path('help/', RequestView.as_view(), name='req_reg'),
     path('help_req/', request_help, name='request_help'),
     path('view-request/', ViewRequest.as_view(), name='view'),
]
