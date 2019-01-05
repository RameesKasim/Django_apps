from home.views import indexView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('', indexView.as_view(), name='index' )
 ]
