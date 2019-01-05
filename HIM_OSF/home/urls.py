from home.views import indexView
from django.urls import path
urlpatterns = [
     path('', indexView.as_view(), name='index' )
 ]
